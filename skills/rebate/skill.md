# Skill: 10%簽賬回贈迎新優惠｜🎉新客戶最高回贈HK$500

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
- URL: https://www.paykool.hk/promotions/rebate
- Slug: rebate
- Promotion period: 2026年6月1日起至2026年6月14日，包括首尾兩天（「推廣期」）
- Invite code: Not detected
- New customer definition: 全新客戶定義為於申請日前12個月內未曾於本公司申請（不論成功與否）或持有任何信用卡賬戶。
- Spend requirement: Not detected
- Reward summary: 迎新獎賞」推廣優惠之條款及細則 PayKool信用卡「PayKool x Apple Pay加卡賞」推廣活動條款及細則（「本條款及細則」) PayKool Visa Platinum卡「PayKool x Bar Pacific迎新獎賞」及「Pay
- Voucher validity: Not detected
- Customer responsibility: Not detected

## Source Excerpt
條款及細則約束。 立即申請 PayKool Visa Platinum卡「10%簽賬回贈迎新優惠」推廣優惠之條款及細則（「本條款及細則」） 任何人士參與由 K Cash Limited（「本公司」）旗下 PayKool 信用卡提供之 PayKool Visa Platinum 卡「10%簽賬回贈迎新優惠」（「本推廣活動」），即表示已閱讀、明白及同意 PayKool Visa Platinum 卡（「PayKool卡」）的私隱政策、收集個人資料聲明及本推廣活動之所有條款及細則並受其約束，有關資料可於 PayKool 官方網頁查閱。 本推廣活動推廣期由 2026年6月1日起至2026年6月14日，包括首尾兩天（「推廣期」）。 本推廣活動只適用於符合以下所有條件之客戶（「合資格客戶」）： i. 持有香港居民身分證；及 ii. 年滿 18 歲或以上；及 iii. 於推廣期內輸入優惠碼「REBATE」申請 PayKool 卡並成功獲批核，且未曾獲得本公司任何其他迎新優惠之全新客戶。 全新客戶定義為於申請日前12個月內未曾於本公司申請（不論成功與否）或持有任何信用卡賬戶。 合資格客戶於信用卡批核日起計 30個曆日內，以 PayKool 卡作出之合資格消費可享 10% 簽賬回贈（「本優惠」），每位合資格客戶於本推廣活動最高可獲 HK$500 簽賬回贈（「回贈上限」）。例子：若合資格客戶之 PayKool 卡於2026年6月1日成功批核，該客戶於2026年6月30日或之前以 PayKool 卡作出之合資格消費可享10%簽賬回贈。假設該客戶於此期間以PayKool 卡作出之合資格消費總額為 HK$8,000，按10%計算可獲回贈 HK$800，惟因回贈上限為 HK$500，故該客戶最終可獲之簽賬回贈為 HK$500。 合資格消費包括成功入賬的本地、海外零售交易和網上購物消費，但不包括以下類別： i. 現金透支、信用卡費用（包括但不限於年費、利息、逾期費用、超額費用）； ii. 退款或取消的交易、未經授權的交易及其他本公司不時指定為不合資格的交易類別。 本公司可全權酌情決定有關簽賬是否屬於合資格消費。本公司對有關簽賬是否屬於合資格消費的決定為最終及決定性的。 簽賬回贈將於合資格客戶完成上述條件簽賬後1個月內存入該客戶的 PayKool 卡賬戶。 客戶必須保留任何簽賬的簽賬存根正本、其他證明文件或證據。如有爭議，本公司保留權利要求客戶提供有關的文件或證據以作核實。已遞交的文件及/或證據將不獲發還。如本公司的紀錄與客戶的紀錄不符，概以本公司的紀錄為準。 此優惠不可退回、轉讓/轉售、兌換現金或換取其他優惠。如有遺失、失效或逾期，恕不獲補發。若合資格客戶於得到此優惠後 12 個月內取消該信用卡，將會被收取該信用卡首年年費或有關此優惠的價值費用，以較高者為準。 合資格客戶必須確保所提供的登記資料全屬真實、正確、完整、沒有誤導及欺詐成份。 本公司保留給予客戶此優惠之權利，客戶於信用卡生效後，信用卡戶口須於發放此優惠前維持良好狀況，包括但不限於沒有逾期還款紀錄、未有逾額情況或任何違反信用卡持卡人合約條款的行為。否則，本公司保留對客戶撤回此優惠之獲得權利而毋須事先通知。 若本推廣活動因但不限於未經授權的干預、欺詐、技術故障的原因，而破壞或影響安全性、公平性、誠信及本推廣活動的正常運作，本公司有權取消有關合資格客戶的資格，而無須發出事先通知。 本公司有權隨時修訂、暫停或終止本推廣活動及/或獎賞及更改本條款及細則，而毋須另行通知。如有任何爭議，本公司對本推廣活動及/或獎賞之所有事宜均有最終決定權，並對所有相關人士具約束力。 有關收集、保留、處理或以任何方式處理個人資料有關的私隱事宜的責任及政策提供的資料，可瀏覽 PayKool 官方網頁內的私隱政策聲明。 本條款及細則是附加於本公司信用卡持卡人合約（「持卡人合約」）之一部份，倘若本條款及細則與持卡人合約有任何歧異，將以本條款及細則為準。 本推廣活動受制於本公司（具唯一及絕對酌情權）核實及確認為合資格，如有任何爭議，本公司將保留最終決定權。 並非本條款協議一方的人士無權按《合約(第三者權利)條例》(香港法例第 623 章)執行本條款的任何條文，或享有本條款的任何條文下的利益。 本推廣活動及其條款和細則受香港特別行政區法律的管轄

## Refresh
`python extract_paykool_terms.py --split --skills-dir skills`