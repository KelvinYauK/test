# Skill: 【PayKool x Mudan Noir母親節限定🌸】持卡人專屬優惠

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
- URL: https://www.paykool.hk/promotions/MudanNoir2026
- Slug: MudanNoir2026
- Promotion period: 2026年4月29日至2026年5月30日(包括首尾兩日) (「推廣期」)
- Invite code: Not detected
- New customer definition: Not detected
- Spend requirement: Not detected
- Reward summary: 迎新獎賞」推廣優惠之條款及細則 PayKool信用卡「PayKool x Apple Pay加卡賞」推廣活動條款及細則（「本條款及細則」) PayKool Visa Platinum卡「PayKool x Bar Pacific迎新獎賞」及「Pay
- Voucher validity: Not detected
- Customer responsibility: 客戶責任 客戶須於付款前聲明享用有關優惠。 如有任何爭議，客戶必須提供有關之文件之正本、交易單據及信用卡簽賬存根正本(如適用)以便本公司作進一步調查。 有關獎賞不可退回、轉讓/轉售、兌換現金或換取其他優惠。如有遺失、失效或逾期，恕不獲補發。 若合資格客戶於得到有關獎賞後一年內取消PayKool卡，將會被收取PayKool卡年費 HK$1,800。 本公司保留給予客戶此優惠之權利，客戶於PayKool卡生效後，PayKool卡戶口須於發放此優惠前維持良好狀況，包括但不限於沒有逾期還款紀錄、未有逾額情況或任何違反信用卡持卡人合約條款的行為。否則，本公司保留對客戶撤回此優惠之獲得權利而毋須事先通知。

## Source Excerpt
條款及細則約束 立即申請 [PayKool x Mudan Noir]優惠– PayKool信用卡持卡人禮遇(「本推廣活動」)之條款及細則 任何人士參與 K Cash Limited（「本公司」）旗下 PayKool 信用卡品牌與 Mudan Noir（「商戶」）聯合推出的本推廣活動，即表示已充分了解並同意受本條款及細則的約束。 本推廣活動只適用於持有本公司發行之PayKool Visa Platinum卡（「PayKool卡」）之客戶。 優惠推廣期 除特別註明外，優惠推廣期由2026年4月29日至2026年5月30日(包括首尾兩日) (「推廣期」)。 優惠詳情 持卡人禮遇：指定商戶精彩禮遇 要求及資格： a. 推廣期內，PayKool 現有信用卡客戶於Mudan Noir網店，使用 PayKool 持卡人優惠碼，並以PayKool信用卡簽賬，可享香薰陶瓷花產品即減HK$100優惠。 b. 優惠由Mudan Noir提供，數量有限，額滿即止。訂單滿HK$500可享免運費。 c. 優惠受商戶電子優惠券使用條款約束。 d. Mudan Noir網店: https://www.mudannoir.com/collections/all 商戶電子優惠券 PayKool持卡人優惠碼領取及使用方式： a. 推廣期內PayKool卡持卡人在PayKool手機應用程式內的「禮遇」活動頁面，可獲得一張「電子優惠券」， 領取相關電子優惠券後，會顯示PayKool持卡人優惠碼，使用流程如下： i. 於付款前請前往 PayKool 手機應用程式 > 禮遇，選取相關電子優惠券； ii. 按下「立即領取」按鈕； iii. 頁面會顯示PayKool持卡人優惠碼； iv. 於Mudan Noir網店付款前輸入PayKool持卡人優惠碼，並以PayKool信用卡簽賬，以享用優惠。 電子優惠券使用條款包括(但不限於)： 優惠由Mudan Noir提供，數量有限，額滿即止。訂單滿HK$500可享免運費。 優惠只適用於Mudan Noir網店； 不能兌換現金及不設找贖； 不適用於購買禮券、現金券及其他指定產品； 不可與其他優惠﹑折扣或優惠碼同時使用； 優惠受Mudan Noir網店條款及細則約束； 本公司及Mudan Noir保留隨時修改或終止本優惠的權利，恕不另行通知。 一般條款及細則 客戶責任 客戶須於付款前聲明享用有關優惠。 如有任何爭議，客戶必須提供有關之文件之正本、交易單據及信用卡簽賬存根正本(如適用)以便本公司作進一步調查。 有關獎賞不可退回、轉讓/轉售、兌換現金或換取其他優惠。如有遺失、失效或逾期，恕不獲補發。 若合資格客戶於得到有關獎賞後一年內取消PayKool卡，將會被收取PayKool卡年費 HK$1,800。 本公司保留給予客戶此優惠之權利，客戶於PayKool卡生效後，PayKool卡戶口須於發放此優惠前維持良好狀況，包括但不限於沒有逾期還款紀錄、未有逾額情況或任何違反信用卡持卡人合約條款的行為。否則，本公司保留對客戶撤回此優惠之獲得權利而毋須事先通知。 免責聲明 本推廣活動的獎賞須視乎供應情況而定，先到先得，換完即止。如有任何更改，將以惠顧時之優惠詳情為準。 除特別註明外，PayKool卡之客戶只可於接受該卡簽賬之商戶享本推廣活動，詳情請向商戶查詢。 圖片、產品資料及價錢只供參考。 客戶明白及接納所有商戶提供的產品及/或服務並非由本公司所提供。因此，有關商戶、其員工、其人員及其供應商於推廣活動提供的各項產品/服務的各方面，包括但不只限於商戶所提供的產品及/或其服務的質素、供應量、產品及/或其服務說明、任何虛假的交易說明、虛假陳述、錯誤聲明、遺漏、未經授權的陳述、與本推廣活動相關或就提供本推廣活動下的產品及/或服務的不公平貿易慣例或行為，本公司均毋須負上任何責任。 本推廣活動商戶附有額外條款及細則，詳情請向有關商戶查詢（如適用）。 商戶或許會收集客戶之個人資料，其個人資料之用途將受商戶之個人資料收集聲明約束，詳情請向有關商戶查詢。 保留權利 本公司保留隨時更改、延長或終止優惠，以及修訂條款及細則之權利，無須另行通知。如對有關本推廣活動的條款及細則有任何爭議，本公司將保留最終決定權。 如本公司認為客戶所提供的資料無效及 / 或於交易過程中涉及任何不被認

## Refresh
`python extract_paykool_terms.py --split --skills-dir skills`