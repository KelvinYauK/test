import argparse
import csv
from pathlib import Path
import xml.etree.ElementTree as ET


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Analyze KCASH XML transaction files and export flattened rows to CSV."
    )
    parser.add_argument(
        "--input-dir",
        default=".",
        help="Directory containing XML files (default: current directory).",
    )
    parser.add_argument(
        "--output",
        default="transaction_analysis.csv",
        help="Output CSV file path (default: transaction_analysis.csv).",
    )
    return parser.parse_args()


def ns_tag(namespace: str, tag: str) -> str:
    return f"{{{namespace}}}{tag}" if namespace else tag


def get_text(parent: ET.Element | None, tag: str, namespace: str = "") -> str:
    if parent is None:
        return ""
    node = parent.find(ns_tag(namespace, tag))
    return (node.text or "").strip() if node is not None and node.text else ""


def categorize_transaction(transaction_type: str, entry_type: str, oper_type: str) -> str:
    known = {
        "TRNT0101": "Base transaction",
        "TRNT1002": "Balance movement",
        "TRNT1003": "Installment charge",
        "TRNT1004": "Fee/interest debit",
        "TRNT1005": "Statement movement",
        "TRNT1052": "Repayment transfer",
        "TRNT1053": "Reversal/offset",
        "TRNT0007": "Reward/points",
    }
    base = known.get(transaction_type, "Other")
    return f"{base} | {entry_type} | {oper_type}"


def parse_xml_file(xml_path: Path) -> list[dict[str, str]]:
    tree = ET.parse(xml_path)
    root = tree.getroot()

    namespace = ""
    if root.tag.startswith("{"):
        namespace = root.tag[1:].split("}")[0]

    rows: list[dict[str, str]] = []

    file_id = get_text(root, "file_id", namespace)
    file_date = get_text(root, "file_date", namespace)

    for operation in root.findall(ns_tag(namespace, "operation")):
        oper_id = get_text(operation, "oper_id", namespace)
        oper_type = get_text(operation, "oper_type", namespace)
        oper_date = get_text(operation, "oper_date", namespace)
        merchant_number = get_text(operation, "merchant_number", namespace)
        merchant_country = get_text(operation, "merchant_country", namespace)

        issuer = operation.find(ns_tag(namespace, "issuer"))
        issuer_card_number = get_text(issuer, "card_number", namespace)
        issuer_account_number = get_text(issuer, "account_number", namespace)
        customer_number = get_text(issuer, "customer_number", namespace)

        for tx in operation.findall(ns_tag(namespace, "transaction")):
            transaction_id = get_text(tx, "transaction_id", namespace)
            transaction_type = get_text(tx, "transaction_type", namespace)
            posting_date = get_text(tx, "posting_date", namespace)

            for entry_name in ("credit_entry", "debit_entry"):
                entry = tx.find(ns_tag(namespace, entry_name))
                if entry is None:
                    continue

                account = entry.find(ns_tag(namespace, "account"))
                amount_node = entry.find(ns_tag(namespace, "amount"))

                entry_account_number = get_text(account, "account_number", namespace)
                currency = get_text(amount_node, "currency", namespace) or get_text(
                    account, "currency", namespace
                )
                amount = get_text(amount_node, "amount_value", namespace)

                rows.append(
                    {
                        "source_file": xml_path.name,
                        "file_id": file_id,
                        "file_date": file_date,
                        "oper_id": oper_id,
                        "oper_type": oper_type,
                        "oper_date": oper_date,
                        "transaction_id": transaction_id,
                        "transaction_type": transaction_type,
                        "transaction_category": categorize_transaction(
                            transaction_type, entry_name.replace("_entry", ""), oper_type
                        ),
                        "posting_date": posting_date,
                        "entry_type": entry_name.replace("_entry", ""),
                        "issuer_card_number": issuer_card_number,
                        "issuer_account_number": issuer_account_number,
                        "entry_account_number": entry_account_number,
                        "currency": currency,
                        "amount": amount,
                        "merchant_number": merchant_number,
                        "merchant_country": merchant_country,
                        "customer_number": customer_number,
                    }
                )

    return rows


def main() -> None:
    args = parse_args()
    input_dir = Path(args.input_dir)
    output_path = Path(args.output)

    xml_files = sorted(input_dir.glob("*.xml"))
    if not xml_files:
        raise SystemExit(f"No XML files found in: {input_dir.resolve()}")

    all_rows: list[dict[str, str]] = []
    for xml_file in xml_files:
        all_rows.extend(parse_xml_file(xml_file))

    headers = [
        "source_file",
        "file_id",
        "file_date",
        "oper_id",
        "oper_type",
        "oper_date",
        "transaction_id",
        "transaction_type",
        "transaction_category",
        "posting_date",
        "entry_type",
        "issuer_card_number",
        "issuer_account_number",
        "entry_account_number",
        "currency",
        "amount",
        "merchant_number",
        "merchant_country",
        "customer_number",
    ]

    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(all_rows)

    print(f"Parsed {len(xml_files)} file(s), extracted {len(all_rows)} row(s).")
    print(f"CSV written to: {output_path.resolve()}")


if __name__ == "__main__":
    main()
