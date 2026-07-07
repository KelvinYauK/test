# Skill: PayKool Promotion Terms Checker

## Goal
Use promotion terms from PayKool pages to validate whether a customer is eligible for each promotion reward.

## Data Source
- Listing page: https://www.paykool.hk/promotions
- Individual promotion pages under `/promotions/<slug>`

## Agent Input (Customer Profile)
- `customer_id`
- `is_new_customer` (boolean)
- `application_date`
- `invite_code_used`
- `card_approved_date`
- `transactions` (date, merchant, amount, channel)
- `account_status_good` (boolean)

## Agent Output
For each promotion: `eligible` or `not_eligible`, failed checks, and evidence fields.

## Core Validation Checklist
1. Check promotion period.
2. Check required invitation code (if any).
3. Check customer type requirement (new customer / existing customer).
4. Check spending requirement (amount, merchant, time window).
5. Check one-time limit / duplicate redemption.
6. Check account status (no overdue/invalid status).

## Extracted Promotion Rules

### 1. 限時快閃迎新優惠｜🎉PayKool信用卡送你100%簽賬回贈
- URL: https://www.paykool.hk/promotions/345
- Promotion period: 2026年3月27日起至2026年6月30日，包括首尾兩天（「推廣期」）
- Invite code: Not detected
- New customer definition: 全新客戶定義為申請日起計過去 12 個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: Not detected
- Reward summary: 迎新獎賞」推廣優惠之條款及細則 PayKool信用卡「PayKool x Apple Pay加卡賞」推廣活動條款及細則（「本條款及細則」) PayKool Visa Platinum卡「PayKool x Bar Pacific迎新獎賞」及「Pay
- Voucher validity: Not detected

### 2. 【🎉 759 阿信屋掃貨必備，PayKool 至抵拍檔 🤜🏻🤛🏻！】
- URL: https://www.paykool.hk/promotions/759
- Promotion period: 2026年4月1日至2027年3月31日，包括首尾兩天（「推廣期」）
- Invite code: Not detected
- New customer definition: 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: Not detected
- Reward summary: 迎新獎賞」及「759阿信屋x PayKool持卡人專屬優惠」推廣優惠之條款及細則（「本條款及細則」） 任何人士參與由 K Cash Limited（「本公司」）旗下 PayKool 信用卡提供之 PayKool Visa Platinum卡「759
- Voucher validity: 有效期內使用，逾期無效

### 3. 🛍️ 「PayKool x GIORMANI」全新客戶專屬優惠 🎉
- URL: https://www.paykool.hk/promotions/Giormani
- Promotion period: 2026年4月1日至2026年5月3日(包括首尾兩日) (「推廣期」)
- Invite code: M2PCCGIORMANI
- New customer definition: 全新客戶定義 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: 指定簽賬要求」)，可獲得HK$500 PayKool卡免找數簽賬額
- Reward summary: Not detected
- Voucher validity: Not detected

### 4. 【PayKool x Mudan Noir母親節限定🌸】持卡人專屬優惠
- URL: https://www.paykool.hk/promotions/MudanNoir2026
- Promotion period: 2026年4月29日至2026年5月30日(包括首尾兩日) (「推廣期」)
- Invite code: Not detected
- New customer definition: Not detected
- Spend requirement: Not detected
- Reward summary: Not detected
- Voucher validity: Not detected

### 5. 【☕ PayKool 全新客戶專享 Starbucks電子現金禮券｜全新客戶迎新及簽賬獎賞 🎁】
- URL: https://www.paykool.hk/promotions/Starbucks2026
- Promotion period: 2026年7月6日至2026年12月31日(包括首尾兩日) (「推廣期」)
- Invite code: PPSB
- New customer definition: 全新客戶定義 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: 單一簽賬或增值滿 HK$100
- Reward summary: 可獲高達HK$500的Starbucks電子現金禮券
- Voucher validity: 有效日期至2027年7月31日

### 6. 【👟 PayKool x AKIV｜迎新消費獎賞及持卡人專屬禮遇 ✨】
- URL: https://www.paykool.hk/promotions/akiv
- Promotion period: 2026年5月12日至2026年8月11日(包括首尾兩日) (「推廣期」)
- Invite code: PPAKIV
- New customer definition: 全新客戶定義 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: 指定簽賬要求」），可獲 $400免找數簽賬額
- Reward summary: Not detected
- Voucher validity: 有效期至2026年8月11日，逾期無效

