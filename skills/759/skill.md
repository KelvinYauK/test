# Skill: 【🎉 759 阿信屋掃貨必備，PayKool 至抵拍檔 🤜🏻🤛🏻！】

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
- URL: https://www.paykool.hk/promotions/759
- Slug: 759
- Promotion period: 2026年4月1日至2027年3月31日，包括首尾兩天（「推廣期」）
- Invite code: Not detected
- New customer definition: 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: Not detected
- Reward summary: 迎新獎賞」及「759阿信屋x PayKool持卡人專屬優惠」推廣優惠之條款及細則（「本條款及細則」） 任何人士參與由 K Cash Limited（「本公司」）旗下 PayKool 信用卡提供之 PayKool Visa Platinum卡「759
- Voucher validity: 有效期內使用，逾期無效
- Customer responsibility: Not detected

## Source Excerpt
條款及細則約束 ^「PayKool x Apple Pay加卡賞」推廣活動條款及細則: https://r.paykool.hk/jvxvnukL 立即申請 PayKool Visa Platinum卡「759阿信屋 x PayKool迎新獎賞」及「759阿信屋x PayKool持卡人專屬優惠」推廣優惠之條款及細則（「本條款及細則」） 任何人士參與由 K Cash Limited（「本公司」）旗下 PayKool 信用卡提供之 PayKool Visa Platinum卡「759阿信屋 x PayKool迎新獎賞」推廣優惠及「759阿信屋x PayKool持卡人專屬優惠」（「本推廣活動」），即被視為明白及同意 PayKool Visa Platinum卡（「PayKool卡」）的私隱政策、收集個人資料聲明及本推廣活動之所有條款及細則並受其約束。有關資料可於 PayKool 官方網站瀏覽。 本推廣活動推廣期為2026年4月1日至2027年3月31日，包括首尾兩天（「推廣期」）。 本推廣活動只適用於符合以下條件之客戶（「合資格客戶」）： i. 必須為香港居民身分證持有人；及 ii. 年齡必須年滿18歲或以上；及 iii. 於推廣期內，在 PayKool 卡申請介面指定位置輸入有效的指定邀請碼申請 PayKool 卡並成功獲得批核之全新客戶。（「合資格全新客戶」）；或 iv. 於推廣期內持有有效PayKool卡之特選客戶(「特選客戶」)。 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。 符合上述要求的合資格全新客戶會收到成功申請確認電郵。 「759阿信屋 x PayKool迎新獎賞」活動詳情： 全新客戶在推廣期內以指定邀請碼申請 PayKool 卡並成功獲批後，可獲得以下獎賞： 1 ) PayKool卡$50免找數簽賬額（免找數簽賬額將於PayKool信用卡獲批後一個月內存入客戶的PayKool信用卡賬戶），及； 2 ) 759阿信屋HK$300電子現金券：合資格全新客戶可在PayKool手機應用程式內的「禮遇」活動頁面，獲得759阿信屋 HK$50電子現金券6張，於香港全線759阿信屋門市消費時使用。 759阿信屋電子現金券使用條款包括： •電子現金券只可以於PayKool手機應用程式內列明之有效期內使用，逾期無效。 •每張現金券只限使用一次。 •此券不能兌換現金及不設找贖。 •不適用於購買優惠券、購買及／或充值儲值卡或電子錢包的簽賬交易、八達通自動增值、自動售賣機貨品及塑膠購物袋收費。 •使用電子現金券購買的貨品不設退款、退貨及更換貨品。 •如有任何爭議，PayKool及759阿信屋保留本迎新獎賞之最終決定權。 •電子現金券受759阿信屋之條款及細則約束。 「759阿信屋x PayKool持卡人專屬優惠」活動詳情: 推廣期內，特選客戶可於PayKool手機應用程式內「禮遇」頁面領取759阿信屋HK$10電子優惠券，於香港全線759阿信屋門市以PayKool信用卡流動支付簽賬滿HK$30或以上（折實後）即可使此電子優惠券。 「759阿信屋 HK$10電子優惠券」使用條款包括： •電子優惠券只可以於PayKool手機應用程式內列明之有效期內使用，逾期無效。 •每次交易只限使用一張電子優惠券。 •每張電子優惠券只限使用一次。 •此券不能兌換現金及不設找贖。 •特選客戶須於付款前出示本優惠的有效電子優惠券，並以PayKool信用卡透過流動支付完成付款方可享用本優惠。「流動支付」包括 Apple Pay、Google Pay、Alipay及微信支付。 •不適用於購買優惠券、購買及／或充值儲值卡或電子錢包的簽賬交易、八達通自動增值、自動售賣機貨品及塑膠購物袋收費。 •使用電子優惠券購買的貨品不設退款、退貨及更換貨品。 •如有任何爭議，PayKool及759阿信屋保留本優惠之最終決定權。 •電子優惠券受759阿信屋之條款及細則約束。 推廣期內，合資格全新客戶符合以上要求可獲得「759阿信屋 x PayKool迎新獎賞」優惠（「此優惠」），合資格全新客戶只可獲此優惠乙次。 合資格客戶必須確保所提供的登記資料全屬真實、正確、完整、沒有誤導及欺詐成份。 本公司保留給予客戶此優惠之權利，客戶於PayKool

## Refresh
`python extract_paykool_terms.py --split --skills-dir skills`