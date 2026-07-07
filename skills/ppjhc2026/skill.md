# Skill: 🎉【PayKool x 日本城】新客戶迎新及現有客戶消費獎賞

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
- URL: https://www.paykool.hk/promotions/ppjhc2026
- Slug: ppjhc2026
- Promotion period: 2026年4月9日至2026年12月31日，包括首尾兩天（「推廣期」）
- Invite code: Not detected
- New customer definition: 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: Not detected
- Reward summary: 迎新獎賞」推廣優惠（「本推廣活動」），即被視為明白及同意 PayKool Visa Platinum卡（「PayKool卡」）的私隱政策、收集個人資料聲明及本推廣活動之所有條款及細則並受其約束
- Voucher validity: 有效期：即日至2027年4月30日 • 此券只限使用一次
- Customer responsibility: Not detected

## Source Excerpt
條款及細則（「本條款及細則」） 任何人士參與由 K Cash Limited（「本公司」）旗下 PayKool 信用卡提供之 PayKool Visa Platinum卡「PayKool x 日本城 迎新獎賞」推廣優惠（「本推廣活動」），即被視為明白及同意 PayKool Visa Platinum卡（「PayKool卡」）的私隱政策、收集個人資料聲明及本推廣活動之所有條款及細則並受其約束。有關資料可於 PayKool 官方網站瀏覽。 本推廣活動推廣期為2026年4月9日至2026年12月31日，包括首尾兩天（「推廣期」）。 本推廣活動只適用於符合以下條件之客戶（「合資格客戶」）： i. 必須為香港居民身分證持有人；及 ii. 年齡必須年滿18歲或以上；及 iii. 於推廣期內，在 PayKool 卡申請介面指定位置輸入有效的指定邀請碼申請 PayKool 卡並成功獲得批核之全新客戶。（「合資格全新客戶」）；或 iv. 於推廣期內持有有效PayKool卡之現有客戶(「合資格現有客戶」)。 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。 符合上述要求的合資格客戶會收到成功申請確認電郵。 「PayKool x 日本城 迎新獎賞」活動詳情： 全新客戶在推廣期內以指定邀請碼申請 PayKool 卡並成功獲批後，可獲得以下獎賞： 日本城HK$300電子現金券：合資格全新客戶可在PayKool手機應用程式內的「禮遇」活動頁面，獲得日本城 HK$100電子現金券3張，於香港日本城、生活提案及生活工房門市或日本城網購JHCeshop消費時使用。此外，客戶亦可選擇於香港日本城門市即場以電子現金券兌換成指定禮品。指定禮品詳情請向門市職員查詢，禮品數量有限及視乎供應而定，換完即止。 日本城電子現金券使用條款包括： • 電子現金券有效期：即日至2027年4月30日 • 此券只限使用一次。 • 此券不能兌換現金及不設找贖。 • 此優惠不適用於購買禮券、現金券、美食券。 • 如有任何爭議，日本城(香港)有限公司保留此使用優惠之最終決定權。 「PayKool 客戶專屬獎賞」 (由 「日本城」 提供): 合資格現有客戶可在PayKool手機應用程式內的「禮遇」活動頁面，獲得「日本城 HK$10折扣電子優惠券」。客戶以PayKool信用卡於香港日本城、生活提案及生活工房門市或日本城網購JHCeshop簽賬滿HK$218或以上，即可使用「HK$10折扣電子優惠券」，即減HK$10。 (有效期內使用次數不設上限) 「日本城 HK$10折扣電子優惠券」使用條款包括： • 電子優惠券有效期：即日至2026年12月31日 • 此券不能兌換現金及不設找贖。 • 此優惠不可與其他優惠(包括但不限於全場大型推廣、其他優惠券及優惠碼)同時使用。 • 此優惠不適用於購買禮券、現金券、美食券、食品、飲品、藥品、保健品、清貨勁減商品、指定品牌3C數碼產品、易購點內之大型電器、膠袋徵費及運輸費用。 • 如有任何爭議，日本城(香港)有限公司保留此使用優惠之最終決定權。 推廣期內，合資格客戶符合以上要求可使用「PayKool x 日本城 迎新獎賞」優惠（「此優惠」），合資格客戶只可獲此優惠乙次。 合資格客戶必須確保所提供的登記資料全屬真實、正確、完整、沒有誤導及欺詐成份。 本公司保留給予客戶此優惠之權利，客戶於PayKool卡生效後，PayKool卡戶口須於發放此優惠前維持良好狀況，包括但不限於沒有逾期還款紀錄、未有逾額情況或任何違反信用卡持卡人合約條款的行為。否則，本公司保留對客戶撤回此優惠之獲得權利而毋須事先通知。 此優惠不可退回、轉讓/轉售、兌換現金或換取其他優惠。如有遺失、失效或逾期，恕不獲補發。若合資格客戶於得到此優惠後一年內取消該PayKool卡，將會被收取該PayKool卡首年年費 HK$1,800。 本公司並非本活動之指定禮品製造/供應商，亦非該製造/供應商的代理。所有指定禮品之使用須受個別製造/供應商所訂定之所有條款及條件規限。本公司不會對指定禮品之質素、供應及與使用指定禮品有關事宜之任何後果負責。本公司毋須就指定禮品的任何問題（包括但不限於其品質、供應及使用有關事宜）負上任何責任。對任何因使用或不當使用該指定禮品而直接或間接引

## Refresh
`python extract_paykool_terms.py --split --skills-dir skills`