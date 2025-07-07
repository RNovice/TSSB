import requests, re
from bs4 import BeautifulSoup

def run():
    result = {
        "name": "美國對台旅遊建議",
        "symbol": "🌏",
        "status": "",
        "header": "☮️",
        "content": "模組異常"
    }
    try:
        url = "https://travel.state.gov/content/travel/en/traveladvisories/traveladvisories/new-caledonia-travel-advisory.html"
        headers = {"User-Agent": "Mozilla/5.0"}

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise Exception(f"URL error, status code: {response.status_code}")

        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.find("h3", class_="tsg-rwd-emergency-alertheader-title")
        text = title.get_text(strip=True) if title else None
        if not text:
            raise Exception("title not found")
        
        match = re.search(r'Level (\d+):', text)
        if match:
            level = int(match.group(1))
        else:
            raise ValueError("title format did't match")
        
        if level not in [1, 2, 3, 4]:
                raise ValueError("unknown advisory level", level) 
        if level == 1:
            result["content"] = f"{level}級，一切正常 \n{text}"
        else:
            result.update({
                "status": "🚨",
                "header": "🚨",
                "content": f"{level}級，{'狀態反常，需高度警覺' if level == 2 else '高度危險'} \n{text}"
            })

    except Exception as e:
        result.update({
            "status": "🐞",
            "header": "🐞",
            "content": f"module error, please fix the bug \n{e}"
        })
        
    return result

if __name__ == "__main__":
    print(run())
