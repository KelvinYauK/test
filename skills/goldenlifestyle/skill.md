# Skill: 🧚🏻‍♀️ PayKool × Golden LifeStyle 迎新及持卡人專屬優惠 🎉

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
- URL: https://www.paykool.hk/promotions/goldenlifestyle
- Slug: goldenlifestyle
- Promotion period: 2026年4月17日至2026年7月16日(包括首尾兩日) (「推廣期」)
- Invite code: Not detected
- New customer definition: 全新客戶定義 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: Not detected
- Reward summary: 迎新獎賞 要求及資格： a. 推廣期內，客戶於Golden LifeStyle網店消費滿HK$800或以上，將獲Golden LifeStyle職員提供指定邀請碼
- Voucher validity: 有效期為即日至2026年7月16日； • 只適用於Golden LifeStyle網店； • 不能兌換現金及不設找贖； • 不適用於購買禮券、現金券及其他指定產品；
- Customer responsibility: 客戶責任 客戶須於付款前聲明享用有關優惠。 如有任何爭議，客戶必須提供有關之文件之正本、交易單據及信用卡簽賬存根正本(如適用)以便本公司作進一步調查。 有關獎賞不可退回、轉讓/轉售、兌換現金或換取其他優惠。如有遺失、失效或逾期，恕不獲補發。 若合資格客戶於得到有關獎賞後一年內取消PayKool卡，將會被收取PayKool卡年費 HK$1,800。 本公司保留給予客戶此優惠之權利，客戶於PayKool卡生效後，PayKool卡戶口須於發放此優惠前維持良好狀況，包括但不限於沒有逾期還款紀錄、未有逾額情況或任何違反信用卡持卡人合約條款的行為。否則，本公司保留對客戶撤回此優惠之獲得權利而毋須事先通知。

## Source Excerpt
條款及細則約束 立即申請 PayKool 信用卡 [PayKool x Golden LifeStyle]優惠– PayKool信用卡迎新推廣及持卡人禮遇(「本推廣活動」)之條款及細則 任何人士參與 K Cash Limited（「本公司」）旗下 PayKool 信用卡品牌與Golden LifeStyle（「商戶」）聯合推出的本推廣活動，即表示已充分了解並同意受本條款及細則的約束。 本推廣活動優惠只適用於持有本公司發行之PayKool Visa Platinum卡（「PayKool卡」）之客戶。 優惠推廣期 除特別註明外，優惠推廣期由2026年4月17日至2026年7月16日(包括首尾兩日) (「推廣期」)。 優惠詳情 迎新推廣：PayKool迎新獎賞 要求及資格： a. 推廣期內，客戶於Golden LifeStyle網店消費滿HK$800或以上，將獲Golden LifeStyle職員提供指定邀請碼。客戶使用該指定邀請碼申請PayKool信用卡, 成功申請之全新客戶可獲$500免找數簽賬額。 b. 推廣期內，合資格客戶只可領取PayKool迎新獎賞最多1次，即合共最高HK$500 PayKool卡免找數簽賬額。 c. Golden LifeStyle網店連結: https://www.golden-lifestyle.com/ d. 如需取得指定邀請碼申請PayKool信用卡，請聯絡Golden LifeStyle職員: • Golden LifeStyle客服電話：852-61815163 • Golden LifeStyle WhatsApp聯絡連結: https://wa.me/85261815163 持卡人禮遇：指定商戶精彩禮遇 要求及資格： a. 在推廣期內，PayKool 信用卡客戶於Golden Lifestyle網店使用 PayKool 持卡人優惠碼消費，即可享全單5%折扣優惠。 b. 推廣期內，合資格客戶可享指定商戶精彩禮遇不設使用次數上限。 c. Golden LifeStyle網店連結: https://www.golden-lifestyle.com/ 獎賞領取方式 PayKool卡免找數簽賬額 免找數簽賬額將於PayKool信用卡獲批後一個月內存入客戶的PayKool信用卡賬戶。 商戶電子折扣券/ 優惠券 PayKool持卡人優惠碼領取及使用方式： a. PayKool卡持卡人在PayKool手機應用程式內的「禮遇」活動頁面，可獲得一張「電子優惠券」， 領取相關電子優惠券後，會顯示PayKool持卡人優惠碼，使用流程如下： i. 於付款前請前往 PayKool 手機應用程式 > 禮遇，選取相關電子優惠券； ii. 按下「立即領取」按鈕； iii. 頁面會顯示PayKool持卡人優惠碼； iv. 於Golden LifeStyle網店付款前輸入PayKool持卡人優惠碼以享用優惠。 電子優惠券使用條款包括(但不限於)： • PayKool持卡人優惠碼有效期為即日至2026年7月16日； • 只適用於Golden LifeStyle網店； • 不能兌換現金及不設找贖； • 不適用於購買禮券、現金券及其他指定產品； • 不可與其他優惠﹑折扣或優惠碼同時使用； • 如有任何爭議，Golden LifeStyle保留最終決定權。 一般條款及細則 全新客戶定義 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。 合資格簽賬 合資格簽賬只包括所有已入賬之本地及 / 或海外零售購物金額及 / 或網上消費零售購物金額，並不包括（但不限於）以下類別的消費或單據： a. 現金透支金額、信用卡費用（包括年費、利息 / 財務費用、逾期費用、超逾信用額手續費、現金透支手續費及其他費用）、賭場交易金額、任何金錢 / 電子貨幣轉賬（包括但不只限於個人對個人(P2P)支付服務或流動裝置/應用程式/電子轉賬平台）/充值電子錢包、優惠套現金額、現金分期、分期金額、未入賬 / 取消 / 退回 / 偽造之交易金額及所有未經授權之交易金額； b. 任何重印單據、單據之影印副本、分拆之單據及手寫單據； c. 本公司不時決定的任何其他消費或單據類別。 指定商戶消費獎賞適用於手機流動支付簽賬 (Apple

## Refresh
`python extract_paykool_terms.py --split --skills-dir skills`