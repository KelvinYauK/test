# Skill: 【PayKool x Carder Toysnplace】訓練家集結！限時尊享寶可夢卡牌優惠 🃏⚡

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
- URL: https://www.paykool.hk/promotions/cardertoysnplace
- Slug: cardertoysnplace
- Promotion period: 2026年4月30日至2027年4月29日(包括首尾兩日) (「推廣期」)
- Invite code: MBCARDER
- New customer definition: 全新客戶定義 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: Not detected
- Reward summary: 迎新獎賞指定禮品 迎新獎賞指定禮品換購方式： a. 客戶須於成功批核後一個月內，憑PayKool手機應用程式內的「HK$1 Carder Toysnplace 指定卡盒換購券」，於商戶指定門店以PayKool卡支付HK$1換購指定禮品
- Voucher validity: 有效期為發出日起計1個月內 (以PayKool App內顯示之日期為準)； b. 可供換購的指定禮品由 Carder Toysnplace 提供，款式由商戶決定，有關
- Customer responsibility: 客戶責任 客戶須於付款前聲明享用有關優惠，並以PayKool卡全數簽賬方可享優惠。 如有任何爭議，客戶必須提供有關之文件之正本、交易單據及信用卡簽賬存根正本(如適用)以便本公司作進一步調查。 有關獎賞不可退回、轉讓/轉售、兌換現金或換取其他優惠。如有遺失、失效或逾期，恕不獲補發。 若合資格客戶於得到有關獎賞後一年內取消PayKool卡，將會被收取PayKool卡年費 HK$1,800。 本公司保留給予客戶此優惠之權利，客戶於PayKool卡生效後，PayKool卡戶口須於發放此優惠前維持良好狀況，包括但不限於沒有逾期還款紀錄、未有逾額情況或任何違反信用卡持卡人合約條款的行為。否則，本公司保留對客戶撤回此優惠之獲得權利而毋須事先通知。

## Source Excerpt
條款及細則約束。 立即申請 PayKool 信用卡 [PayKool x Carder Toysnplace] 優惠– PayKool信用卡迎新推廣及持卡人消費獎賞及禮遇 (「本推廣活動」)之條款及細則 任何人士參與 K Cash Limited（「本公司」）旗下 PayKool 信用卡品牌與 Carder Toysnplace（「商戶」）聯合推出的本推廣活動，即表示已充分了解並同意受本條款及細則的約束。 本推廣活動只適用於持有本公司發行之PayKool Visa Platinum卡（「PayKool卡」）之客戶。 優惠推廣期 除特別註明外，優惠推廣期由2026年4月30日至2027年4月29日(包括首尾兩日) (「推廣期」)。 優惠詳情 迎新推廣：「PayKool迎新消費獎賞」 簽賬要求及資格： a. 推廣期內，全新客戶在PayKool卡申請介面指定位置輸入指定邀請碼「MBCARDER」申請PayKool卡，成功獲得批核後，會收到由本公司發出的確認電郵，同時客戶的PayKool手機應用程式內的「禮遇」活動頁面將自動獲發「HK$1 Carder Toysnplace 指定卡盒換購券」(「商戶電子換購券」)1張。客戶可於一個月內憑此商戶電子換購券，於商戶指定門店以PayKool卡支付HK$1換購由商戶提供的繁體中文版寶可夢集換式卡牌遊戲擴充包1 盒(「指定禮品」)。此HK$1換購費用必須以PayKool卡支付，包括但不限於透過Apple Pay、Google Pay或AlipayHK綁定PayKool卡支付。 b. 推廣期內，合資格客戶只可領取PayKool迎新消費獎賞最多1次。 c. 指定禮品由商戶提供，數量有限，換完即止。 d. 使用商戶電子換購券受其條款及細則約束。 商戶電子換購券條款及細則 商戶電子換購券Carder Toysnplace使用條款包括(但不限於)： a. 有效期為發出日起計1個月內 (以PayKool App內顯示之日期為準)； b. 可供換購的指定禮品由 Carder Toysnplace 提供，款式由商戶決定，有關指定禮品詳情請向商戶查詢； c. 可供換購的指定禮品數量有限，換完即止； d. 使用受制於 Carder Toysnplace 的條款及細則，如有任何爭議，Carder Toysnplace 保留最終決定權。 持卡人禮遇：「PayKool 客戶專屬獎賞」(由「Carder Toysnplace」提供): 推廣期內，合資格現有客戶可在PayKool手機應用程式內的「禮遇」活動頁面登記，可獲得「Carder Toysnplace HK$50 優惠券」(「商戶電子優惠券」)。 推廣期內，合資格現有客戶以PayKool卡於商戶指定門店簽賬滿HK$1,000或以上，可使用商戶電子優惠券Carder Toysnplace，即減HK$50 (「本優惠」) 。 商戶電子優惠券Carder Toysnplace條款及細則: 「Carder Toysnplace HK$50 優惠券」使用條款包括(但不限於)： a. 有效期至2027年4月23日 b. 只適用於商戶指定門店； c. 於推廣期內使用次數不設上限； d. 本優惠每次消費限使用一張； e. 不適用於購買禮券及現金券； f. 如有任何爭議，Carder Toysnplace保留最終決定權。 優惠領取方式 迎新獎賞指定禮品 迎新獎賞指定禮品換購方式： a. 客戶須於成功批核後一個月內，憑PayKool手機應用程式內的「HK$1 Carder Toysnplace 指定卡盒換購券」，於商戶指定門店以PayKool卡支付HK$1換購指定禮品。換購流程如下： I. 開啟 PayKool 手機應用程式 > 禮遇 > 我的禮遇，選取相關電子優惠碼； II. 按下「立即領取」按鈕； III. 於商戶指定門店出示商戶電子換購券，並以PayKool卡支付HK$1換購指定禮品。 商戶電子優惠券 領取及使用方式： a. 客戶須於商戶付款前出示PayKool 手機應用程式內有效的商戶電子優惠券，使用流程如下： i. 付款前請前往 PayKool 手機應用程式 > 禮遇 > 我的禮遇，選取相關電子優惠券； ii. 按下「立即領取」按鈕； iii. 頁面會顯示電子優惠券的QR code (

## Refresh
`python extract_paykool_terms.py --split --skills-dir skills`