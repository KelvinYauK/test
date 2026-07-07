# Skill: 【🎉 PayKool x PP Lab 新客戶迎新 + 持卡人優惠🐾】

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
- URL: https://www.paykool.hk/promotions/pplab
- Slug: pplab
- Promotion period: 2026年3月1日至2026年5月31日(包括首尾兩日) (「推廣期」)
- Invite code: PPLAB
- New customer definition: 全新客戶定義 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: Not detected
- Reward summary: 迎新獎賞 要求及資格： a. 推廣期內，全新客戶在PayKool卡申請介面指定位置輸入指定 邀請碼「PPLAB」 申請PayKool卡，成功獲得批核後，會收到由本公司發出的確認電郵，及獲得以下獎賞
- Voucher validity: 有效期為即日至2027年2月28日； • 每張賬單只接受一張電子折扣券； • 只適用於PP Lab網店； • 不能兌換現金及不設找贖； • 不適用於購買禮券、現金券及
- Customer responsibility: 客戶責任 客戶須於付款前聲明享用有關優惠。 如有任何爭議，客戶必須提供有關之文件之正本、交易單據及信用卡簽賬存根正本(如適用)以便本公司作進一步調查。 有關獎賞不可退回、轉讓/轉售、兌換現金或換取其他優惠。如有遺失、失效或逾期，恕不獲補發。 若合資格客戶於得到有關獎賞後一年內取消PayKool卡，將會被收取PayKool卡年費 HK$1,800。 本公司保留給予客戶此優惠之權利，客戶於PayKool卡生效後，PayKool卡戶口須於發放此優惠前維持良好狀況，包括但不限於沒有逾期還款紀錄、未有逾額情況或任何違反信用卡持卡人合約條款的行為。否則，本公司保留對客戶撤回此優惠之獲得權利而毋須事先通知。

## Source Excerpt
條款及細則約束 立即申請 PayKool 信用卡 [PayKool x PP Lab]優惠– PayKool信用卡迎新推廣及持卡人禮遇(「本推廣活動」)之條款及細則 任何人士參與 K Cash Limited（「本公司」）旗下 PayKool 信用卡品牌與 PP Lab（「商戶」）聯合推出的本推廣活動，即表示已充分了解並同意受本條款及細則的約束。 本推廣活動只適用於持有本公司發行之PayKool Visa Platinum卡（「PayKool卡」）之客戶。 優惠推廣期 除特別註明外，優惠推廣期由2026年3月1日至2026年5月31日(包括首尾兩日) (「推廣期」)。 優惠詳情 迎新推廣：PayKool迎新獎賞 要求及資格： a. 推廣期內，全新客戶在PayKool卡申請介面指定位置輸入指定 邀請碼「PPLAB」 申請PayKool卡，成功獲得批核後，會收到由本公司發出的確認電郵，及獲得以下獎賞。 i. PP Lab 網店 HK$100 電子折扣券 (共三張) ：合資格全新客戶在PayKool手機應用程式內的「禮遇」活動頁面，可獲得PP Lab網店 HK$100 電子折扣券三張(合共總值 HK$300)，於PP Lab網店消費滿HK$500，使用電子折扣券上的優惠碼，可即時獲HK$100折扣。 ii. PayKool卡 HK$100免找數簽賬額 ：免找數簽賬額將於PayKool卡獲批後一個月內存入客戶的PayKool卡賬戶。 b. 推廣期內，合資格客戶只可領取PayKool迎新獎賞最多1次。 c. PP Lab網店連結: https://pplab.com.hk/ d. 使用PP Lab網店電子折扣券受其條款及細則約束。 持卡人禮遇：指定商戶精彩禮遇 要求及資格： a. 推廣期內，PayKool信用卡客戶於PP Lab網店使用PayKool持卡人優惠碼消費，可享全單9折。 b. 推廣期內，合資格客戶可享指定商戶精彩禮遇不設使用次數上限。 c. PayKool持卡人優惠碼不可與其他優惠﹑折扣或優惠碼同時使用。 d. PP Lab網店連結: https://pplab.com.hk/ e. 使用PayKool持卡人優惠碼受其條款及細則約束。 獎賞領取方式 PayKool卡免找數簽賬額 免找數簽賬額將於PayKool卡獲批後一個月內存入客戶的PayKool卡賬戶。 商戶電子折扣券/ 優惠券 PP Lab 網店 HK$100 電子折扣券領取及使用方式： a. 合資格全新客戶在PayKool手機應用程式內的「禮遇」活動頁面，可獲得PP Lab網店 HK$100 電子折扣券三張(合共總值 HK$300)，於PP Lab網店消費滿HK$500，使用電子折扣券上的優惠碼，可即時獲HK$100折扣。使用流程如下： i. 於付款前請前往 PayKool 手機應用程式 > 禮遇 > 我的禮遇，選取相關電子折扣券； ii. 按下「立即領取」按鈕； iii. 頁面會顯示PP Lab 網店 HK$100 電子折扣券優惠碼； iv. 於PP Lab網店付款前輸入電子折扣券上的優惠碼享用折扣。 PayKool持卡人優惠碼領取及使用方式： b. PayKool卡持卡人在PayKool手機應用程式內的「禮遇」活動頁面，可獲得一張「電子優惠券」， 領取相關電子優惠券後，會顯示PayKool持卡人優惠碼，使用流程如下： i. 於付款前請前往 PayKool 手機應用程式 > 禮遇，選取相關電子優惠券； ii. 按下「立即領取」按鈕； iii. 頁面會顯示PayKool持卡人優惠碼； iv. 於PP Lab網店付款前輸入PayKool持卡人優惠碼以享用優惠。 商戶電子折扣券/ 優惠券條款及細則 PP Lab網店電子折扣券使用條款包括(但不限於)： • 電子折扣券有效期為即日至2027年2月28日； • 每張賬單只接受一張電子折扣券； • 只適用於PP Lab網店； • 不能兌換現金及不設找贖； • 不適用於購買禮券、現金券及其他指定產品； • 不可與其他優惠﹑折扣或優惠碼同時使用； • 如有任何爭議，PP Lab保留最終決定權。 PayKool持卡人優惠碼使用條款包括(但不限於)： • PayKool持卡人優惠碼有效期為即日至2026年5月31日； • 只適用於PP Lab網

## Refresh
`python extract_paykool_terms.py --split --skills-dir skills`