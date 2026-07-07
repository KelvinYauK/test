# Skill: Apple Pay FAQ

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
- URL: https://www.paykool.hk/promotions/apple-pay
- Slug: apple-pay
- Promotion period: Not detected
- Invite code: Not detected
- New customer definition: Not detected
- Spend requirement: Not detected
- Reward summary: 迎新獎賞」推廣優惠之條款及細則 PayKool信用卡「PayKool x Apple Pay加卡賞」推廣活動條款及細則（「本條款及細則」) PayKool Visa Platinum卡「PayKool x Bar Pacific迎新獎賞」及「Pay
- Voucher validity: Not detected
- Customer responsibility: Not detected

## Source Excerpt
條款及細則約束。 常見疑問 問：我的 PayKool 卡能用Apple Pay嗎? 答：PayKool Visa Platinum 卡可以使用 Apple Pay 問：使用 Apple Pay 會額外收費嗎? 答：我們不會因你使用 Apple Pay 而收費。 問：什麼設備能使用 Apple Pay ? 答：有關可使用 Apple Pay 之裝置，請瀏覽 www.apple.com/apple-pay/ ◊ 免責聲明 透過更多瀏覽器以 Apple Pay 付款： 適用於兼容瀏覽器上的參與商户。兼容的瀏覽器需要 WebSocket 支援。此功能並不是在所有市場提供。須使用符合要求的軟件。要確保你能使用此產品的所有功能，請將你的 iPhone 或 iPad 更新至最新軟件版本。 透過 Apply Pay 分期付款： 貸款並不是由 Apple 提供。須符合資格要求並獲成功批核。並不是在所有市場提供，且未必適用於所有類型的消費，例如訂閱項目及定期交易。透過 Apply Pay 在 iPhone 及 iPad 上提供，適用於網上及 app 內付款。不適用於店內消費。須使用符合要求的軟件。可能有額外條款。有關使用資格與功能詳情，請參閱 support.apple.com/zh-hk/120477 。 透過 Apple Pay 以獎賞付款： 獎賞由你的付款卡提供。交易的全額將於購買時記入你的付款卡，而兌換的獎賞金額將以簽帳回贈方式存入你的帳户。使用此功能須符合資格要求，而此功能並不是在所有市場提供，且未必適用於所有類型的消費，例如訂閱項目及定期交易。Apple 銀包中顯示的可用獎賞餘額及其他資料，可能受互聯網服務等多項因素影響而有所延遲。此功能在 iPhone 及 iPad 上提供，只適用於網上及 app 內付款。不適用於店內消費。須使用符合要求的軟件。有關使用資格及其他功能詳情，請參閱 support.apple.com/zh-hk/120479 。 要使用 Apple Pay，你需要一張由參與的發卡機構所發行，並支援此功能的付款卡。要了解你的付款卡是否兼容 Apple Pay，請聯絡你的發卡機構。 Apple Pay 並不是在所有市場提供。詳情請參閱 apple.com/hk/ios/feature-availability/#apple-wallet-apple-pay 。 功能可能視乎情況改變。部分功能、應用程式/服務未必在所有地區提供或適用於所有語言；可能須使用特定硬件及軟件。詳情請參閱 apple.com/hk/ios/feature-availability/#apple-wallet-apple-pay 。 PayKool 自主分期 想玩唔使等 下載應用程式 PayKool 重要條款及細則 信用卡持有人合約 信用卡申請條款及細則 信用卡登記開立賬戶條款及細則(流動應用程式註冊登記) 信用卡私隱政策及個人資料收集聲明 產品資料概要及財務費用 持卡人爭議交易表格 重要聲明 使用網站及流動應用程式條款及細則 電子直接付款授權 (自動轉賬 )條款及細則 電子直通整合程序條款及細則 新卡注意事項 信用卡分期服務條款及細則 網上保安提示 積分獎賞計劃 (PayKool Point) 條款及細則 流動支付服務條款及細則 「Fun K 易」現金分期服務條款及細則 「邀請碼」推廣優惠之條款及細則 PayKool會員計劃條款及細則 關於《個人資料（私隱）條例》（「條例」）致客戶通知 （「通知」） PayKool Visa Platinum卡「特選客戶優惠」推廣優惠之條款及細則 PayKool Visa Platinum卡 x Trip.com推廣優惠之條款及細則 PayKool Visa Platinum卡「PayKool x 嘉聯車行 迎新獎賞」推廣優惠之條款及細則 PayKool信用卡「PayKool x Apple Pay加卡賞」推廣活動條款及細則（「本條款及細則」) PayKool Visa Platinum卡「PayKool x Bar Pacific迎新獎賞」及「PayKool 客戶專屬獎賞」 推廣優惠之條款及細則（「本條款及細則」） PayKool Visa Platinum卡「PayKool x 基督教家庭服務中心 （CFSC）迎新獎賞

## Refresh
`python extract_paykool_terms.py --split --skills-dir skills`