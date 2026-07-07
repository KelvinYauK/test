# Skill: ✈️ PayKool × SIM SQ 信用卡迎新及持卡人專屬優惠 🎉

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
- URL: https://www.paykool.hk/promotions/mbsim
- Slug: mbsim
- Promotion period: 2026年3月2日至2027年3月1日(包括首尾兩日) (「推廣期」)
- Invite code: MBSIM
- New customer definition: 全新客戶定義 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: 指定簽賬要求」)，可享以下迎新消費獎賞： PayKool卡$288免找數簽賬額，及； 完成指定簽賬要求後一個月內可於PayKool手機應用程式內的「禮遇」活動頁面，使用電子
- Reward summary: 迎新獎賞指定禮品 迎新獎賞指定禮品換領方式： a. 客戶須於完成指定簽賬要求後一個月內，於SIM SQ官方網站，使用PayKool 手機應用程式內有效的電子優惠碼，換領流程如下： i. 開啟 PayKool 手機應用程式 > 禮遇 > 我的禮遇，選
- Voucher validity: 有效期至2027年3月1日； b. 由World Sim Asia Telecom Limited 提供； c. 使用受制於World Sim Asia Teleco
- Customer responsibility: 客戶責任 客戶須於付款前聲明享用有關優惠，並以PayKool卡全數簽賬方可享優惠。 如有任何爭議，客戶必須提供有關之文件之正本、交易單據及信用卡簽賬存根正本(如適用)以便本公司作進一步調查。 有關獎賞不可退回、轉讓/轉售、兌換現金或換取其他優惠。如有遺失、失效或逾期，恕不獲補發。 若合資格客戶於得到有關獎賞後一年內取消PayKool卡，將會被收取PayKool卡年費 HK$1,800。 本公司保留給予客戶此優惠之權利，客戶於PayKool卡生效後，PayKool卡戶口須於發放此優惠前維持良好狀況，包括但不限於沒有逾期還款紀錄、未有逾額情況或任何違反信用卡持卡人合約條款的行為。否則，本公司保留對客戶撤回此優惠之獲得權利而毋須事先通知。

## Source Excerpt
條款及細則 任何人士參與 K Cash Limited（「本公司」）旗下 PayKool 信用卡品牌與 World Sim Asia Telecom Limited（「商戶」）聯合推出的本推廣活動，即表示已充分了解並同意受本條款及細則的約束。 本推廣活動只適用於持有本公司發行之PayKool Visa Platinum卡（「PayKool卡」）之客戶。 優惠推廣期 除特別註明外，優惠推廣期由2026年3月2日至2027年3月1日(包括首尾兩日) (「推廣期」)。 優惠詳情 迎新推廣：「PayKool迎新消費獎賞」 簽賬要求及資格： a. 推廣期內，全新客戶在PayKool卡申請介面指定位置輸入指定邀請碼「MBSIM」申請PayKool卡，成功獲得批核後，會收到由本公司發出的確認電郵，客戶需於一個月內使用PayKool卡完成單一合資格簽賬滿HK$1 (「指定簽賬要求」)，可享以下迎新消費獎賞： PayKool卡$288免找數簽賬額，及； 完成指定簽賬要求後一個月內可於PayKool手機應用程式內的「禮遇」活動頁面，使用電子優惠碼，於World Sim Asia Telecom Limited 旗下官方網站simsq.hk (「SIM SQ官方網站」)換領由商戶提供的【閃卡】亞洲10地 8 日上網數據卡1張(「指定禮品」)。 b. 推廣期內，合資格客戶只可領取PayKool迎新消費獎賞最多1次。 c. 使用指定禮品受其條款及細則約束。 指定禮品條款及細則 【閃卡】亞洲10地 8 日上網數據卡使用條款包括(但不限於)： a. 有效期至2027年3月1日； b. 由World Sim Asia Telecom Limited 提供； c. 使用受制於World Sim Asia Telecom Limited 的條款及細則，如有任何爭議，World Sim Asia Telecom Limited 保留最終決定權。 「PayKool 客戶專屬獎賞」(由「World Sim Asia Telecom Limited」提供): 推廣期內，合資格現有客戶可在PayKool手機應用程式內的「禮遇」活動頁面登記，可獲得「 SIM SQ $20電子優惠券」。 推廣期內，客戶以PayKool卡於 SIM SQ官方網站 簽賬滿HK$50或以上，可使用「 SIM SQ $20電子優惠券」，即減HK20 (「本優惠」) 。 「 SIM SQ $20電子優惠券」條款及細則: SIM SQ $20電子優惠券使用條款包括(但不限於)： a. 有效期至2027年3月1日 b. 只適用於 SIM SQ官方網站； c. 於推廣期內使用次數不設上限； d. 本優惠每次消費限使用一張； e. 不適用於購買禮券及現金券； f. 如有任何爭議，World Sim Asia Telecom Limited保留最終決定權。 獎賞領取方式 PayKool卡免找數簽賬額 免找數簽賬額將於完成指定簽賬要求後一個月內存入客戶的PayKool信用卡賬戶。 迎新獎賞指定禮品 迎新獎賞指定禮品換領方式： a. 客戶須於完成指定簽賬要求後一個月內，於SIM SQ官方網站，使用PayKool 手機應用程式內有效的電子優惠碼，換領流程如下： i. 開啟 PayKool 手機應用程式 > 禮遇 > 我的禮遇，選取相關電子優惠碼； ii. 按下「立即領取」按鈕； iii. 於SIM SQ官方網站輸入指定優惠碼換領指定禮品。 商戶電子優惠券 領取及使用方式： a. 客戶須於商戶付款前出示PayKool 手機應用程式內有效的商戶電子現金券，使用流程如下： i. 付款前請前往 PayKool 手機應用程式 > 禮遇 > 我的禮遇，選取相關電子現金券； ii. 按下「立即領取」按鈕； iii. 頁面會顯示電子現金券的QR code (如適用)/ 優惠碼(如適用)； iv. 向商戶職員出示或於自助付款機展示(如適用)電子現金券的QR code或於網店輸入電子現金券上的優惠碼(如適用)。 一般條款及細則 全新客戶定義 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。 合資格簽賬 合資格簽賬只包括所有已入賬之本地及 / 或海外零售購物金額及 / 或網上消費零售購物金額，並不

## Refresh
`python extract_paykool_terms.py --split --skills-dir skills`