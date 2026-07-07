# Skill: 🎉 「PayKool × 姐姐王國」 信用卡迎新及持卡人專屬禮遇

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
- URL: https://www.paykool.hk/promotions/helperkingodom
- Slug: helperkingodom
- Promotion period: 2026年3月17日至2026年6月16日(包括首尾兩日) (「推廣期」)
- Invite code: Not detected
- New customer definition: 全新客戶定義 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: Not detected
- Reward summary: 迎新獎賞 簽賬要求及資格： a. 推廣期內，客戶於姐姐王國分店聘請外傭，可獲姐姐王國職員提供指定邀請碼
- Voucher validity: Not detected
- Customer responsibility: 客戶責任 客戶須於付款前聲明享用有關優惠。 如有任何爭議，客戶必須提供有關之文件之正本、交易單據及信用卡簽賬存根正本(如適用)以便本公司作進一步調查。 有關獎賞不可退回、轉讓/轉售、兌換現金或換取其他優惠。如有遺失、失效或逾期，恕不獲補發。 若合資格客戶於得到有關獎賞後一年內取消PayKool卡，將會被收取PayKool卡年費 HK$1,800。 本公司保留給予客戶此優惠之權利，客戶於PayKool卡生效後，PayKool卡戶口須於發放此優惠前維持良好狀況，包括但不限於沒有逾期還款紀錄、未有逾額情況或任何違反信用卡持卡人合約條款的行為。否則，本公司保留對客戶撤回此優惠之獲得權利而毋須事先通知。

## Source Excerpt
條款及細則約束 PayKool僅提供優惠資訊並不構成對商戶提供的產品及/或服務推薦或要約。 立即申請 PayKool 信用卡 [PayKool x 姐姐王國]優惠– PayKool信用卡迎新推廣及持卡人禮遇(「本推廣活動」)之條款及細則 任何人士參與 K Cash Limited（「本公司」）旗下 PayKool 信用卡品牌與姐姐王國（「商戶」）聯合推出的本推廣活動，即表示已充分了解並同意受本條款及細則的約束。 本推廣活動只適用於持有本公司發行之PayKool Visa Platinum卡（「PayKool卡」）之客戶。 優惠推廣期 除特別註明外，優惠推廣期由2026年3月17日至2026年6月16日(包括首尾兩日) (「推廣期」)。 優惠詳情 PayKool迎新獎賞 簽賬要求及資格： a. 推廣期內，客戶於姐姐王國分店聘請外傭，可獲姐姐王國職員提供指定邀請碼。客戶使用該指定邀請碼申請PayKool信用卡，成功申請之全新客戶可獲$400免找數簽賬額。 b. 推廣期內，合資格客戶只可領取PayKool迎新獎賞最多1次，即合共最高HK$400 PayKool信用卡免找數簽賬額。 c. 姐姐王國分店： • 將軍澳富康花園91號舖 • 沙田石門京瑞廣場一期129號舖 • 沙田石門京瑞廣場二期120號舖 • 奧運西九滙108C號舖 持卡人禮遇：指定商戶精彩禮遇 要求及資格： 推廣期內，PayKool卡持卡人於姐姐王國分店聘請(i) 外籍家傭; 或 (ii) 外籍司機; 或 (iii) 補充勞工，於付款前出示PayKool信用卡，可享每單$1,000折扣。 優惠條款及細則： a. 推廣期內，合資格客戶可享指定商戶精彩禮遇一次。 b. 優惠只適用於於姐姐王國分店成功聘請外籍家傭、外籍司機或補充勞工的客戶。 c. 每位客戶每單交易只可享用一次優惠，不得累積或轉讓。 d. 折扣不可兌換現金，不可轉售或轉讓。 e. 以上折扣優惠不可與商戶其他優惠共同使用。 f. 客戶必須於交易時出示有效的 PayKool信用卡，方可享有折扣。 g. 商戶不會就因使用或未能使用優惠而引致的任何損失或爭議承擔責任。 h. 優惠由商戶提供，並受商戶條款及細則約束。 i. 本公司及商戶保留隨時修改或終止本優惠的權利，恕不另行通知。 j. 如有任何爭議，商戶保留此使用優惠之最終決定權。 獎賞領取方式 PayKool卡免找數簽賬額 免找數簽賬額將於PayKool卡獲批後一個月內存入客戶的PayKool卡賬戶。 一般條款及細則 全新客戶定義 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。 合資格簽賬 合資格簽賬只包括所有已入賬之本地及 / 或海外零售購物金額及 / 或網上消費零售購物金額，並不包括（但不限於）以下類別的消費或單據： a. 現金透支金額、信用卡費用（包括年費、利息 / 財務費用、逾期費用、超逾信用額手續費、現金透支手續費及其他費用）、賭場交易金額、任何金錢 / 電子貨幣轉賬（包括但不只限於個人對個人(P2P)支付服務或流動裝置/應用程式/電子轉賬平台）/充值電子錢包、優惠套現金額、現金分期、分期金額、未入賬 / 取消 / 退回 / 偽造之交易金額及所有未經授權之交易金額； b. 任何重印單據、單據之影印副本、分拆之單據及手寫單據； c. 本公司不時決定的任何其他消費或單據類別。 指定商戶消費獎賞適用於手機流動支付簽賬 (Apple Pay, Google Pay™)，但不適用於任何電子錢包簽賬之交易 (包括但不限於支付寶)。 客戶責任 客戶須於付款前聲明享用有關優惠。 如有任何爭議，客戶必須提供有關之文件之正本、交易單據及信用卡簽賬存根正本(如適用)以便本公司作進一步調查。 有關獎賞不可退回、轉讓/轉售、兌換現金或換取其他優惠。如有遺失、失效或逾期，恕不獲補發。 若合資格客戶於得到有關獎賞後一年內取消PayKool卡，將會被收取PayKool卡年費 HK$1,800。 本公司保留給予客戶此優惠之權利，客戶於PayKool卡生效後，PayKool卡戶口須於發放此優惠前維持良好狀況，包括但不限於沒有逾期還款紀錄、未有逾額情況或任何違反信用卡持卡人合約條款的行為。否則，本公司保留對客戶撤回此優惠之獲得權利而毋須事先通知。 免

## Refresh
`python extract_paykool_terms.py --split --skills-dir skills`