### 7. Apple Pay FAQ
- URL: https://www.paykool.hk/promotions/apple-pay
- Promotion period: Not detected
- Invite code: Not detected
- New customer definition: Not detected
- Spend requirement: Not detected
- Reward summary: 迎新獎賞」推廣優惠之條款及細則 PayKool信用卡「PayKool x Apple Pay加卡賞」推廣活動條款及細則（「本條款及細則」) PayKool Visa Platinum卡「PayKool x Bar Pacific迎新獎賞」及「Pay
- Voucher validity: Not detected

### 8. 【🎉 PayKool信用卡 - 果迷出機迎新優惠】💻
- URL: https://www.paykool.hk/promotions/apple26
- Promotion period: 2026年3月17日至2026年5月31日，包括首尾兩天 (「推廣期」)
- Invite code: APPLE26
- New customer definition: 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請(不論成功申請與否)或擁有任何信用卡賬戶。
- Spend requirement: Not detected
- Reward summary: 迎新獎賞」推廣優惠之條款及細則 PayKool信用卡「PayKool x Apple Pay加卡賞」推廣活動條款及細則（「本條款及細則」) PayKool Visa Platinum卡「PayKool x Bar Pacific迎新獎賞」及「Pay
- Voucher validity: Not detected

### 9. 🏠 PayKool x at.home｜迎新獎賞及持卡人專屬禮遇 ✨
- URL: https://www.paykool.hk/promotions/athome
- Promotion period: 2026年5月22日至2026年8月21日(包括首尾兩日) (「推廣期」)
- Invite code: PPHOME
- New customer definition: 全新客戶定義 9. 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: Not detected
- Reward summary: 迎新獎賞 4. 要求及資格： a) 推廣期內，全新客戶以指定邀請碼「PPHOME」申請PayKool 信用卡，成功批核後可獲得以下迎新獎賞： i. at.home HK$400 電子折扣券 : 全新客戶可在 PayKool 手機應用程式內的「禮遇」
- Voucher validity: 有效日期至2026年8月31日

### 10. 【PayKool x Aura Yoga │🧘‍♀️ $500迎新獎賞】
- URL: https://www.paykool.hk/promotions/aurayoga
- Promotion period: 2026年3月6日至2026年6月5日(包括首尾兩日) (「推廣期」)
- Invite code: Not detected
- New customer definition: 全新客戶定義 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: Not detected
- Reward summary: 迎新獎賞 要求及資格： a. 推廣期內，客戶於Aura Yoga分店購買指定課堂套票，將獲Aura Yoga職員提供指定邀請碼，客戶使用該指定邀請碼申請PayKool信用卡，成功申請之全新客戶可獲$500免找數簽賬額
- Voucher validity: Not detected

### 11. 【PayKool x Bar Pacific】Happy Friday去返個 Happy Hour🍹🍤
- URL: https://www.paykool.hk/promotions/barpacific2025
- Promotion period: 2026年3月19日至2026年6月18日，包括首尾兩天（「推廣期」）
- Invite code: Not detected
- New customer definition: 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: Not detected
- Reward summary: 迎新獎賞」及「PayKool 客戶專屬獎賞」 推廣優惠之條款及細則（「本條款及細則」） 任何人士參與由 K Cash Limited（「本公司」）旗下 PayKool 信用卡提供之 PayKool Visa Platinum卡「 PayKool x
- Voucher validity: 有效期至2026年6月18日 (包括當天)， 逾期作廢

### 12. 🐾 「PayKool x Big Paws Pet Salon and Academy」信用卡迎新及持卡人專屬優惠 🎉
- URL: https://www.paykool.hk/promotions/bigpaws
- Promotion period: 2026年3月25日至2026年6月24日(包括首尾兩日) (「推廣期」)
- Invite code: Not detected
- New customer definition: 全新客戶定義 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: Not detected
- Reward summary: 迎新獎賞 要求及資格： a. 推廣期內，客戶於Big Paws Pet Salon and Academy門店購買指定課程或美容套票，將獲店員提供指定邀請碼
- Voucher validity: Not detected

