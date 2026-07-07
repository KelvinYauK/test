# Skill: PayKool x 冒險樂園🎡｜PayKool信用卡迎新獎賞及持卡人專屬禮遇 ✨

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
- URL: https://www.paykool.hk/promotions/jumpingym
- Slug: jumpingym
- Promotion period: 2026年6月1日至2027年5月31日(包括首尾兩日) (「推廣期」)
- Invite code: JG
- New customer definition: 全新客戶定義 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: Not detected
- Reward summary: 迎新獎賞 要求及資格： a) 推廣期內，全新客戶以指定邀請碼「JG」申請PayKool 信用卡，成功批核後可獲得以下迎新獎賞： i. 冒險樂園代幣400個：全新客戶可在 PayKool 手機應用程式內的「禮遇」活動頁面，領取冒險樂園代幣電子禮券（「
- Voucher validity: 有效日期至2027年11月30日
- Customer responsibility: 客戶責任 客戶須於付款前聲明享用有關優惠，並以PayKool卡全數簽賬方可享優惠。 如有任何爭議，客戶必須提供有關之文件之正本、交易單據及信用卡簽賬存根正本(如適用)以便本公司作進一步調查。 有關獎賞不可退回、轉讓/轉售、兌換折扣或換取其他優惠。如有遺失、失效或逾期，恕不獲補發。 若合資格客戶於得到有關獎賞後一年內取消PayKool卡，將會被收取PayKool卡年費 HK$1,800。 本公司保留給予客戶此優惠之權利，客戶於PayKool卡生效後，PayKool卡戶口須於發放此優惠前維持良好狀況，包括但不限於沒有逾期還款紀錄、未有逾額情況或任何違反信用卡持卡人合約條款的行為。否則，本公司保留對客戶撤回此優惠之獲得權利而毋須事先通知。

## Source Excerpt
條款及細則約束 立即申請 PayKool 信用卡 📋 [PayKool x 冒險樂園]優惠– PayKool信用卡迎新推廣及持卡人禮遇(「本推廣活動」)之條款及細則 任何人士參與 K Cash Limited（「本公司」）旗下 PayKool 信用卡品牌與 冒險樂園（「商戶」）聯合推出的本推廣活動，即表示已充分了解並同意受本條款及細則的約束。 本推廣活動優惠只適用於持有本公司發行之PayKool Visa Platinum卡（「PayKool卡」）之客戶。 優惠推廣期 除特別註明外，優惠推廣期由2026年6月1日至2027年5月31日(包括首尾兩日) (「推廣期」)。 優惠詳情 迎新推廣：PayKool迎新獎賞 要求及資格： a) 推廣期內，全新客戶以指定邀請碼「JG」申請PayKool 信用卡，成功批核後可獲得以下迎新獎賞： i. 冒險樂園代幣400個：全新客戶可在 PayKool 手機應用程式內的「禮遇」活動頁面，領取冒險樂園代幣電子禮券（「電子禮券」）一張，可於冒險樂園香港任何一間分店使用兌換冒險樂園代幣400個（價值HK$800）。 ii. HK$100免找數簽賬額：於PayKool信用卡成功獲批核後一個月內存入客戶的PayKool信用卡賬戶。 b) 合資格客戶只可獲得PayKool迎新獎賞最多1次。 c) 使用商戶電子禮券受其條款及細則約束。 持卡人禮遇：指定商戶精彩禮遇 要求及資格： a) 由2026年6月1日至2026年12月31日，PayKool 信用卡持卡人於冒險樂園香港任何一間分店以PayKool信用卡簽賬，可以優惠價HK$600購買冒險樂園代幣530個。 b) 優惠由商戶提供，並受商戶條款約束。 迎新獎賞領取方式 商戶電子禮券 冒險樂園代幣電子禮券領取及使用方式： o 客戶須於冒險樂園分店，付款前出示PayKool 手機應用程式內有效的電子禮券，並由冒險樂園職員驗證兌換資格後才可使用。驗證流程如下： i. 付款前請開啟 PayKool 手機應用程式 > 禮遇 > 我的禮遇，選取相關電子禮券； ii. 按下「立即領取」按鈕； iii. 出示二維碼讓冒險樂園職員掃描； iv. 冒險樂園職員在PayKool手機應用程式輸入專屬認證碼; v. 驗證成功後會顯示「兌換成功」，客戶隨即獲得冒險樂園代幣400個。 商戶電子禮券條款及細則 冒險樂園代幣電子禮券使用條款及細則包括(但不限於)： • 電子禮券有效日期至2027年11月30日。 • 電子禮券只適用於冒險樂園分店。 • 電子禮券只限使用一次。 • 每一單交易只限使用最多一張電子禮券。 • 電子禮券不能兌換現金及不設找贖。 • 電子禮券不可與冒險樂園其他推廣優惠、優惠券及現金券同時使用。 • 冒險樂園代幣不適用於部分遊戲，請以店內公佈為準。 • 如有任何因網絡、電話、技術或不可歸責於冒險樂園之事由，而導致不能使用電子禮券，冒險樂園概不負責。 • 電子禮券條款及細則如有更改，恕不另行通知。 • 電子禮券於有效日期後無效並不能使用，亦不會獲補發或延期。 • 如有任何爭議，冒險樂園保留最終使用決定權。 • 電子禮券受冒險樂園之條款及細則約束。 持卡人禮遇條款及細則 優惠條款及細則包括(但不限於)： • 此優惠有效期由2026年6月1日至2026年12月31日，逾期無效。 • 此優惠不適用於購買禮券、現金券及其他指定產品。 • 此優惠不可與其他優惠同時使用 (包括但不限於遊戲卡推廣)。 • 此優惠不能兌換現金及不設找贖。 • 推廣期內每位持卡人不限使用優惠次數。 • 必須於購物時以PayKool信用卡簽賬方可享此優惠。 • 使用優惠購買的貨品或服務不設退款、退貨及更換。 • 此優惠受冒險樂園條款及細則約束。 • 如有任何爭議，冒險樂園將保留最終決定權。 一般條款及細則 全新客戶定義 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。 合資格簽賬 合資格簽賬只包括所有已入賬之本地及 / 或海外零售購物金額及 / 或網上消費零售購物金額，並不包括（但不限於）以下類別的消費或單據： o a) 折扣透支金額、信用卡費用（包括年費、利息 / 財務費用、逾期費用、超逾信用額手續費、折扣透支手續費及其他費用）、賭場交易金額、任何金錢 / 電子貨幣

## Refresh
`python extract_paykool_terms.py --split --skills-dir skills`