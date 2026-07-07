# Skill: 🔧「 PayKool × 裝修佬」信用卡迎新及持卡人專屬優惠 ✨

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
- URL: https://www.paykool.hk/promotions/ppdeco
- Slug: ppdeco
- Promotion period: 2026年3月20日至2026年6月19日(包括首尾兩日) (「推廣期」)
- Invite code: PPDECO
- New customer definition: 全新客戶定義 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: Not detected
- Reward summary: 迎新獎賞 要求及資格： a. 推廣期內，全新客戶以指定邀請碼「PPDECO」申請PayKool信用卡，客戶成功批核後14天內可於PayKool手機應用程式內的「禮遇」活動頁面，使用電子換領券於裝修佬指定換領地點及時間換領由裝修佬提供的「WORX 威
- Voucher validity: 有效期：即日至2026年6月19日 b. 於推廣期內只限使用一次
- Customer responsibility: 客戶責任 客戶須於付款前聲明享用有關優惠。 如有任何爭議，客戶必須提供有關之文件之正本、交易單據及信用卡簽賬存根正本(如適用)以便本公司作進一步調查。 有關獎賞不可退回、轉讓/轉售、兌換現金或換取其他優惠。如有遺失、失效或逾期，恕不獲補發。 若合資格客戶於得到有關獎賞後一年內取消PayKool卡，將會被收取PayKool卡年費 HK$1,800。 本公司保留給予客戶此優惠之權利，客戶於PayKool卡生效後，PayKool卡戶口須於發放此優惠前維持良好狀況，包括但不限於沒有逾期還款紀錄、未有逾額情況或任何違反信用卡持卡人合約條款的行為。否則，本公司保留對客戶撤回此優惠之獲得權利而毋須事先通知。

## Source Excerpt
條款及細則約束 立即申請 PayKool 信用卡 [PayKool x 裝修佬]優惠– PayKool信用卡迎新推廣及持卡人禮遇(「本推廣活動」)之條款及細則 任何人士參與 K Cash Limited（「本公司」）旗下 PayKool 信用卡品牌與 裝修佬（「商戶」）聯合推出的本推廣活動，即表示已充分了解並同意受本條款及細則的約束。 本推廣活動只適用於持有本公司發行之PayKool Visa Platinum卡（「PayKool卡」）之客戶。 優惠推廣期 除特別註明外，優惠推廣期由2026年3月20日至2026年6月19日(包括首尾兩日) (「推廣期」)。 優惠詳情 PayKool迎新獎賞 要求及資格： a. 推廣期內，全新客戶以指定邀請碼「PPDECO」申請PayKool信用卡，客戶成功批核後14天內可於PayKool手機應用程式內的「禮遇」活動頁面，使用電子換領券於裝修佬指定換領地點及時間換領由裝修佬提供的「WORX 威克士 – 4V電動起子電批(索頭) WX242 」一支 (「指定禮品」)。 b. 推廣期內，合資格客戶只可領取PayKool迎新獎賞指定禮品最多一次。 c. 換領指定禮品受其條款及細則約束。 d. 商戶指定換領地點： - 香港九龍荔枝角永康街63號Global Gateway Tower 3樓303室 e. 商戶指定換領時間 (請於PayKool信用卡成功批核的14天內換領)： - 商戶辦公時間：星期一至星期五：10:00 - 18:00（公眾假期除外） - 裝修佬《家居維修DIY班》上堂期間：10:00 - 18:00 持卡人禮遇：指定商戶精彩禮遇 要求及資格： a. 推廣期內，PayKool信用卡持卡人報讀裝修佬《家居維修DIY班》，使用PayKool持卡人優惠碼可享85折優惠。 b. 客戶在PayKool手機應用程式內的「禮遇」活動頁面領取相關電子優惠券後，頁面將顯示PayKool持卡人優惠碼。於報讀裝修佬《家居維修DIY班》時，在報名表的「優惠碼」欄位填寫PayKool持卡人優惠碼，可享上述折扣優惠。 c. 推廣期內，合資格客戶可享指定商戶精彩禮遇一次。 d. 裝修佬《家居維修DIY班》課程連結：https://deco-academy.com/diy e. 禮遇由裝修佬提供，受裝修佬條款及細則約束。 f. 本公司及裝修佬保留隨時修改或終止本優惠的權利，恕不另行通知。 迎新獎賞換領方式 PayKool迎新獎賞指定禮品換領方式： a. 客戶須於PayKool信用卡成功批核的14天內，於裝修佬指定換領地點及時間，出示PayKool 手機應用程式內有效的電子換領券，換領流程如下： i. 開啟 PayKool 手機應用程式 > 禮遇 > 我的禮遇，選取相關電子換領券； ii. 按下「立即領取」按鈕； iii. 即場掃描由裝修佬職員提供的指定二維碼； iv. 成功驗證將顯示「兌換成功」 (「驗證成功畫面」)； v. 驗證成功後，職員會向客戶提供指定禮品，並由職員拍攝禮品及驗證成功畫面以作記錄。 商戶(電子)優惠券 裝修佬《家居維修DIY班》電子優惠券領取及使用方式： a. 客戶在PayKool手機應用程式內的「禮遇」活動頁面領取相關電子優惠券後，頁面將顯示PayKool持卡人優惠碼。於報讀裝修佬《家居維修DIY班》時，在報名表的「優惠碼」欄位填寫PayKool持卡人優惠碼，可享折扣優惠，使用流程如下： i. 報名前請開啟 PayKool 手機應用程式 > 禮遇，選取相關電子優惠券； ii. 按下「立即領取」按鈕； iii. 頁面將顯示PayKool持卡人優惠碼； iv. 於報讀裝修佬《家居維修DIY班》時，在報名表的「優惠碼」欄位填寫PayKool持卡人優惠碼，可享折扣優惠。 優惠條款及細則 PayKool迎新獎賞指定禮品換領條款及細則包括： a. 客戶須於PayKool信用卡成功批核的14天內換領指定禮品，逾期將不獲補領。 b. 此券只限使用一次。 c. 此券不能兌換現金及不設找贖。 d. 指定禮品由裝修佬提供。數量有限，送完即止。 e. 如有任何爭議，裝修佬保留此使用優惠之最終決定權。 裝修佬《家居維修DIY班》電子優惠券使用條款包括： a. 電子優惠券有效期：即日至2026年6月19日 b. 於推廣期內只限使

## Refresh
`python extract_paykool_terms.py --split --skills-dir skills`