### 13. 🎓 PayKool x BrainStation 信用卡迎新及持卡人專屬優惠✨
- URL: https://www.paykool.hk/promotions/brainstation
- Promotion period: 2026年3月6日至2026年6月5日(包括首尾兩日) (「推廣期」)
- Invite code: Not detected
- New customer definition: 全新客戶定義 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: Not detected
- Reward summary: 迎新獎賞 簽賬要求及資格： a. 推廣期內，客戶於BrainStation旗下指定分店報讀指定課程，將獲BrainStation職員提供指定邀請碼，客戶使用該指定邀請碼申請PayKool卡，成功申請之全新客戶可獲$500免找數簽賬額
- Voucher validity: Not detected

### 14. Paykool復活節Truck Show驚喜快閃登場 挑戰贏高達 $10,000 簽賬回贈上限
- URL: https://www.paykool.hk/promotions/bread345
- Promotion period: Not detected
- Invite code: Not detected
- New customer definition: 全新客戶定義為申請日起計過去 12 個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: Not detected
- Reward summary: Not detected
- Voucher validity: Not detected

### 15. 【PayKool x Card Buddies 訓練家召集！🃏】信用卡迎新及持卡人專屬禮遇
- URL: https://www.paykool.hk/promotions/cardbuddies
- Promotion period: 2026年4月24日至2027年4月23日(包括首尾兩日) (「推廣期」)
- Invite code: MBCARDB
- New customer definition: 全新客戶定義 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: Not detected
- Reward summary: 迎新獎賞指定禮品 迎新獎賞指定禮品換購方式： a. 客戶須於成功批核後一個月內，憑PayKool手機應用程式內的「HK$1 Card Buddies 指定卡盒換購券」，於商戶指定門店以PayKool卡支付HK$1換購指定禮品
- Voucher validity: 有效期為發出日起計1個月內 (以PayKool App內顯示之日期為準)； b. 可供換購的指定禮品由 Card Buddies 提供，款式由商戶決定，有關指定禮品詳

### 16. 【PayKool x Carder Toysnplace】訓練家集結！限時尊享寶可夢卡牌優惠 🃏⚡
- URL: https://www.paykool.hk/promotions/cardertoysnplace
- Promotion period: 2026年4月30日至2027年4月29日(包括首尾兩日) (「推廣期」)
- Invite code: MBCARDER
- New customer definition: 全新客戶定義 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: Not detected
- Reward summary: 迎新獎賞指定禮品 迎新獎賞指定禮品換購方式： a. 客戶須於成功批核後一個月內，憑PayKool手機應用程式內的「HK$1 Carder Toysnplace 指定卡盒換購券」，於商戶指定門店以PayKool卡支付HK$1換購指定禮品
- Voucher validity: 有效期為發出日起計1個月內 (以PayKool App內顯示之日期為準)； b. 可供換購的指定禮品由 Carder Toysnplace 提供，款式由商戶決定，有關

### 17. 🚕 PayKool x 幫到你車隊 Friendly Fare Taxi 專屬禮遇 🎉
- URL: https://www.paykool.hk/promotions/friendlyfaretaxi
- Promotion period: 2026年6月10日至2026年12月9日(包括首尾兩日) (「推廣期」)
- Invite code: PPFFT
- New customer definition: 全新客戶定義 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: Not detected
- Reward summary: 迎新獎賞 要求及資格： a. 推廣期內，全新客戶以指定邀請碼「PPFFT 」申請PayKool信用卡, 成功批核後可獲$400免找數簽賬額
- Voucher validity: 有效期內預約車隊服務可享有豁免行李費優惠

### 18. 🧚🏻‍♀️ PayKool × Golden LifeStyle 迎新及持卡人專屬優惠 🎉
- URL: https://www.paykool.hk/promotions/goldenlifestyle
- Promotion period: 2026年4月17日至2026年7月16日(包括首尾兩日) (「推廣期」)
- Invite code: Not detected
- New customer definition: 全新客戶定義 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: Not detected
- Reward summary: 迎新獎賞 要求及資格： a. 推廣期內，客戶於Golden LifeStyle網店消費滿HK$800或以上，將獲Golden LifeStyle職員提供指定邀請碼
- Voucher validity: 有效期為即日至2026年7月16日； • 只適用於Golden LifeStyle網店； • 不能兌換現金及不設找贖； • 不適用於購買禮券、現金券及其他指定產品；

