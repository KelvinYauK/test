# Skill: 【🍕✨ PayKool x Pizza Hut 迎新消費獎賞✨🍕】

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
- URL: https://www.paykool.hk/promotions/pizzahut202602
- Slug: pizzahut202602
- Promotion period: 2026年2月9日至2026年7月8日(包括首尾兩日) (「推廣期」)
- Invite code: PPPZH
- New customer definition: 全新客戶定義 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: 指定簽賬要求」)，可獲得PayKool卡免找數簽賬額HK$100
- Reward summary: 迎新獎賞：合資格全新客戶可在PayKool手機應用程式內的「禮遇」活動頁面，獲得Pizza Hut HK$300電子現金券，於Pizza Hut分店消費時使用
- Voucher validity: 有效期為即日至2026年8月8日； c. 適用於香港及澳門Pizza Hut必勝客所有分店； d. 不適用於Pizza Hut網上訂購平台落單； e. 適用於堂食或外
- Customer responsibility: 客戶責任 如有任何爭議，客戶必須提供有關之文件之正本、交易單據及信用卡簽賬存根正本(如適用)以便本公司作進一步調查。 有關獎賞不可退回、轉讓/轉售、兌換現金或換取其他優惠。如有遺失、失效或逾期，恕不獲補發。 若合資格客戶於得到有關獎賞後一年內取消PayKool卡，將會被收取PayKool卡年費 HK$1,800。 本公司保留給予客戶此優惠之權利，客戶於PayKool卡生效後，PayKool卡戶口須於發放此優惠前維持良好狀況，包括但不限於沒有逾期還款紀錄、未有逾額情況或任何違反信用卡持卡人合約條款的行為。否則，本公司保留對客戶撤回此優惠之獲得權利而毋須事先通知。

## Source Excerpt
條款及細則約束 立即申請 [PayKool x Pizza Hut]優惠– PayKool信用卡迎新推廣(「本推廣活動」)之條款及細則 任何人士參與 K Cash Limited（「本公司」）旗下 PayKool 信用卡品牌與 Pizza Hut（「商戶」）聯合推出的本推廣活動，即表示已充分了解並同意受本條款及細則的約束。 本推廣活動優惠只適用於持有本公司發行之PayKool Visa Platinum卡（「PayKool卡」）之客戶。 優惠推廣期 除特別註明外，優惠推廣期由2026年2月9日至2026年7月8日(包括首尾兩日) (「推廣期」)。 優惠詳情 迎新推廣：PayKool迎新及消費獎賞 要求及資格： a. 推廣期內，全新客戶在PayKool卡申請介面指定位置輸入**指定邀請碼「PPPZH」**申請PayKool卡，成功獲得批核後，會收到由本公司發出的確認電郵，及獲得以下獎賞。 i.PayKool迎新獎賞：合資格全新客戶可在PayKool手機應用程式內的「禮遇」活動頁面，獲得Pizza Hut HK$300電子現金券，於Pizza Hut分店消費時使用。 ii.PayKool迎新消費獎賞：客戶需於PayKool卡成功批核後的2個月內於Pizza Hut分店或Pizza Hut網上訂購平台，使用PayKool卡完成單一合資格簽賬滿HK$100 (「指定簽賬要求」)，可獲得PayKool卡免找數簽賬額HK$100。免找數簽賬額將於完成指定簽賬要求後下一個月內存入客戶的PayKool卡賬戶。 b. 推廣期內，合資格客戶只可領取PayKool迎新獎賞最多1次。 c. 合資格客戶只可獲得PayKool迎新消費獎賞最多1次，即合共最高HK$100 PayKool卡免找數簽賬額。 d. 使用商戶(電子)現金券受其條款及細則約束。 獎賞領取方式 商戶(電子)現金券 Pizza Hut HK$300電子現金券領取及使用方式： a. 客戶須於Pizza Hut分店落單時聲明使用此電子現金券，並於付款前向店員出示PayKool 手機應用程式內有效的商戶電子現金券以換領優惠，使用流程如下： i. 付款前請前往 PayKool 手機應用程式 > 禮遇 > 我的禮遇，選取相關電子現金券； ii. 按下「立即領取」按鈕； iii. 頁面會顯示HK$300 Pizza Hut電子現金券的QR code； iv. 於付款前向店員出示電子現金券的QR code。 現金券條款及細則 Pizza Hut HK$300電子現金券使用條款包括(但不限於)： a. 憑券於Pizza Hut所有分店惠顧堂食或外賣自取或外送速遞即可享全單減HK$300； b. HK$300電子現金券有效期為即日至2026年8月8日； c. 適用於香港及澳門Pizza Hut必勝客所有分店； d. 不適用於Pizza Hut網上訂購平台落單； e. 適用於堂食或外賣自取或外送速遞； f. 每張電子現金券只限使用一次。每張賬單只接受一張電子現金券； g. 請於分店落單時聲明使用此電子現金券，並於付款前向店員出示PayKool 手機應用程式內有效的商戶電子現金券以換領優惠；兌換一經確認，有關兌換不可取消或退款。 h. 每張只可使用一次，不得分拆交易使用； i. 此券不可轉售、兌換現金或退換，亦不設退款及找續。 j. 此券不適用於購買現金券、禮券或任何香港必勝客禮品。 k. 如有任何爭議，香港及澳門必勝客保留對此優惠券使用的最終決定權。 一般條款及細則 全新客戶定義 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。 合資格簽賬 合資格簽賬只包括所有已入賬之本地及 / 或海外零售購物金額及 / 或網上消費零售購物金額，並不包括（但不限於）以下類別的消費或單據： a. 現金透支金額、信用卡費用（包括年費、利息 / 財務費用、逾期費用、超逾信用額手續費、現金透支手續費及其他費用）、賭場交易金額、任何金錢 / 電子貨幣轉賬（包括但不只限於個人對個人(P2P)支付服務或流動裝置/應用程式/電子轉賬平台）/充值電子錢包、優惠套現金額、現金分期、分期金額、未入賬 / 取消 / 退回 / 偽造之交易金額及所有未經授權之交易金額； b. 任何重印單據、單據之影印副本、

## Refresh
`python extract_paykool_terms.py --split --skills-dir skills`