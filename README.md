# Auto Assistant Bot

Auto Assistant 是一個以 Flask 架構為基礎的聊天機器人整合平台，支援 Slack 與 LINE Bot，能接收頻道訊息與私訊，並具備良好的模組化分層設計，方便擴充智慧回應（如串接大語言模型）。

---

## 🚀 功能特性
- ✅ 接收 Slack 頻道與私訊訊息
- ✅ 接收 LINE 頻道訊息
- ✅ 使用 Slack `chat.postMessage` 回應訊息
- ✅ 使用 LINE Messaging API 回覆訊息
- ✅ 分層設計（routes / handlers / services）
- ✅ Slack webhook 支援 `url_verification` 驗證
- ✅ 可擴充支援圖片、影片、語音等媒體格式

---

## 📦 專案結構

```
auto-assistant/
├── app/
│   ├── routes/
│   │   └── webhooks/
│   │       ├── __init__.py              # Webhook 路由初始化
│   │       ├── line_webhook.py          # LINE Webhook 路由
│   │       ├── slack_webhook.py         # Slack Webhook 路由
│   ├── services/
│   │   ├── line_service.py              # LINE 發送訊息服務
│   │   └── slack_service.py             # Slack 發送訊息服務
│   ├── webhook_handlers/
│   │   ├── line_handler.py              # LINE 訊息處理器
│   │   └── slack_handler.py             # Slack 訊息處理器
│   ├── config.py                        # 設定檔讀取與管理
│   └── __init__.py                      # 建立 Flask App 並註冊 Blueprint
├── static/                              # 靜態檔案
│   ├── profile.png                      # Bot 頭像
├── requirements.txt                     # 套件需求檔
├── config.ini                           # 設定檔
├── run.py                               # 啟動入口點
```

---

## ⚙️ 安裝與啟動

```bash
# 安裝套件
pip install -r requirements.txt

# 建立設定檔
cp config.sample.ini config.ini
```

---

## 🔐 config.ini 範例

```ini
[Line]
CHANNEL_SECRET = your-line-channel-secret
CHANNEL_ACCESS_TOKEN = your-line-access-token

[Slack]
SLACK_BOT_TOKEN = xoxb-your-slack-bot-token
SLACK_SIGNING_SECRET = your-slack-signing-secret


```

---

## 🧪 本地測試與開發

```bash
python run.py
ngrok http 5001  # 曝露本機 port 給 Slack / LINE webhook
```

Webhook 設定請填入：
```
# Slack
https://xxxx.ngrok-free.app/api/webhooks/slack/message

# LINE
https://xxxx.ngrok-free.app/api/webhooks/line
```

---

## ✅ Slack App 權限建議
> 請到 Slack App → OAuth & Permissions → Scopes → Bot Token Scopes 加入下列權限：

| Scope               | 用途                 |
|--------------------|----------------------|
| `chat:write`       | 發送訊息             |
| `app_mentions:read`| 接收被 @ 提及事件     |
| `message.im`       | 接收私訊事件         |
| `channels:history` | 讀取公開頻道歷史訊息 |
| `im:history`       | 讀取私訊歷史訊息     |

⚠️ 加完 scope 後記得點「Reinstall to Workspace」讓權限生效

---

## 🔧 待辦 / 擴充項目
- [ ] 串接大語言模型（OpenAI / Claude / Gemini）
- [ ] 自動圖片 / 音訊回覆
- [ ] 資料庫記錄訊息紀錄與補償機制
- [ ] 加入通知提醒、背景任務等進階功能

---

## 🤝 貢獻與協作
歡迎任何開發者一同參與，共同打造多平台整合的 AI 助理 ✨

---

> 如需更多功能（圖文模板、按鈕互動、LLM 整合），請參考 `app/services/` 中的實作方向，或提 issue 與我討論。