### 19. 🎉 「PayKool × 姐姐王國」 信用卡迎新及持卡人專屬禮遇
- URL: https://www.paykool.hk/promotions/helperkingodom
- Promotion period: 2026年3月17日至2026年6月16日(包括首尾兩日) (「推廣期」)
- Invite code: Not detected
- New customer definition: 全新客戶定義 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: Not detected
- Reward summary: 迎新獎賞 簽賬要求及資格： a. 推廣期內，客戶於姐姐王國分店聘請外傭，可獲姐姐王國職員提供指定邀請碼
- Voucher validity: Not detected

### 20. PayKool x 冒險樂園🎡｜PayKool信用卡迎新獎賞及持卡人專屬禮遇 ✨
- URL: https://www.paykool.hk/promotions/jumpingym
- Promotion period: 2026年6月1日至2027年5月31日(包括首尾兩日) (「推廣期」)
- Invite code: JG
- New customer definition: 全新客戶定義 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: Not detected
- Reward summary: 迎新獎賞 要求及資格： a) 推廣期內，全新客戶以指定邀請碼「JG」申請PayKool 信用卡，成功批核後可獲得以下迎新獎賞： i. 冒險樂園代幣400個：全新客戶可在 PayKool 手機應用程式內的「禮遇」活動頁面，領取冒險樂園代幣電子禮券（「
- Voucher validity: 有效日期至2027年11月30日

### 21. 🔧 PayKool × MAKERSOUL 🛠️ 信用卡迎新及持卡人專屬優惠 🎉
- URL: https://www.paykool.hk/promotions/mbmakersoul
- Promotion period: 2026年3月25日至2027年3月24日(包括首尾兩日) (「推廣期」)
- Invite code: MBMAKERSOUL
- New customer definition: 全新客戶定義 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: 指定簽賬要求」)，可獲得HK$500 PayKool卡免找數簽賬額
- Reward summary: Not detected
- Voucher validity: 有效期至2027年3月24日 b. 只適用於MAKERSOUL指定門店購買指定品牌產品； c. MAKERSOUL 指定門店包括：深水埗汝州街271號1樓及2樓，觀塘

### 22. ✈️ PayKool × SIM SQ 信用卡迎新及持卡人專屬優惠 🎉
- URL: https://www.paykool.hk/promotions/mbsim
- Promotion period: 2026年3月2日至2027年3月1日(包括首尾兩日) (「推廣期」)
- Invite code: MBSIM
- New customer definition: 全新客戶定義 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: 指定簽賬要求」)，可享以下迎新消費獎賞： PayKool卡$288免找數簽賬額，及； 完成指定簽賬要求後一個月內可於PayKool手機應用程式內的「禮遇」活動頁面，使用電子
- Reward summary: 迎新獎賞指定禮品 迎新獎賞指定禮品換領方式： a. 客戶須於完成指定簽賬要求後一個月內，於SIM SQ官方網站，使用PayKool 手機應用程式內有效的電子優惠碼，換領流程如下： i. 開啟 PayKool 手機應用程式 > 禮遇 > 我的禮遇，選
- Voucher validity: 有效期至2027年3月1日； b. 由World Sim Asia Telecom Limited 提供； c. 使用受制於World Sim Asia Teleco

### 23. 🐱【PayKool x OneDegree】信用卡持卡人專屬投保優惠🐶
- URL: https://www.paykool.hk/promotions/onedegree2026
- Promotion period: Not detected
- Invite code: ONEDEGREE
- New customer definition: 全新客戶定義 全新客戶定義為申請日起計過去 12 個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: 指定簽賬要求」），成功投保可享以下對應獎賞： 寵物保險：首年保費 8 折及 $800 免找數簽賬額^；或 家居保險：首年保費 7 折及 $800 免找數簽賬額^；或 火險：
- Reward summary: Not detected
- Voucher validity: Not detected

### 24. PayKool x Trip.com｜機票酒店15%回贈，旅遊必搶優惠！
- URL: https://www.paykool.hk/promotions/paykool-trip-2025
- Promotion period: 2025年8月1日至2026年7月31日，包括首尾兩天 (「推廣期」)
- Invite code: Not detected
- New customer definition: 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請(不論成功申請與否)或擁有任何信用卡賬戶。
- Spend requirement: Not detected
- Reward summary: Not detected
- Voucher validity: Not detected

