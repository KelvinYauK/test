# Skill: 🐱【PayKool x OneDegree】信用卡持卡人專屬投保優惠🐶

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
- URL: https://www.paykool.hk/promotions/onedegree2026
- Slug: onedegree2026
- Promotion period: Not detected
- Invite code: ONEDEGREE
- New customer definition: 全新客戶定義 全新客戶定義為申請日起計過去 12 個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: 指定簽賬要求」），成功投保可享以下對應獎賞： 寵物保險：首年保費 8 折及 $800 免找數簽賬額^；或 家居保險：首年保費 7 折及 $800 免找數簽賬額^；或 火險：
- Reward summary: 迎新獎賞」推廣優惠之條款及細則 PayKool信用卡「PayKool x Apple Pay加卡賞」推廣活動條款及細則（「本條款及細則」) PayKool Visa Platinum卡「PayKool x Bar Pacific迎新獎賞」及「Pay
- Voucher validity: Not detected
- Customer responsibility: 客戶責任 客戶須於付款前聲明享用有關優惠，並以 PayKool 卡全數簽賬方可享優惠。 如有任何爭議，客戶必須提供有關文件之正本、交易單據及信用卡簽賬存根正本（如適用），以便本公司作進一步調查。 有關獎賞不可退回、轉讓／轉售、兌換現金或換取其他優惠。如有遺失、失效或逾期，恕不獲補發。 若合資格客戶於得到有關獎賞後一年內取消 PayKool 卡，將會被收取 PayKool 卡年費 HK$1,800。 本公司保留給予客戶此優惠之權利，客戶於 PayKool 卡生效後，PayKool 卡戶口須於發放此優惠前維持良好狀況，包括但不限於沒有逾期還款紀錄、未有逾額情況或任何違反信用卡持卡人合約條款的行為。否則，本公司保留對客戶撤回此優惠之獲得權利而毋須事先通知。

## Source Excerpt
條款及細則約束，上述保險產品由持牌保險公司提供，PayKool僅提供優惠資訊並不構成對服務推薦 立即申請PayKool信用卡 PayKool Visa Platinum卡「PayKool x OneDegree」優惠-- PayKool信用卡迎新推廣及持卡人禮遇 (「本推廣活動」)之條款及細則 任何人士參與 K Cash Limited（「本公司」）旗下 PayKool 信用卡品牌與 OneDegree Hong Kong Limited（「商戶」、「OneDegree」）聯合推出的本推廣活動，即表示已充分了解並同意受本條款及細則的約束。 本推廣活動只適用於持有本公司發行之 PayKool Visa Platinum 卡（「PayKool卡」）之客戶。 優惠推廣期 除特別註明外，優惠推廣期由 2026 年 1 月 14 日至 2026 年 9 月 30 日（包括首尾兩日）（「推廣期」）。 優惠詳情 迎新推廣：PayKool 迎新消費獎賞 簽賬要求及資格： a. 推廣期內，全新客戶在 PayKool 卡申請介面指定位置輸入指定邀請碼「ONEDEGREE」申請 PayKool 卡，成功獲得批核後，會收到由本公司發出的確認電郵，客戶於推廣期內透過確認電郵／PayKool App 的指定禮遇頁面內之指定連結**連接至 OneDegree 之投保網站，並使用 PayKool 卡完成合資格簽賬投保 OneDegree（「指定簽賬要求」），成功投保可享以下對應獎賞： 寵物保險：首年保費 8 折及 $800 免找數簽賬額^；或 家居保險：首年保費 7 折及 $800 免找數簽賬額^；或 火險：投保可享 $800 免找數簽賬額^ ^ 每位合資格全新客戶於本推廣活動可享之免找數簽賬額上限為 $800 ** 客戶點擊指定連結將進入 OneDegree 網站及受其使用條款及私隱政策限制。在購買前，請客戶確保已明白 OneDegree 保險產品詳情及條款。 b. 投保申請之提交時間及狀況（成功提交與否）將以 OneDegree 之記錄為準。 c. OneDegree 保留最終決定是否接受任何保險申請的權利。由於可保性的考慮而導致保險申請被拒絕，可能導致無法享受保費折扣及／或免找數簽賬額優惠。假如保險申請被拒絕，申請人只能取回實際已繳付的保費金額及保費徵費（如有）。 d. 保費折扣優惠由 OneDegree 提供，OneDegree 就提供保費折扣之所有事宜及爭議均有最終決定權。 e. 投保 OneDegree 受其條款及細則約束，詳情請參閱 OneDegree 之官方網頁。 持卡人禮遇：PayKool 客戶指定商戶消費獎賞 簽賬要求及資格： a. PayKool 卡持卡人需於推廣期內透過 PayKool App 的指定禮遇頁面內的指定連結**連接至 OneDegree 之投保網站，並使用 PayKool 卡完成合資格簽賬投保 OneDegree（「指定簽賬要求」），成功投保可享以下對應獎賞： 寵物保險：首年保費 8 折及 $300 免找數簽賬額#；或 家居保險：首年保費 7 折及 $300 免找數簽賬額#；或 火險：投保可享 $300 免找數簽賬額# # 每位合資格持卡人（合資格全新客戶除外）於本推廣活動可享之免找數簽賬額上限為 $300 ** 客戶點擊指定連結將進入 OneDegree 網站及受其使用條款及私隱政策限制。在購買前，請客戶確保已明白 OneDegree 保險產品詳情及條款。 b. 投保申請之提交時間及狀況（成功提交與否）將以 OneDegree 之記錄為準。 c. OneDegree 保留最終決定是否接受任何保險申請的權利。由於可保性的考慮而導致保險申請被拒絕，可能導致無法享受保費折扣及／或免找數簽賬額優惠。假如保險申請被拒絕，申請人只能取回實際已繳付的保費金額及保費徵費（如有）。 d. 保費折扣優惠由 OneDegree 提供，OneDegree 就提供保費折扣之所有事宜及爭議均有最終決定權。 e. 投保 OneDegree 受其條款及細則約束，詳情請參閱 OneDegree 之官方網頁。 獎賞領取方式 PayKool 卡免找數簽賬額 迎新消費獎賞之免找數簽賬額將於 PayKool 卡獲批後三個月內存入客戶的 PayKool 卡賬戶。 Pay

## Refresh
`python extract_paykool_terms.py --split --skills-dir skills`