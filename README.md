[中文指南](README.zh.md)

## Fork for GitHub action automation

--

## Local usage

> may use python3 & pip3 in different os

optional venv：

```
python -m venv env
# Linux, macOS
env\bin\activate
# Windows
env\Scripts\activate
```

setup `.env` file：

```
DISCORD_WEBHOOK={{your discord webhooks url}}
FLIGHTS_API_KEY={{your aviationstack api key}}
```

run scripts：

```
pip install -r requirements.txt
python main.py
```

## Analyze source

- U.S. DEPARTMENT of STATE - [Travel.State.Gov](https://travel.state.gov/content/travel.html)
- Aviationstack Global Aviation Data - [Aviationstack](https://aviationstack.com)
- Taiwan Ministry of National Defense - [mnd.gov.tw](https://www.mnd.gov.tw/)
- fawazahmed0/exchange-api - [currency-api](https://github.com/fawazahmed0/exchange-api)
- Google News - [news.google.com](https://news.google.com/)