### 25. 【🍕✨ PayKool x Pizza Hut 迎新消費獎賞✨🍕】
- URL: https://www.paykool.hk/promotions/pizzahut202602
- Promotion period: 2026年2月9日至2026年7月8日(包括首尾兩日) (「推廣期」)
- Invite code: PPPZH
- New customer definition: 全新客戶定義 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: 指定簽賬要求」)，可獲得PayKool卡免找數簽賬額HK$100
- Reward summary: 迎新獎賞：合資格全新客戶可在PayKool手機應用程式內的「禮遇」活動頁面，獲得Pizza Hut HK$300電子現金券，於Pizza Hut分店消費時使用
- Voucher validity: 有效期為即日至2026年8月8日； c. 適用於香港及澳門Pizza Hut必勝客所有分店； d. 不適用於Pizza Hut網上訂購平台落單； e. 適用於堂食或外

### 26. 🔧「 PayKool × 裝修佬」信用卡迎新及持卡人專屬優惠 ✨
- URL: https://www.paykool.hk/promotions/ppdeco
- Promotion period: 2026年3月20日至2026年6月19日(包括首尾兩日) (「推廣期」)
- Invite code: PPDECO
- New customer definition: 全新客戶定義 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: Not detected
- Reward summary: 迎新獎賞 要求及資格： a. 推廣期內，全新客戶以指定邀請碼「PPDECO」申請PayKool信用卡，客戶成功批核後14天內可於PayKool手機應用程式內的「禮遇」活動頁面，使用電子換領券於裝修佬指定換領地點及時間換領由裝修佬提供的「WORX 威
- Voucher validity: 有效期：即日至2026年6月19日 b. 於推廣期內只限使用一次

### 27. 【🍚🔥 PayKool × Home A Day 迎新消費獎賞】
- URL: https://www.paykool.hk/promotions/pphad
- Promotion period: 2026年2月6日至2026年5月5日(包括首尾兩日) (「推廣期」)
- Invite code: PPHAD
- New customer definition: 全新客戶定義 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: 指定簽賬要求」)，可獲得HK$500 PayKool卡免找數簽賬額
- Reward summary: Not detected
- Voucher validity: Not detected

### 28. 🎉【PayKool x 日本城】新客戶迎新及現有客戶消費獎賞
- URL: https://www.paykool.hk/promotions/ppjhc2026
- Promotion period: 2026年4月9日至2026年12月31日，包括首尾兩天（「推廣期」）
- Invite code: Not detected
- New customer definition: 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: Not detected
- Reward summary: 迎新獎賞」推廣優惠（「本推廣活動」），即被視為明白及同意 PayKool Visa Platinum卡（「PayKool卡」）的私隱政策、收集個人資料聲明及本推廣活動之所有條款及細則並受其約束
- Voucher validity: 有效期：即日至2027年4月30日 • 此券只限使用一次

### 29. 【🎉 PayKool x PP Lab 新客戶迎新 + 持卡人優惠🐾】
- URL: https://www.paykool.hk/promotions/pplab
- Promotion period: 2026年3月1日至2026年5月31日(包括首尾兩日) (「推廣期」)
- Invite code: PPLAB
- New customer definition: 全新客戶定義 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: Not detected
- Reward summary: 迎新獎賞 要求及資格： a. 推廣期內，全新客戶在PayKool卡申請介面指定位置輸入指定 邀請碼「PPLAB」 申請PayKool卡，成功獲得批核後，會收到由本公司發出的確認電郵，及獲得以下獎賞
- Voucher validity: 有效期為即日至2027年2月28日； • 每張賬單只接受一張電子折扣券； • 只適用於PP Lab網店； • 不能兌換現金及不設找贖； • 不適用於購買禮券、現金券及

### 30. 🚗 PayKool × StarDrive 迎新及消費專屬優惠
- URL: https://www.paykool.hk/promotions/ppsta
- Promotion period: 2026年2月11日至2026年5月10日(包括首尾兩日) (「推廣期」)
- Invite code: PPSTA
- New customer definition: 全新客戶定義 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: Not detected
- Reward summary: 迎新獎賞 要求及資格： a. 推廣期內，全新客戶在PayKool卡申請介面指定位置輸入指定邀請碼「PPSTA」申請PayKool卡，成功獲得批核後，會收到由本公司發出的確認電郵，及獲得以下獎賞
- Voucher validity: 有效期：即日至2026年6月30日 b. 此券只限使用一次

