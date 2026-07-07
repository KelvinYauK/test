# Skill: 【☕ PayKool 全新客戶專享 Starbucks電子現金禮券｜全新客戶迎新及簽賬獎賞 🎁】

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
- URL: https://www.paykool.hk/promotions/Starbucks2026
- Slug: Starbucks2026
- Promotion period: 2026年7月6日至2026年12月31日(包括首尾兩日) (「推廣期」)
- Invite code: PPSB
- New customer definition: 全新客戶定義 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: 單一簽賬或增值滿 HK$100
- Reward summary: 可獲高達HK$500的Starbucks電子現金禮券
- Voucher validity: 有效日期至2027年7月31日
- Customer responsibility: 客戶責任 客戶須於付款前聲明享用有關優惠。 如有任何爭議，客戶必須提供有關之文件之正本、交易單據及信用卡簽賬存根正本(如適用)以便本公司作進一步調查。 有關獎賞不可退回、轉讓/轉售、兌換現金或換取其他優惠。如有遺失、失效或逾期，恕不獲補發。 若合資格客戶於得到有關獎賞後一年內取消PayKool卡，將會被收取PayKool卡年費 HK$1,800。 本公司保留給予客戶此優惠之權利，客戶於PayKool卡生效後，PayKool卡戶口須於發放此優惠前維持良好狀況，包括但不限於沒有逾期還款紀錄、未有逾額情況或任何違反信用卡持卡人合約條款的行為。否則，本公司保留對客戶撤回此優惠之獲得權利而毋須事先通知。

## Source Excerpt
條款及細則約束 📲 立即申請 PayKool 信用卡享受各種專屬優惠啦！ 立即申請 PayKool 信用卡 [PayKool全新客戶專享 Starbucks電子現金禮券 ]– PayKool信用卡迎新及簽賬獎賞推廣(「本推廣活動」)之條款及細則 任何人士參與 K Cash Limited（「本公司」）旗下 PayKool 信用卡品牌與 Starbucks（「商戶」）推出的本推廣活動，即表示已充分了解並同意受本條款及細則的約束。 本推廣活動優惠只適用於持有本公司發行之PayKool Visa Platinum卡（「PayKool卡」）之客戶。 優惠推廣期 除特別註明外，優惠推廣期由2026年7月6日至2026年12月31日(包括首尾兩日) (「推廣期」)。 優惠詳情 迎新推廣：PayKool迎新及簽賬獎賞 要求及資格： a) 推廣期內，全新客戶以指定邀請碼「PPSB」(「指定邀請碼」)申請PayKool 信用卡，成功獲批並完成指定簽賬要求後，可獲高達HK$500的Starbucks電子現金禮券。 i. 迎新獎賞: 推廣期內使用指定邀請碼申請PayKool信用卡並成功獲批之全新客戶可獲HK$400 Starbucks電子現金禮券(合共 8 張HK$50 Starbucks電子現金禮券)，客戶可以在PayKool手機應用程式內的「禮遇」活動頁面查閱電子禮券。 ii. 簽賬獎賞: 上述合資格全新客戶成功獲批PayKool 信用卡後1個月內，於Starbucks分店或Starbucks手機應用程式以PayKool信用卡單一簽賬或增值滿 HK$100(「指定簽賬要求」)，可獲額外HK$100 Starbucks 電子現金禮券 (合共 2 張 Starbucks HK$50 電子現金禮券)。電子禮券將於完成指定簽賬要求後的下1個月內存入客戶的PayKool手機應用程式內的「禮遇」活動頁面。 b) 合資格客戶只可獲得PayKool迎新獎賞及簽賬獎賞各最多1次。 c) 使用Starbucks電子現金禮券受其條款及細則約束。 獎賞領取方式 商戶電子現金禮券 Starbucks電子現金禮券領取及使用方式： 客戶須於付款前向Starbucks職員出示電子現金禮券二維碼，使用流程如下： i. 開啟 PayKool 手機應用程式 > 禮遇 > 我的禮遇，選取相關電子現金禮券； ii. 按下「立即領取」按鈕； iii. 按下「使用Starbucks電子現金禮券」按鈕，將開啟Starbucks電子現金禮券連結； iv. 於付款前向Starbucks職員出示Starbucks電子現金禮券二維碼。 商戶電子現金禮券條款及細則 Starbucks 電子現金禮券(「電子禮券」)使用條款及細則包括(但不限於)： • 電子禮券有效日期至2027年7月31日。 • 電子禮券只限在香港或澳門之星巴克分店使用一次 (香港迪士尼樂園分店除外) 。 • 電子禮券不適用於香港或澳門之星巴克 ‘We Proudly Serve Starbucks’ 櫃檯 。 • 電子禮券不能兌換現金，並恕不找續 。 • 電子禮券不能用作啟用或增值星巴克卡、八達通卡及澳門通卡 。 • 電子禮券不適用於購買任何星巴克禮券產品 。 • 只接受電子禮券的電子版本，列印版本或截圖恕不接受 。 • 電子禮券不能轉售予他人 。 • 電子禮券如遭損壞或遺失，Coffee Concepts (HK) Ltd. 及 Coffee Concepts (Macau) Ltd. 恕不負責 。 • Coffee Concepts (HK) Ltd. 及 Coffee Concepts (Macau) Ltd. 保留更改有關使用此電子禮券條款及細則的決定權。 一般條款及細則 全新客戶定義 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。 合資格簽賬 合資格簽賬只包括所有已入賬之本地及 / 或海外零售購物金額及 / 或網上消費零售購物金額，並不包括（但不限於）以下類別的消費或單據： a) 現金透支金額、信用卡費用（包括年費、利息 / 財務費用、逾期費用、超逾信用額手續費、現金透支手續費及其他費用）、賭場交易金額、任何金錢 / 電子貨幣轉賬（包括但不只限於個人對個人(P2P)支付服務或流動裝

## Refresh
`python extract_paykool_terms.py --split --skills-dir skills`