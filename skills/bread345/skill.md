# Skill: Paykool復活節Truck Show驚喜快閃登場 挑戰贏高達 $10,000 簽賬回贈上限

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
- URL: https://www.paykool.hk/promotions/bread345
- Slug: bread345
- Promotion period: Not detected
- Invite code: Not detected
- New customer definition: 全新客戶定義為申請日起計過去 12 個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: Not detected
- Reward summary: 迎新獎賞」推廣優惠之條款及細則 PayKool信用卡「PayKool x Apple Pay加卡賞」推廣活動條款及細則（「本條款及細則」) PayKool Visa Platinum卡「PayKool x Bar Pacific迎新獎賞」及「Pay
- Voucher validity: Not detected
- Customer responsibility: Not detected

## Source Excerpt
條款及細則約束 ^活動當日的詳細活動資訊及地址有機會不時更新，請瀏覽Paykool Facebook或Instagram專頁。 點解揀 PayKool？ 消費更自由．生活更輕鬆 • 最長 46 日免息還款期 : 先消費，後付款，現金流更靈活 • 自主分期你話事 : 任何簽賬可即時於 App 選擇 3 / 4 / 5 個月分期， 擺脫長期財務壓力，消費更從容 • 即開即用，付款無阻 : 申請流程簡單，最快 3 分鐘完成批核， 數位卡即時開通，支援 Apple Pay / Google Pay / AlipayHK • 無最低入息要求 : 公屋、居屋、私樓住戶均可申請，入場門檻低 PayKool 支持你 即刻擁有，及早享受， 由日常開支到節日消費，一張卡幫你輕鬆應付。 新客戶限定 獎賞及名額有限，送完即止 上述產品受條款及細則約束，詳情請參閱 https://www.paykool.hk/ 或 PayKool App PayKool Visa Platinum卡「復活節Truck Show驚喜快閃」智取金麵包大挑戰迎新活動之條款及細則 任何人士參與由 K Cash Limited（「本公司」）旗下 PayKool 信用卡提供之 PayKool Visa Platinum 卡「復活節Truck Show驚喜快閃」智取金麵包大挑戰迎新活動（「本推廣活動」），即被視為明白及同意 PayKool Visa Platinum 卡（「PayKool 卡」）的私隱政策、收集個人資料聲明及本推廣活動之所有條款及細則並受其約束，有關資料可於 PayKool 官方網頁瀏覽。 本推廣活動推廣期及指定活動地點以PayKool Facebook / Instagram 專頁公布為準（「推廣期」）。本推廣活動指定活動地點為 PayKool 流動推廣車（「指定活動地點」）。最終活動日期、時間及地點以現場或PayKool社交媒體專頁公布為準。 本推廣活動提供的指定獎賞只適用於推廣期內於指定活動地點使用指定優惠碼成功申請PayKool卡並獲得批核的全新客戶（「合資格客戶」）。 全新客戶定義為申請日起計過去 12 個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。 參加者必須為香港居民身分證持有人及年滿 18 歲或以上。如現場PayKool工作人員認為有需要，可要求參加者出示身分證以確認符合參加資格。 推廣期內，參加者可於指定活動地點按現場PayKool工作人員指示參與遊戲： 1、 完成簡單任務爭取遊戲時限； 2、 在時限內，用智慧同技巧從遊戲專用機取出金色、銀色或銅色道具麵包其中一個 (如取出多於1個道具麵包，將被視作取出銅色道具麵包，不得異議)； 3、按照取出麵包的顏色贏取7日自主消費體驗 ，獲得相應限時7日PayKool卡100%簽賬回贈金額上限（「指定獎賞」）： i. 金色麵包：限時7日100%簽賬回贈上限HK$10,000(名額1個) ii. 銀色麵包：限時7日100%簽賬回贈上限HK$1,000 (名額5個) iii. 銅色麵包：限時7日100%簽賬回贈上限HK$500 遊戲結果及合資格客戶所得指定獎賞以本公司紀錄為準，不得異議。 獲得指定獎賞之合資格客戶，於PayKool卡成功批核後翌日起計7個曆日內，使用PayKool卡完成合資格消費簽賬可獲得100%簽賬回贈，簽賬回贈金額上限以上述遊戲結果為準。例子：如遊戲中取得銅色麵包，即獲得限時7日100%簽賬回贈上限HK$500。如合資格客戶之PayKool卡於2026年4月1日成功獲批核，於2026年6月30日或之前，合資格客戶使用 PayKool 卡進行合資格消費可享100%簽賬回贈優惠，假如最終合資格消費簽賬額為HK$1,000，可獲得的簽賬回贈只可以為上限HK$500。 每位合資格客戶於本推廣活動只可參與遊戲及獲取指定獎賞乙次。如合資格客戶參與遊戲多於1次，將以本公司紀錄第1次遊戲結果為準。 本推廣活動遊戲及指定獎賞名額有限，先到先得，送完即止。 指定活動地點內任何非本公司受權人士不得進行任何形式的拍攝活動，如有違反會被取消參加本推廣活動的資格，本公司保留一切法律追究權利。 合資格消費包括成功入賬的本地、海外零售交易和網上購物消費，但不包括以下類別： i. 現金透支、信用卡費用（包括但不限於年

## Refresh
`python extract_paykool_terms.py --split --skills-dir skills`