### 31. 【🍚🔥 PayKool × 華豐燒臘 迎新消費獎賞】
- URL: https://www.paykool.hk/promotions/ppwaf
- Promotion period: 2026年2月6日至2026年5月5日(包括首尾兩日) (「推廣期」)
- Invite code: PPWAF
- New customer definition: 全新客戶定義 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: 指定簽賬要求」)，可獲得HK$388 PayKool卡免找數簽賬額
- Reward summary: Not detected
- Voucher validity: Not detected

### 32. 🦞 PayKool × 威龍海鮮酒家 信用卡迎新及持卡人專屬優惠 🎉
- URL: https://www.paykool.hk/promotions/ppwlsf
- Promotion period: 2026年3月25日至2026年6月24日(包括首尾兩日) (「推廣期」)
- Invite code: PPWLSF
- New customer definition: 全新客戶定義 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: Not detected
- Reward summary: 迎新獎賞 要求及資格： a. 推廣期內，全新客戶以指定邀請碼「PPWLSF」申請PayKool信用卡, 成功批核後可獲$500免找數簽賬額
- Voucher validity: Not detected

### 33. 🍽️ PayKool x 鈺膳潮州菜｜迎新獎賞高達 $500 折扣 ✨
- URL: https://www.paykool.hk/promotions/ppyuk
- Promotion period: 2026年1月19日至2026年4月18日(包括首尾兩日) (「推廣期」)
- Invite code: PPYUK
- New customer definition: 全新客戶定義全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: Not detected
- Reward summary: 迎新獎賞簽賬要求及資格： a. 推廣期內，全新客戶在PayKool卡申請介面指定位置輸入指定邀請碼「PPYUK」申請PayKool卡，成功獲得批核後，會收到由本公司發出的確認電郵及HK$500鈺膳潮州菜電子折扣券(「電子折扣券」)
- Voucher validity: Not detected

### 34. 10%簽賬回贈迎新優惠｜🎉新客戶最高回贈HK$500
- URL: https://www.paykool.hk/promotions/rebate
- Promotion period: 2026年6月1日起至2026年6月14日，包括首尾兩天（「推廣期」）
- Invite code: Not detected
- New customer definition: 全新客戶定義為於申請日前12個月內未曾於本公司申請（不論成功與否）或持有任何信用卡賬戶。
- Spend requirement: Not detected
- Reward summary: 迎新獎賞」推廣優惠之條款及細則 PayKool信用卡「PayKool x Apple Pay加卡賞」推廣活動條款及細則（「本條款及細則」) PayKool Visa Platinum卡「PayKool x Bar Pacific迎新獎賞」及「Pay
- Voucher validity: Not detected

### 35. 【✈️ PayKool x Travel 360｜新客戶迎新獎賞 🎁】
- URL: https://www.paykool.hk/promotions/travel360
- Promotion period: 2026年5月26日至2026年8月25日(包括首尾兩日) (「推廣期」)
- Invite code: PPAT360
- New customer definition: 全新客戶定義 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: Not detected
- Reward summary: 迎新獎賞 要求及資格： a) 推廣期內，全新客戶以指定邀請碼「PPAT360」申請PayKool 信用卡，成功批核後可獲得以下迎新獎賞： i. Travel 360 HK$300 電子折扣券 : 全新客戶可在 PayKool 手機應用程式內的「禮遇
- Voucher validity: 有效日期至2026年9月25日

### 36. 🍔 「PayKool x Two Ediots 」信用卡迎新及持卡人專屬優惠 🎉
- URL: https://www.paykool.hk/promotions/twoediots
- Promotion period: 2026年3月25日至2026年6月24日(包括首尾兩日) (「推廣期」)
- Invite code: Not detected
- New customer definition: 全新客戶定義 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: Not detected
- Reward summary: 迎新獎賞 要求及資格： a. 推廣期內，客戶於Two Ediots門店消費滿HK$400或以上，將獲店員提供指定邀請碼
- Voucher validity: Not detected

## Runbook
1. Refresh rules from website with the script.
2. Load customer profile and transactions.
3. Evaluate checks in order and store pass/fail evidence.
4. Return decision and reasons.

## Refresh Command
`python extract_paykool_terms.py --output-skill skill.md`