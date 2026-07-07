# Skill: 🚗 PayKool × StarDrive 迎新及消費專屬優惠

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
- URL: https://www.paykool.hk/promotions/ppsta
- Slug: ppsta
- Promotion period: 2026年2月11日至2026年5月10日(包括首尾兩日) (「推廣期」)
- Invite code: PPSTA
- New customer definition: 全新客戶定義 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: Not detected
- Reward summary: 迎新獎賞 要求及資格： a. 推廣期內，全新客戶在PayKool卡申請介面指定位置輸入指定邀請碼「PPSTA」申請PayKool卡，成功獲得批核後，會收到由本公司發出的確認電郵，及獲得以下獎賞
- Voucher validity: 有效期：即日至2026年6月30日 b. 此券只限使用一次
- Customer responsibility: 客戶責任 如有任何爭議，客戶必須提供有關之文件之正本、交易單據及信用卡簽賬存根正本(如適用)以便本公司作進一步調查。 有關獎賞不可退回、轉讓/轉售、兌換現金或換取其他優惠。如有遺失、失效或逾期，恕不獲補發。 若合資格客戶於得到有關獎賞後一年內取消PayKool卡，將會被收取PayKool卡年費 HK$1,800。 本公司保留給予客戶此優惠之權利，客戶於PayKool卡生效後，PayKool卡戶口須於發放此優惠前維持良好狀況，包括但不限於沒有逾期還款紀錄、未有逾額情況或任何違反信用卡持卡人合約條款的行為。否則，本公司保留對客戶撤回此優惠之獲得權利而毋須事先通知。

## Source Excerpt
條款及細則約束 立即申請PayKool 信用卡 [PayKool x StarDrive]優惠– PayKool信用卡迎新推廣(「本推廣活動」)之條款及細則 任何人士參與 K Cash Limited（「本公司」）旗下 PayKool 信用卡品牌與 StarDrive（「商戶」）聯合推出的本推廣活動，即表示已充分了解並同意受本條款及細則的約束。 本推廣活動只適用於持有本公司發行之PayKool Visa Platinum卡（「PayKool卡」）之客戶。 優惠推廣期 除特別註明外，優惠推廣期由2026年2月11日至2026年5月10日(包括首尾兩日) (「推廣期」)。 優惠詳情 迎新推廣：PayKool迎新獎賞 要求及資格： a. 推廣期內，全新客戶在PayKool卡申請介面指定位置輸入指定邀請碼「PPSTA」申請PayKool卡，成功獲得批核後，會收到由本公司發出的確認電郵，及獲得以下獎賞。 i. StarDrive HK$200電子現金券：合資格全新客戶可在PayKool手機應用程式內的「禮遇」活動頁面，獲得StarDrive HK$200電子現金券，於StarDrive網上平台消費時使用。 ii. PayKool卡 HK$100免找數簽賬額：免找數簽賬額將於PayKool卡獲批後一個月內存入客戶的PayKool卡賬戶。 b. 推廣期內，合資格客戶只可領取PayKool迎新獎賞最多1次。 c. StarDrive網上平台連結: https://stardrivehk.com/ d. 使用StarDrive電子現金券受其條款及細則約束。 持卡人禮遇：指定商戶精彩禮遇 要求及資格： a. 推廣期內，PayKool信用卡客戶於StarDrive網上平台，於付款前使用PayKool持卡人優惠碼購買指定服務，可享以下優惠價: 優惠1: 專業人手洗車+Ozone空氣淨化 優惠價HK$288 (原價HK$710) (🔗 優惠連結 ) 優惠2: 一般私家車特亮水晶車蠟服務 優惠價 HK$888 (原價HK$2,080) (🔗 優惠連結 ) 優惠3: 吸塵 + 360度車廂納米消毒 + 蒸汽內籠消毒 優惠價HK$1,688 (原價HK$3,020) (🔗 優惠連結 ) b. PayKool卡持卡人在PayKool手機應用程式內的「禮遇」活動頁面，可獲得三張「電子優惠券」， 領取相關電子優惠券後，會顯示PayKool持卡人優惠碼。於StarDrive網上平台於付款前可以PayKool持卡人優惠碼，以優惠價購買指定服務。 c. 使用StarDrive電子優惠券受其條款及細則約束。 獎賞領取方式 商戶(電子)現金券 StarDrive HK$200電子現金券領取及使用方式： a. 客戶須於StarDrive網上平台消費，並於付款前出示PayKool 手機應用程式內有效的電子現金券，使用流程如下： i. 付款前請前往 PayKool 手機應用程式 > 禮遇 > 我的禮遇，選取相關電子現金券； ii. 按下「立即領取」按鈕； iii. 頁面會顯示HK$200 StarDrive電子現金券優惠碼； iv. 於StarDrive網上平台付款前輸入電子現金券上的優惠碼。 商戶(電子)優惠券 StarDrive電子優惠券領取及使用方式： a. PayKool卡持卡人在PayKool手機應用程式內的「禮遇」活動頁面，可獲得三張「電子優惠券」， 領取相關電子優惠券後，會顯示PayKool持卡人優惠碼，使用流程如下： i. 付款前請前往 PayKool 手機應用程式 > 禮遇，選取相關電子優惠券； ii. 按下「立即領取」按鈕； iii. 頁面會顯示PayKool持卡人優惠碼； iv. 於StarDrive網上平台付款前輸入PayKool持卡人優惠碼以享用折扣； 現金券條款及細則 StarDrive HK$200電子現金券使用條款包括： a. 電子現金券有效期：即日至2026年6月30日 b. 此券只限使用一次。 c. 此券不能兌換現金及不設找贖。 d. 如有任何爭議，StarDrive網上平台保留此使用優惠之最終決定權。 StarDrive電子優惠券使用條款包括： a. 電子優惠券有效期：即日至2026年5月10日 b. 於推廣期內使用次數不設上限。 c. 此券不能兌換

## Refresh
`python extract_paykool_terms.py --split --skills-dir skills`