## 使用 GitHub action 自動化 (Fork)

--

## 本地運行

> 不同作業系統下可能是 python3 & pip3

虛擬環境(可選)：

```
python -m venv env
# Linux, macOS
env\bin\activate
# Windows
env\Scripts\activate
```

建立 `.env` 檔案：

```
DISCORD_WEBHOOK={{你的 discord webhooks 網址}}
FLIGHTS_API_KEY={{你的 aviationstack api 金鑰}}
```

執行腳本：

```
pip install -r requirements.txt
python main.py
```

## 分析來源

- Aviationstack 全球航空數據 - [Aviationstack](https://aviationstack.com)
- fawazahmed0/exchange-api - [currency-api](https://github.com/fawazahmed0/exchange-api)
- Google 新聞 - [news.google.com](https://news.google.com/)
- 美國國務院 - [Travel.State.Gov](https://travel.state.gov/content/travel.html)
- 台灣國防部 - [mnd.gov.tw](https://www.mnd.gov.tw/)
