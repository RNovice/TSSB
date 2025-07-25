## 自動運行 (雲端自動腳本)

### 事前準備

1. [GitHub](https://github.com/) 帳號 (用來執行自動腳本)
2. [Discord](https://discord.com/app) 帳號和伺服器 (用來接收每日報告)
   - 創建一個伺服器
   - 在伺服器設定中，選**整合**
   - 建立 Webhook，取得 Webhook 網址
3. [Aviationstack](https://aviationstack.com) API 金鑰 (用來查詢航班資訊，若不需要可不準備)
   - 申請一個帳號，選免費的方案就行
   - 表格隨便填個大概就行(~~但帳號密碼要記住~~)
   - 可以在 **Dashboard** 的地方拿到 **API Access Key**

### 使用 GitHub action 自動化 (Fork)

1. [Fork 本專案](https://github.com/RNovice/TSSB/fork)
2. 設定 Secrets（機密變數）：
   - 前往： **Settings** > **Secrets and variables** > **Actions**
   - 新增機密變數：
     - Name: `DISCORD_WEBHOOK`
     - Secret: 填你的 Discord webhook 網址
   - （可選）新增另一個機密變數：
     - Name: `FLIGHTS_API_KEY`
     - Secret: 填你的 aviationstack API 金鑰
   - > FLIGHTS_API_KEY 為選填，若未設置，腳本會自動略過航班資料流程
3. 啟用 GitHub Actions 工作流程：

   - 前往： **Actions**
   - 點選： "I understand my workflows, go ahead and enable them"
   - 找到 **Daily Alert Report**，點選 **Enable workflow**

4. 手動測試流程：
   - 在 **Actions** 頁面中，選擇 **Daily Alert Report**
   - 點選 **Run workflow**，等待執行完畢後查看結果

### 客製化

1. 發送時間
   - 每日 7:00 發送消息，包含運作時間、網路等狀況大約 7:10 ~ 20
   - 更改 [`.github/workflows/daily.yml`](.github/workflows/daily.yml) 中的 `on: schedule: - cron:` 設置時間
   - 格式為 UTC+0 `分 時 日 月 週`，[格式詳細](https://zh.wikipedia.org/zh-tw/Cron)
   ```diff
   # 範例 - 從每日7:00(UTC+8)
   - - cron: "00 23 * * *"
   # 改為每月1號11:11(UTC+8)
   + - cron: "11 3 1 * *"
   ```
2. 中國軍機、軍艦動態
   - 共機數量 > 40 或 共艦數量 > 15 會發警告 ⚠️
   - 共機數量 > 70 或 共艦數量 > 30 會發警報 🚨
   - 可在 [`modules/adiz.py`](modules/adiz.py) 更改
3. 美元對台幣波動
   - 單日漲幅 > 1.5% 或 雙日漲幅 > 2.0% 會發警告 ⚠️
   - 單日漲幅 > 3.0% 或 雙日漲幅 > 4.0% 會發警報 🚨
   - 可在 [`modules/forex.py`](modules/forex.py) 更改
4. 今日飛往桃園機場航班
   - 因為撈取資料的時間不同取得航班數會有差異
     - 有調整發送時間者建議調整航班參考值
   - 總航班數 > 800 或 取消航班數 > 15 會發警告 ⚠️
   - 總航班數 > 600 或 取消航班數 > 30 會發警報 🚨
   - 可在 [`modules/flights.py`](modules/flights.py) 更改

## 本地運行

> 註：不同作業系統可能需使用 `python3` 與 `pip3`

### （可選）建立虛擬環境

```bash
python -m venv env
# macOS/Linux
source env/bin/activate
# Windows
env\Scripts\activate
```

### 設置環境變數

在根目錄建立 .env 檔案：

```env
DISCORD_WEBHOOK={{你的 discord webhooks 網址}}
FLIGHTS_API_KEY={{你的 aviationstack api 金鑰}}
```

> 如果不需要航班數據可以不用 FLIGHTS_API_KEY

### 安裝依賴與執行：

```bash
pip install -r requirements.txt
python main.py
```

## 分析來源

- Aviationstack 全球航空數據 - [Aviationstack](https://aviationstack.com)
- fawazahmed0/exchange-api - [currency-api](https://github.com/fawazahmed0/exchange-api)
- Google 新聞 - [news.google.com](https://news.google.com/)
- 美國國務院 - [Travel.State.Gov](https://travel.state.gov/content/travel.html)
- 台灣國防部 - [mnd.gov.tw](https://www.mnd.gov.tw/)
