# Skill: PayKool x Trip.com｜機票酒店15%回贈，旅遊必搶優惠！

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
- URL: https://www.paykool.hk/promotions/paykool-trip-2025
- Slug: paykool-trip-2025
- Promotion period: 2025年8月1日至2026年7月31日，包括首尾兩天 (「推廣期」)
- Invite code: Not detected
- New customer definition: 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請(不論成功申請與否)或擁有任何信用卡賬戶。
- Spend requirement: Not detected
- Reward summary: 迎新獎賞」推廣優惠之條款及細則 PayKool信用卡「PayKool x Apple Pay加卡賞」推廣活動條款及細則（「本條款及細則」) PayKool Visa Platinum卡「PayKool x Bar Pacific迎新獎賞」及「Pay
- Voucher validity: Not detected
- Customer responsibility: Not detected

## Source Excerpt
條款及細則約束。 自主分期&優惠福利，通通都有！ 靈活分期，輕鬆旅遊 使用PayKool簽賬後可自行選擇分 3/4/5 個月分期付款#，過程只需繳付一次性手續費。靈活選擇最適合用戶的分期計劃，減輕旅費壓力。 不論是機票，還是酒店住宿，都能分期付款，輕鬆享受！ 結合Trip.com優惠，省上加省 PayKool全新客戶於推廣期內出卡後1個月內透過指定鏈結於Trip.com預訂機票及/或酒店，可享15%簽賬回贈優惠*，並搭配自主分期功能#，進一步降低旅遊每月支出壓力！ PayKool現有客戶於推廣期內透過指定鏈結於Trip.com預訂亦可享酒店6%簽賬回贈優惠 *，再結合自主分期#，旅費更可控！ 如何使用PayKool x Trip.com優惠？ 申請PayKool Visa Platinum卡 下載PayKool App並申請PayKool Visa Platinum卡。 使用指定鏈結預訂機票或酒店 PayKool Visa Platinum卡成功批核後，透過指定鏈結前往Trip.com搜尋心儀的航班或住宿，盡享PayKool x Trip.com機票優惠及酒店優惠。 使用PayKool Visa Platinum卡完成支付 使用PayKool Visa Platinum 卡於Trip.com完成支付，全新客戶於推廣期內出卡後1 個月內可獲得15%機票酒店簽賬回贈優惠*。現有客戶亦可於推廣期內享酒店6%簽賬回贈優惠*。 啟用自主分期 簽賬後於PayKool App內啟用自主分期功能#，選擇簽賬分期計劃可達成自主分期。 三大理由｜用PayKool x Trip.com，旅遊就是這麼簡單！ 專屬優惠福利：全新客戶15%機票酒店簽賬回贈優惠*，現有客戶酒店6%簽賬回贈優惠*，PayKool卡用戶獨享！ 靈活分期支付：透過PayKool自主分期功能#，分攤機票或酒店費用，減輕每月開支經濟壓力！ 一站式旅遊服務：Trip.com覆蓋全球220個國家及地區，機票、住宿任用戶選，享受更多便利！Shape 即刻行動｜PayKool自主分期，讓旅遊夢想更輕鬆 透過PayKool自主分期搭配Trip.com專享機票優惠與酒店優惠！，讓用戶立刻啟程，無需等待！不論是環球旅行還是週末小旅行，都可以隨時安排，輕鬆享受旅遊樂趣。 *受活動條款及細則約束。 #受簽賬分期服務條款及細則約束。 立即申請👉PayKool Visa Platinum卡，讓下一趟旅程更實惠、更輕鬆！ 立即預訂 PayKool Visa Platinum卡 x Trip.com推廣優惠之條款及細則 PayKool Visa Platinum卡 x Trip.com推廣優惠之條款及細則(「本條款及細則」)： 任何人士使用由K Cash Limited（「本公司」）旗下PayKool信用卡提供之PayKool Visa Platinum卡x Trip.com推廣優惠（「本推廣活動」），即被視為明白及同意PayKool Visa Platinum卡（「PayKool卡」）的私隱政策、收集個人資料聲明及本推廣活動之所有條款及細則並受其約束，有關資料可於PayKool官方網頁瀏覽。 本推廣活動推廣期為2025年8月1日至2026年7月31日，包括首尾兩天 (「推廣期」)。 本推廣活動只適用於符合以下條件之客戶 (「合資格客戶」)： i. 必須為香港居民身分證持有人；及 ii. 年齡必須年滿18歲或以上；及 iii. PayKool卡現有客戶 (於推廣期內持有有效PayKool卡) ；或 iv. PayKool卡全新客戶 (於推廣期內申請PayKool卡並成功獲得批核以及沒有獲得其他迎新優惠之全新客戶)。 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請(不論成功申請與否)或擁有任何信用卡賬戶。 推廣期內，合資格客戶透過指定鏈結於Trip.com使用PayKool卡簽賬(「指定簽賬」)，可享以下優惠(「此優惠」)： i. PayKool卡全新客戶於PayKool卡獲批後一個月內任何指定簽賬(包括預訂機票及/或酒店)，可享15%簽賬回贈優惠，回贈上限為HK$500；及 ii. PayKool卡現有客戶透過指定簽賬預訂酒店，可享6%簽賬回贈優惠。 以上優惠不能同時使用，以可以獲得的簽賬回贈優惠較高者為

## Refresh
`python extract_paykool_terms.py --split --skills-dir skills`