import argparse
import re
from dataclasses import dataclass
from html import unescape
from pathlib import Path
from typing import Iterable
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen


@dataclass
class PromotionRule:
    url: str
    slug: str
    title: str
    promo_period: str
    invite_code: str
    new_customer_definition: str
    spend_requirement: str
    reward_summary: str
    voucher_validity: str
    customer_responsibility: str
    raw_terms_excerpt: str


def fetch_text(url: str) -> str:
    req = Request(url, headers={"User-Agent": "Mozilla/5.0 (PromotionTermsBot/1.0)"})
    with urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="ignore")


def strip_html(html: str) -> str:
    html = re.sub(r"<script[^>]*>.*?</script>", " ", html, flags=re.IGNORECASE | re.DOTALL)
    html = re.sub(r"<style[^>]*>.*?</style>", " ", html, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"<[^>]+>", " ", html)
    text = unescape(text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def discover_promotion_links(promotions_html: str, listing_url: str) -> list[str]:
    links = set()
    for match in re.findall(r'href=["\']([^"\']+)["\']', promotions_html, flags=re.IGNORECASE):
        full = urljoin(listing_url, match)
        parsed = urlparse(full)
        if parsed.netloc != "www.paykool.hk":
            continue
        if not parsed.path.startswith("/promotions/"):
            continue
        slug = parsed.path.split("/promotions/")[-1].strip("/")
        if not slug:
            continue
        if "." in slug:
            continue
        links.add(f"https://www.paykool.hk/promotions/{slug}")
    return sorted(links)


def find_value(patterns: Iterable[str], text: str) -> str:
    for p in patterns:
        m = re.search(p, text, flags=re.IGNORECASE)
        if m:
            if m.lastindex:
                return m.group(1).strip()
            return m.group(0).strip()
    return ""


def extract_title(html: str, text: str, url: str) -> str:
    m = re.search(r"<h1[^>]*>(.*?)</h1>", html, flags=re.IGNORECASE | re.DOTALL)
    if m:
        return strip_html(m.group(1))
    og = re.search(r'property=["\']og:title["\'][^>]*content=["\']([^"\']+)["\']', html, flags=re.IGNORECASE)
    if og:
        return og.group(1).strip()
    return url.rsplit("/", 1)[-1]


def extract_terms_excerpt(text: str) -> str:
    anchors = ["條款及細則", "Terms and Conditions", "一般條款"]
    start = -1
    for a in anchors:
        i = text.find(a)
        if i != -1:
            start = i
            break
    if start == -1:
        return text[:1500]
    return text[start : start + 7000]


def extract_section(text: str, heading: str, next_headings: list[str], max_len: int = 1200) -> str:
    start = text.find(heading)
    if start == -1:
        return ""
    end = len(text)
    for nh in next_headings:
        idx = text.find(nh, start + len(heading))
        if idx != -1:
            end = min(end, idx)
    return text[start:end][:max_len].strip()


def parse_promotion(url: str) -> PromotionRule:
    html = fetch_text(url)
    text = strip_html(html)
    excerpt = extract_terms_excerpt(text)

    promo_period = find_value(
        [
            r"推廣期[^0-9]{0,20}(\d{4}年\d{1,2}月\d{1,2}日[^。；]{0,60})",
            r"(\d{4}-\d{2}-\d{2}\s*至\s*\d{4}-\d{2}-\d{2})",
        ],
        excerpt,
    )
    invite_code = find_value(
        [r"邀請碼[「\"『]?([A-Za-z0-9]+)[」\"』]?", r"指定邀請碼[「\"『]?([A-Za-z0-9]+)[」\"』]?"],
        excerpt,
    )
    new_customer_definition = find_value(
        [r"全新客戶定義[^。]{0,120}。", r"全新客戶[^。]{0,120}12個月[^。]{0,120}。"],
        excerpt,
    )
    spend_requirement = find_value(
        [r"(單一簽賬或增值滿\s*HK\$?\s*\d+[\d,]*)", r"(指定簽賬要求[^。]{0,80})"],
        excerpt,
    )
    reward_summary = find_value(
        [r"(可獲高達\s*HK\$?\s*\d+[\d,]*[^。]{0,80})", r"(迎新獎賞[^。]{0,120})"],
        excerpt,
    )
    voucher_validity = find_value(
        [r"(有效日期至\s*\d{4}年\d{1,2}月\d{1,2}日)", r"(有效期[^。]{0,80})"],
        excerpt,
    )
    customer_responsibility = extract_section(
        excerpt,
        "客戶責任",
        ["免責聲明", "保留權利", "其他事項", "重要條款及細則"],
    )

    return PromotionRule(
        url=url,
        slug=urlparse(url).path.rstrip("/").split("/")[-1],
        title=extract_title(html, text, url),
        promo_period=promo_period,
        invite_code=invite_code,
        new_customer_definition=new_customer_definition,
        spend_requirement=spend_requirement,
        reward_summary=reward_summary,
        voucher_validity=voucher_validity,
        customer_responsibility=customer_responsibility,
        raw_terms_excerpt=excerpt,
    )


def base_skill_lines() -> list[str]:
    lines: list[str] = []
    lines.append("## Goal")
    lines.append("Use promotion terms from PayKool pages to validate whether a customer is eligible for this promotion reward.")
    lines.append("")
    lines.append("## Agent Input (Customer Profile)")
    lines.append("- `customer_id`")
    lines.append("- `is_new_customer` (boolean)")
    lines.append("- `application_date`")
    lines.append("- `invite_code_used`")
    lines.append("- `card_approved_date`")
    lines.append("- `transactions` (date, merchant, amount, channel)")
    lines.append("- `account_status_good` (boolean)")
    lines.append("")
    lines.append("## Agent Output")
    lines.append("`eligible` or `not_eligible`, failed checks, and evidence fields.")
    lines.append("")
    lines.append("## Core Validation Checklist")
    lines.append("1. Check promotion period.")
    lines.append("2. Check required invitation code (if any).")
    lines.append("3. Check customer type requirement (new customer / existing customer).")
    lines.append("4. Check spending requirement (amount, merchant, time window).")
    lines.append("5. Check one-time limit / duplicate redemption.")
    lines.append("6. Check account status (no overdue/invalid status).")
    lines.append("")
    return lines


def build_single_skill_md(rule: PromotionRule, output_file: Path) -> None:
    lines: list[str] = []
    lines.append(f"# Skill: {rule.title}")
    lines.append("")
    lines.extend(base_skill_lines())
    lines.append("## Promotion Rule")
    lines.append(f"- URL: {rule.url}")
    lines.append(f"- Slug: {rule.slug}")
    lines.append(f"- Promotion period: {rule.promo_period or 'Not detected'}")
    lines.append(f"- Invite code: {rule.invite_code or 'Not detected'}")
    lines.append(f"- New customer definition: {rule.new_customer_definition or 'Not detected'}")
    lines.append(f"- Spend requirement: {rule.spend_requirement or 'Not detected'}")
    lines.append(f"- Reward summary: {rule.reward_summary or 'Not detected'}")
    lines.append(f"- Voucher validity: {rule.voucher_validity or 'Not detected'}")
    lines.append(f"- Customer responsibility: {rule.customer_responsibility or 'Not detected'}")
    lines.append("")
    lines.append("## Source Excerpt")
    lines.append(rule.raw_terms_excerpt[:1800] if rule.raw_terms_excerpt else "Not detected")
    lines.append("")
    lines.append("## Refresh")
    lines.append(f"`python extract_paykool_terms.py --split --skills-dir {output_file.parent.parent.as_posix()}`")

    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text("\n".join(lines), encoding="utf-8")


def build_split_skills(rules: list[PromotionRule], skills_dir: Path) -> None:
    skills_dir.mkdir(parents=True, exist_ok=True)

    index_lines: list[str] = []
    index_lines.append("# Promotion Skills Index")
    index_lines.append("")
    index_lines.append("Each promotion has an independent `skill.md` file so agents can load only relevant rules.")
    index_lines.append("")

    for rule in rules:
        skill_file = skills_dir / rule.slug / "skill.md"
        build_single_skill_md(rule, skill_file)
        index_lines.append(f"- `{rule.slug}`: [{rule.title}]({rule.slug}/skill.md)")

    (skills_dir / "index.md").write_text("\n".join(index_lines), encoding="utf-8")


def build_skill_md(rules: list[PromotionRule], output_file: Path) -> None:
    lines: list[str] = []
    lines.append("# Skill: PayKool Promotion Terms Checker")
    lines.append("")
    lines.append("## Goal")
    lines.append("Use promotion terms from PayKool pages to validate whether a customer is eligible for each promotion reward.")
    lines.append("")
    lines.append("## Data Source")
    lines.append("- Listing page: https://www.paykool.hk/promotions")
    lines.append("- Individual promotion pages under `/promotions/<slug>`")
    lines.append("")
    lines.append("## Agent Input (Customer Profile)")
    lines.append("- `customer_id`")
    lines.append("- `is_new_customer` (boolean)")
    lines.append("- `application_date`")
    lines.append("- `invite_code_used`")
    lines.append("- `card_approved_date`")
    lines.append("- `transactions` (date, merchant, amount, channel)")
    lines.append("- `account_status_good` (boolean)")
    lines.append("")
    lines.append("## Agent Output")
    lines.append("For each promotion: `eligible` or `not_eligible`, failed checks, and evidence fields.")
    lines.append("")
    lines.append("## Core Validation Checklist")
    lines.append("1. Check promotion period.")
    lines.append("2. Check required invitation code (if any).")
    lines.append("3. Check customer type requirement (new customer / existing customer).")
    lines.append("4. Check spending requirement (amount, merchant, time window).")
    lines.append("5. Check one-time limit / duplicate redemption.")
    lines.append("6. Check account status (no overdue/invalid status).")
    lines.append("")
    lines.append("## Extracted Promotion Rules")
    lines.append("")

    for i, r in enumerate(rules, start=1):
        lines.append(f"### {i}. {r.title}")
        lines.append(f"- URL: {r.url}")
        lines.append(f"- Promotion period: {r.promo_period or 'Not detected'}")
        lines.append(f"- Invite code: {r.invite_code or 'Not detected'}")
        lines.append(f"- New customer definition: {r.new_customer_definition or 'Not detected'}")
        lines.append(f"- Spend requirement: {r.spend_requirement or 'Not detected'}")
        lines.append(f"- Reward summary: {r.reward_summary or 'Not detected'}")
        lines.append(f"- Voucher validity: {r.voucher_validity or 'Not detected'}")
        lines.append("")

    lines.append("## Runbook")
    lines.append("1. Refresh rules from website with the script.")
    lines.append("2. Load customer profile and transactions.")
    lines.append("3. Evaluate checks in order and store pass/fail evidence.")
    lines.append("4. Return decision and reasons.")
    lines.append("")
    lines.append("## Refresh Command")
    lines.append("`python extract_paykool_terms.py --output-skill skill.md`")

    output_file.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch PayKool promotions and build skill.md for agent checks.")
    parser.add_argument("--listing-url", default="https://www.paykool.hk/promotions")
    parser.add_argument("--output-skill", default="skill.md")
    parser.add_argument("--skills-dir", default="skills", help="Output directory for split promotion skills")
    parser.add_argument("--split", action="store_true", help="Generate one independent skill.md per promotion")
    parser.add_argument("--limit", type=int, default=0, help="Optional max promotion pages to parse")
    args = parser.parse_args()

    listing_html = fetch_text(args.listing_url)
    promo_links = discover_promotion_links(listing_html, args.listing_url)
    if args.limit > 0:
        promo_links = promo_links[: args.limit]

    rules: list[PromotionRule] = []
    for url in promo_links:
        try:
            rules.append(parse_promotion(url))
            print(f"Parsed: {url}")
        except Exception as ex:
            print(f"Skipped {url}: {ex}")

    if not rules:
        raise SystemExit("No promotion rules parsed.")

    if args.split:
        build_split_skills(rules, Path(args.skills_dir))
        print(f"split skills written to: {Path(args.skills_dir).resolve()}")
    else:
        build_skill_md(rules, Path(args.output_skill))
        print(f"skill file written: {Path(args.output_skill).resolve()}")


if __name__ == "__main__":
    main()
