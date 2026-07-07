# Skill: 🏠 PayKool x at.home｜迎新獎賞及持卡人專屬禮遇 ✨

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
- URL: https://www.paykool.hk/promotions/athome
- Slug: athome
- Promotion period: 2026年5月22日至2026年8月21日(包括首尾兩日) (「推廣期」)
- Invite code: PPHOME
- New customer definition: 全新客戶定義 9. 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。
- Spend requirement: Not detected
- Reward summary: 迎新獎賞 4. 要求及資格： a) 推廣期內，全新客戶以指定邀請碼「PPHOME」申請PayKool 信用卡，成功批核後可獲得以下迎新獎賞： i. at.home HK$400 電子折扣券 : 全新客戶可在 PayKool 手機應用程式內的「禮遇」
- Voucher validity: 有效日期至2026年8月31日
- Customer responsibility: 客戶責任 12. 客戶須於付款前聲明享用有關優惠，並以PayKool卡全數簽賬方可享優惠。 13. 如有任何爭議，客戶必須提供有關之文件之正本、交易單據及信用卡簽賬存根正本(如適用)以便本公司作進一步調查。 14. 有關獎賞不可退回、轉讓/轉售、兌換折扣或換取其他優惠。如有遺失、失效或逾期，恕不獲補發。 15. 若合資格客戶於得到有關獎賞後一年內取消PayKool卡，將會被收取PayKool卡年費 HK$1,800。 16. 本公司保留給予客戶此優惠之權利，客戶於PayKool卡生效後，PayKool卡戶口須於發放此優惠前維持良好狀況，包括但不限於沒有逾期還款紀錄、未有逾額情況或任何違反信用卡持卡人合約條款的行為。否則，本公司保留對客戶撤回此優惠之獲得權利而毋須事先通知。

## Source Excerpt
條款及細則約束 立即申請 PayKool 信用卡 [PayKool x at.home]優惠– PayKool信用卡迎新推廣及持卡人禮遇(「本推廣活動」)之條款及細則 任何人士參與 K Cash Limited（「本公司」）旗下 PayKool 信用卡品牌與 at.home（「商戶」）聯合推出的本推廣活動，即表示已充分了解並同意受本條款及細則的約束。 本推廣活動優惠只適用於持有本公司發行之PayKool Visa Platinum卡（「PayKool卡」）之客戶。 優惠推廣期 3. 除特別註明外，優惠推廣期由2026年5月22日至2026年8月21日(包括首尾兩日) (「推廣期」)。 優惠詳情 迎新推廣：PayKool迎新獎賞 4. 要求及資格： a) 推廣期內，全新客戶以指定邀請碼「PPHOME」申請PayKool 信用卡，成功批核後可獲得以下迎新獎賞： i. at.home HK$400 電子折扣券 : 全新客戶可在 PayKool 手機應用程式內的「禮遇」活動頁面，領取 at.home 的 HK$400 電子折扣券(「電子折扣券」)一張，於 at.home 分店單一消費總金額滿HK$1,000，並以PayKool信用卡簽賬，即可使用電子折扣券。經at.home職員成功驗證電子折扣券，可獲全單即減HK$400。 b) 合資格客戶只可獲得PayKool迎新獎賞最多1次。 c) 使用商戶電子折扣券受其條款及細則約束。 持卡人禮遇：指定商戶精彩禮遇 5. 要求及資格： a) 推廣期內，PayKool 信用卡客戶於 at.home分店購買傢俬家品滿HK$2,888並以PayKool信用卡簽賬，即可享全單減HK$188優惠。 b) 優惠由商戶提供，並受商戶條款約束。 迎新獎賞領取方式 商戶電子折扣券 6. at.home電子折扣券領取及使用方式： 客戶須於at.home分店單一消費總金額滿HK$1,000，付款前出示PayKool 手機應用程式內有效的電子折扣券，並由at.home職員驗證兌換資格後才可使用。驗證流程如下： i. 付款前請開啟 PayKool 手機應用程式 > 禮遇 > 我的禮遇，選取相關電子折扣券； ii. 按下「立即領取」按鈕； iii. 即場掃描由at.home職員提供的指定二維碼； iv. 成功驗證將顯示「兌換成功」 (「驗證成功畫面」)； v. 驗證成功後，at.home職員將記錄驗證成功畫面上的「兌換編號」。客戶以PayKool信用卡簽賬可即時獲HK$400 折扣。完成簽賬後，at.home職員將於發票及電子貨幣付款存根蓋印，並拍照備份以作紀錄。 商戶電子折扣券條款及細則 7. at.home 電子折扣券使用條款及細則包括(但不限於)： • 電子折扣券有效日期至2026年8月31日。 • 電子折扣券只適用於at.home分店。 • 電子折扣券只限使用一次。 • 每一單交易只限使用最多一張電子折扣券。 • 電子折扣券不可與at.home其他推廣優惠、優惠券及現金券同時使用。 • 電子折扣券僅適用於全額付款或首筆訂金之支付；恕不接受於支付餘額時使用。 • 如有任何因網絡、電話、技術或不可歸責於at.home之事由，而導致不能使用電子折扣券，at.home概不負責。 • 電子折扣券條款及細則如有更改，恕不另行通知。 • 電子折扣券於有效日期後無效並不能使用，亦不會獲補發或延期。 • 如有任何爭議，at.home保留最終使用決定權。 持卡人禮遇條款及細則 8. 優惠條款及細則包括(但不限於)： • 此優惠有效期由2026年5月22日至2026年8月21日，逾期無效。 • 此優惠不適用於寄賣貨品及禮券。 • 此優惠適用於減價貨品，但不適用於折扣超過5折之貨品。 • 此優惠不可與任何其他推廣優惠、優惠券及現金券同時使用 (包括不可與PayKool迎新獎賞HK$400電子折扣券一同使用)。 • 每一次交易及每一個送貨地址只可以使用此優惠一次。 • 必須於購物時以PayKool信用卡簽賬方可享此優惠。 • 如有任何爭議，at.home將保留最終決定權。 一般條款及細則 全新客戶定義 9. 全新客戶定義為申請日起計過去12個月內並沒有於本公司申請（不論成功申請與否）或擁有任何信用卡賬戶。 合資格簽賬 10. 合資格簽賬只包括所有已

## Refresh
`python extract_paykool_terms.py --split --skills-dir skills`