# Skill: 🍽️ PayKool x 鈺膳潮州菜｜迎新獎賞高達 $500 折扣 ✨

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
- URL: https://www.paykool.hk/promotions/ppyuk
- Slug: ppyuk
- Promotion period: 2026年1月19日至2026年4月18日(包括首尾兩日) (「推廣期」)
- Invite code: PPYUK
- New customer definition: 全新客戶定義全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: Not detected
- Reward summary: 迎新獎賞簽賬要求及資格： a. 推廣期內，全新客戶在PayKool卡申請介面指定位置輸入指定邀請碼「PPYUK」申請PayKool卡，成功獲得批核後，會收到由本公司發出的確認電郵及HK$500鈺膳潮州菜電子折扣券(「電子折扣券」)
- Voucher validity: Not detected
- Customer responsibility: 客戶責任 客戶須於付款前聲明享用有關優惠，並以PayKool卡全數簽賬方可享優惠。 如有任何爭議，客戶必須提供有關之文件之正本、交易單據及信用卡簽賬存根正本(如適用)以便本公司作進一步調查。 有關獎賞不可退回、轉讓/轉售、兌換現金或換取其他優惠。如有遺失、失效或逾期，恕不獲補發。 若合資格客戶於得到有關獎賞後一年內取消PayKool卡，將會被收取PayKool卡年費 HK$1,800。 本公司保留給予客戶此優惠之權利，客戶於PayKool卡生效後，PayKool卡戶口須於發放此優惠前維持良好狀況，包括但不限於沒有逾期還款紀錄、未有逾額情況或任何違反信用卡持卡人合約條款的行為。否則，本公司保留對客戶撤回此優惠之獲得權利而毋須事先通知。

## Source Excerpt
條款及細則約束 立即申請享優惠 [PayKool x 鈺膳潮州菜]優惠– PayKool信用卡迎新推廣及持卡人禮遇 (「本推廣活動」)之條款及細則 任何人士參與 K Cash Limited（「本公司」）旗下 PayKool 信用卡品牌與 鈺膳潮州菜（「商戶」）聯合推出的本推廣活動，即表示已充分了解並同意受本條款及細則的約束。 本推廣活動只適用於持有本公司發行之PayKool Visa Platinum卡（「PayKool卡」）之客戶。 優惠推廣期 除特別註明外，優惠推廣期由2026年1月19日至2026年4月18日(包括首尾兩日) (「推廣期」)。 優惠詳情 PayKool迎新獎賞簽賬要求及資格： a. 推廣期內，全新客戶在PayKool卡申請介面指定位置輸入指定邀請碼「PPYUK」申請PayKool卡，成功獲得批核後，會收到由本公司發出的確認電郵及HK$500鈺膳潮州菜電子折扣券(「電子折扣券」)。客戶需於PayKool卡成功批核後的一個月內於鈺膳潮州菜消費滿HK$2,000，並以PayKool卡簽賬，即可使用電子折扣券。 b. 合資格客戶只可使用PayKool迎新獎賞最多1次。 c. 鈺膳潮州菜地址: 香港銅鑼灣登龍街1號金朝陽中心2期25樓。 d. 使用電子折扣券受其條款及細則約束。 持卡人禮遇：指定商戶精彩禮遇 要求及資格： a. 推廣期內，PayKool卡持卡人於鈺膳潮州菜消費並以PayKool信用卡簽賬，可享全單88折。禮遇由商戶提供，付款前請先向商戶職員查詢。 b. 此優惠不能與迎新獎賞的電子折扣券同時使用。 c. 鈺膳潮州菜地址: 香港銅鑼灣登龍街1號金朝陽中心2期25樓。 d.禮遇受鈺膳潮州菜條款及細則約束。 e. 本公司及鈺膳潮州菜保留隨時修改或終止本優惠的權利，恕不另行通知。 獎賞領取方式 商戶迎新獎賞電子折扣券領取及使用方式： a. 客戶須於鈺膳潮州菜消費滿HK$2,000,付款前出示PayKool 手機應用程式內有效的電子折扣券，並由鈺膳潮州菜職員驗證兌換資格後才可使用。驗證流程如下： i. 付款前請前往 PayKool 手機應用程式 > 禮遇 > 我的禮遇，選取相關電子折扣券； ii. 按下「立即領取」按鈕； iii. 即場掃描由鈺膳潮州菜職員提供的指定QR code； iv. 成功驗證會顯示「兌換成功」。 v. 驗證成功後，客戶以PayKool信用卡簽賬可即時獲$500折扣。完成簽賬後，職員將於發票及電子貨幣付款存根蓋印，並拍照備份以作記錄。 a. 一般條款及細則 全新客戶定義全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。 合資格簽賬 合資格簽賬只包括所有已入賬之本地及 / 或海外零售購物金額及 / 或網上消費零售購物金額，並不包括（但不限於）以下類別的消費或單據： a. 現金透支金額、信用卡費用（包括年費、利息 / 財務費用、逾期費用、超逾信用額手續費、現金透支手續費及其他費用）、賭場交易金額、任何金錢 / 電子貨幣轉賬（包括但不只限於個人對個人(P2P)支付服務或流動裝置/應用程式/電子轉賬平台）/充值電子錢包、優惠套現金額、現金分期、分期金額、未入賬 / 取消 / 退回 / 偽造之交易金額及所有未經授權之交易金額； b. 任何重印單據、單據之影印副本、分拆之單據及手寫單據； c. 本公司不時決定的任何其他消費或單據類別。 指定商戶消費獎賞適用於手機流動支付簽賬 (Apple Pay, Google Pay™)，但不適用於任何電子錢包簽賬之交易 (包括但不限於支付寶)。 客戶責任 客戶須於付款前聲明享用有關優惠，並以PayKool卡全數簽賬方可享優惠。 如有任何爭議，客戶必須提供有關之文件之正本、交易單據及信用卡簽賬存根正本(如適用)以便本公司作進一步調查。 有關獎賞不可退回、轉讓/轉售、兌換現金或換取其他優惠。如有遺失、失效或逾期，恕不獲補發。 若合資格客戶於得到有關獎賞後一年內取消PayKool卡，將會被收取PayKool卡年費 HK$1,800。 本公司保留給予客戶此優惠之權利，客戶於PayKool卡生效後，PayKool卡戶口須於發放此優惠前維持良好狀況，包括但不限於沒有逾期還款紀錄、未有逾額情況或任何違反信用卡持卡人合約條款的行為。否則，

## Refresh
`python extract_paykool_terms.py --split --skills-dir skills`