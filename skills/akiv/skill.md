# Skill: 【👟 PayKool x AKIV｜迎新消費獎賞及持卡人專屬禮遇 ✨】

## Goal
Use promotion terms from PayKool pages to validate whether a customer is eligible for this promotion reward.

## Agent Input (Customer Profile)
- `customer_id`
- `is_new_customer` (boolean)
- `application_date`
- `invite_code_used`
- `card_approved_date`
- `transactions` (date, merchant, amount, channel)
- `account_status_good` (boolean)

## Agent Output
`eligible` or `not_eligible`, failed checks, and evidence fields.

## Core Validation Checklist
1. Check promotion period.
2. Check required invitation code (if any).
3. Check customer type requirement (new customer / existing customer).
4. Check spending requirement (amount, merchant, time window).
5. Check one-time limit / duplicate redemption.
6. Check account status (no overdue/invalid status).

## Promotion Rule
- URL: https://www.paykool.hk/promotions/akiv
- Slug: akiv
- Promotion period: 2026年5月12日至2026年8月11日(包括首尾兩日) (「推廣期」)
- Invite code: PPAKIV
- New customer definition: 全新客戶定義 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: 指定簽賬要求」），可獲 $400免找數簽賬額
- Reward summary: 迎新獎賞」推廣優惠之條款及細則 PayKool信用卡「PayKool x Apple Pay加卡賞」推廣活動條款及細則（「本條款及細則」) PayKool Visa Platinum卡「PayKool x Bar Pacific迎新獎賞」及「Pay
- Voucher validity: 有效期至2026年8月11日，逾期無效
- Customer responsibility: 客戶責任 客戶須於付款前聲明享用有關優惠，並以PayKool卡全數簽賬方可享優惠。 如有任何爭議，客戶必須提供有關之文件之正本、交易單據及信用卡簽賬存根正本(如適用)以便本公司作進一步調查。 有關獎賞不可退回、轉讓/轉售、兌換折扣或換取其他優惠。如有遺失、失效或逾期，恕不獲補發。 若合資格客戶於得到有關獎賞後一年內取消PayKool卡，將會被收取PayKool卡年費 HK$1,800。 本公司保留給予客戶此優惠之權利，客戶於PayKool卡生效後，PayKool卡戶口須於發放此優惠前維持良好狀況，包括但不限於沒有逾期還款紀錄、未有逾額情況或任何違反信用卡持卡人合約條款的行為。否則，本公司保留對客戶撤回此優惠之獲得權利而毋須事先通知。

## Source Excerpt
條款及細則約束 立即申請 PayKool 信用卡 [PayKool x AKIV]優惠– PayKool信用卡迎新推廣及持卡人禮遇(「本推廣活動」)之條款及細則 任何人士參與 K Cash Limited（「本公司」）旗下 PayKool 信用卡品牌與 AKIV（「商戶」）聯合推出的本推廣活動，即表示已充分了解並同意受本條款及細則的約束。 本推廣活動優惠只適用於持有本公司發行之PayKool Visa Platinum卡（「PayKool卡」）之客戶。 優惠推廣期 除特別註明外，優惠推廣期由2026年5月12日至2026年8月11日(包括首尾兩日) (「推廣期」)。 優惠詳情 迎新推廣：PayKool迎新消費獎賞 要求及資格： a) 推廣期內，全新客戶使用指定邀請碼「PPAKIV」申請PayKool信用卡，成功獲批後1個月內於 AKIV門店或AKIV網店 使用PayKool信用卡完成單一簽賬消費滿$500（「指定簽賬要求」），可獲 $400免找數簽賬額 。 b) 合資格客戶只可獲得PayKool迎新消費獎賞最多1次，即合共最高HK$400 PayKool卡免找數簽賬額。 c) AKIV 門店: • AKIV Sportswear Flagship Store: 佐敦彌敦道216-228號恆豐中心一樓11-12號鋪 • AKIV Grand Atelier: 佐敦彌敦道216-228號恆豐中心一樓2號鋪 AKIV網店：https://akiv.co/ 持卡人禮遇：指定商戶精彩禮遇 要求及資格： a) 推廣期內，PayKool 信用卡客戶於AKIV門店 或 AKIV網店 購買AKIV上身服飾產品或配件，以 PayKool 信用卡簽賬，可享全單88折。 • 於AKIV網店，購買上身服飾產品及配件，使用PayKool持卡人優惠碼消費並以 PayKool 信用卡簽賬，可享全單88折。 • 於AKIV門店，購買上身服飾產品及配件，以 PayKool 信用卡簽賬，可享全單88折。 b) AKIV 門店: • AKIV Sportswear Flagship Store: 佐敦彌敦道216-228號恆豐中心一樓11-12號鋪 • AKIV Grand Atelier: 佐敦彌敦道216-228號恆豐中心一樓2號鋪 c) AKIV網店：https://akiv.co/ d) 優惠由商戶提供，並受商戶條款及細則約束。 迎新消費獎賞領取方式 PayKool卡免找數簽賬額 免找數簽賬額將於合資格客戶完成指定簽賬要求後一個月內存入客戶的PayKool卡賬戶。 PayKool持卡人優惠碼 PayKool持卡人優惠碼領取及使用方式： 推廣期內，PayKool 信用卡客戶於AKIV網店，購買上身服飾產品及配件，使用PayKool持卡人優惠碼消費並以 PayKool 信用卡簽賬，可享全單88折。 i. 付款前請開啟 PayKool 手機應用程式 > 禮遇 > 我的禮遇，選取相關AKIV禮遇； ii. 按下「立即領取」按鈕； iii. 頁面會顯示PayKool持卡人優惠碼； iv. 於AKIV網店購買上身服飾產品及配件，付款前輸入PayKool持卡人優惠碼並以 PayKool 信用卡簽賬，可享全單88折。 持卡人禮遇條款及細則 優惠條款及細則包括(但不限於)： • 此優惠有效期至2026年8月11日，逾期無效。 • 此優惠只適用於AKIV門店 或 AKIV網店。 • 此優惠只適用購買上身服飾產品及配件(特定產品除外)。 • 必須於購物時以PayKool信用卡全數簽賬方可享此優惠。 • 不適用於購買禮券、現金券及其他指定產品； • 不可與其他優惠﹑折扣或優惠碼同時使用； • 如有任何爭議，AKIV將保留最終決定權。 一般條款及細則 全新客戶定義 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。 合資格簽賬 合資格簽賬只包括所有已入賬之本地及 / 或海外零售購物金額及 / 或網上消費零售購物金額，並不包括（但不限於）以下類別的消費或單據： a) 折扣透支金額、信用卡費用（包括年費、利息 / 財務費用、逾期費用、超逾信用額手續費、折扣透支手續費及其他費用）、賭場交易金額、任何金錢 / 電子貨幣轉賬（包括但不只限於個人對個人(P

## Refresh
`python extract_paykool_terms.py --split --skills-dir skills`