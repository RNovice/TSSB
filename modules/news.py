import feedparser

BASE_URL = "https://news.google.com/rss/search"
TIME_FILTER = "when:1d"

REGIONS = [
    {
        "name": "US",
        "keywords": ['Taiwan war', 'Taiwan China conflict', 'PLA invasion', 'Taiwan Strait tensions', 'China attack Taiwan'],
        "locale": "hl=en-US&gl=US&ceid=US:en"
    },
    {
        "name": "JP",
        "keywords": ['台湾戦争', '台湾 中国 紛争', '中国人民解放軍 侵攻', '台湾海峡 緊張', '中国 台湾 攻撃'],
        "locale": "hl=ja&gl=JP&ceid=JP:ja"
    },
    {
        "name": "TW",
        "keywords": ['台灣戰爭', '台灣 中國 衝突', '解放軍 侵略', '台灣海峽 緊張', '中國 攻擊 台灣'],
        "locale": "hl=zh-TW&gl=TW&ceid=TW:zh-Hant"
    }
]

def parse_google_news(query: str, locale: str):
    query_param = f"{query} when:1d".replace(" ", "+")
    return feedparser.parse(f"https://news.google.com/rss/search?q={query_param}&{locale}")

def count_articles(region: dict) -> int:
    return sum(len(parse_google_news(keyword, region["locale"]).entries) for keyword in region["keywords"])

def run():
    result = {
        "name": "台海衝突新聞數量",
        "symbol": "📰",
        "status": "",
        "header": "☮️",
        "content": "模組異常"
    }

    try:
        counts = {region["name"]: count_articles(region) for region in REGIONS}
        result["content"] = (
            f"美國{counts['US']}、日本{counts['JP']}、台灣{counts['TW']}  \n"
            "[資料來源](<https://news.google.com>)"
        )

    except Exception as e:
        result.update({
            "status": "🐞",
            "header": "🐞",
            "content": f"module error, please fix the bug \n{str(e)[:200]}"
        })

    return result

if __name__ == "__main__":
    print(run())
