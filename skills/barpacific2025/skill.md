# Skill: 【PayKool x Bar Pacific】Happy Friday去返個 Happy Hour🍹🍤

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
- URL: https://www.paykool.hk/promotions/barpacific2025
- Slug: barpacific2025
- Promotion period: 2026年3月19日至2026年6月18日，包括首尾兩天（「推廣期」）
- Invite code: Not detected
- New customer definition: 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: Not detected
- Reward summary: 迎新獎賞」及「PayKool 客戶專屬獎賞」 推廣優惠之條款及細則（「本條款及細則」） 任何人士參與由 K Cash Limited（「本公司」）旗下 PayKool 信用卡提供之 PayKool Visa Platinum卡「 PayKool x
- Voucher validity: 有效期至2026年6月18日 (包括當天)， 逾期作廢
- Customer responsibility: Not detected

## Source Excerpt
條款及細則約束 立即下載 PayKool Visa Platinum卡「PayKool x Bar Pacific迎新獎賞」及「PayKool 客戶專屬獎賞」 推廣優惠之條款及細則（「本條款及細則」） 任何人士參與由 K Cash Limited（「本公司」）旗下 PayKool 信用卡提供之 PayKool Visa Platinum卡「 PayKool x Bar Pacific 迎新獎賞 」及「 PayKool 客戶專屬獎賞 」推廣優惠（「本推廣活動」），即被視為明白及同意 PayKool Visa Platinum卡（「PayKool卡」）的私隱政策、收集個人資料聲明及本推廣活動之所有條款及細則並受其約束。有關資料可於 PayKool 官方網站瀏覽。 本推廣活動推廣期為2026年3月19日至2026年6月18日，包括首尾兩天（「推廣期」）。 本推廣活動只適用於符合以下條件之客戶（「合資格客戶」）： i. 必須為香港居民身分證持有人；及 ii. 年齡必須年滿18歲或以上；及 iii. 於推廣期內，在 PayKool 卡申請介面指定位置輸入有效的 指定邀請碼 申請 PayKool 卡並成功獲得批核之全新客戶（「合資格全新客戶」）；或 iv. 於推廣期內持有有效PayKool卡之現有客戶(「合資格現有客戶」)。 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。 符合上述要求的合資格全新客戶會收到成功申請確認電郵。 指定邀請碼會張貼於Bar Pacific分店內的宣傳物品上。 「PayKool x Bar Pacific 迎新獎賞」活動詳情 ： 在推廣期內，全新客戶以指定邀請碼申請PayKool卡, 成功批核後，客戶可在PayKool手機應用程式內獲得兩張電子現金券(總值HK$300)： i. HK$250 電子現金券：於Bar Pacific作任何消費即可使用； ii. HK$50 電子現金券：於Bar Pacific作任何消費並以PayKool信用卡簽賬即可使用。 「PayKool x Bar Pacific 迎新獎賞」電子現金券的使用條款如下： • 兩張電子現金券有效期至2026年6月18日 (包括當天)， 逾期作廢。 • 兩張電子現金券可於同一消費同時使用。 • 每張電子現金券只可使用一次，並只適用於單一消費。 • 電子現金券不可兌換現金及其他產品，不設找續、退款或延期。 • 客戶須於付款前向Bar Pacific職員展示電子現金券，並由Bar Pacific職員確認兌換資格才可使用。 • 逾期或已失效的電子現金券將不獲補發。 「PayKool 客戶專屬獎賞」 (由 「Bar Pacific」 提供) : 在推廣期內，合資格現有客戶需在PayKool手機應用程式內登記此獎賞並領取一張電子優惠券，於Bar Pacific惠顧任何一杯酒精飲料後，以PayKool卡簽賬，可使用該電子優惠券兌換由Bar Pacific提供的免費指定小食一客(價值HK$38) 。電子優惠券於每次消費只可兌換一次； 「PayKool 客戶專屬獎賞」電子優惠券的使用條款如下： • 電子優惠券有效期至2026年6月18日 (包括當天)， 逾期作廢。 • 電子優惠券不可兌換現金及其他產品。 • 客戶須於付款前向Bar Pacific職員展示電子優惠券，並由Bar Pacific職員確認兌換資格才可使用。 • 逾期或已失效的電子優惠券將不獲補發。 • 指定小食由Bar Pacific提供，數量有限，送完即止。 推廣期內，合資格客戶符合以上要求可使用「PayKool x Bar Pacific 迎新獎賞」優惠（「此優惠」），合資格客戶只可獲此優惠最多一次。 推廣期內，合資格客戶符合以上要求可同時使用「PayKool x Bar Pacific 迎新獎賞」及「PayKool 客戶專屬獎賞」 (由 「Bar Pacific」 提供)。 合資格客戶必須確保所提供的登記資料全屬真實、正確、完整、沒有誤導及欺詐成份。 本公司保留給予客戶此優惠之權利，客戶於PayKool卡生效後，PayKool卡戶口須於發放此優惠前維持良好狀況，包括但不限於沒有逾期還款紀錄、未有逾額情況或任何違反信用卡持卡人合約條款的行為。否則，本公司保留對

## Refresh
`python extract_paykool_terms.py --split --skills-dir skills`