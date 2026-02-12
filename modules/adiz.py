import requests, re, urllib3
from bs4 import BeautifulSoup


def run():
    result = {
        "name": "中國軍機、軍艦動態",
        "symbol": "🛰️",
        "status": "",
        "header": "☮️",
        "content": "模組異常"
    }
    try:
        try:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            BASE = "https://www.mnd.gov.tw"

            res = requests.get(f"{BASE}/news/plaactlist", verify=False)
            res.encoding = "utf-8"
            soup = BeautifulSoup(res.text, "html.parser")

            target_a = next(
                (a for a in soup.find_all("a", class_="news_list")
                if a.find("div", class_="title") and "海、空域動態" in a.find("div", class_="title").text)
            , None)
            if target_a is None:
                raise Exception("target_a not found")
            
            latest = target_a.get("href")

            url = f"{BASE}/{latest}"

            art_res = requests.get(url, verify=False)
            art_res.encoding = "utf-8"
            art_soup = BeautifulSoup(art_res.text, "html.parser")

            p_list = art_soup.select("div.maincontent p")
            news_content = next((p.text for p in p_list if "活動動態" in p.text), None)
            if news_content is None:
                raise Exception("news content '活動動態' not matched")

        except Exception as e:
            raise Exception(f"BeautifulSoup error, {str(e)}")
            
        
        match = re.search(r'共機(\d+)架', news_content)
        aircraft = int(match.group(1)) if match else None
        match2 = re.search(r'共艦(\d+)艘', news_content)
        ship = int(match2.group(1)) if match2 else None
        
        content = "一切正常。"
        
        if aircraft and aircraft > 70 or ship and ship > 30:
            result.update({
                "status": "🚨",
                "header": "🚨",
            })
            content = "共機/艦數量反常，需高度警覺。"
        elif aircraft and aircraft > 40 or ship and ship > 15:
            result.update({
                "status": "⚠️",
                "header": "⚠️",
            })
            content = "共機/艦數量較多。"
        
        content += f"共機{aircraft}架、" if aircraft is not None else "沒有共機數量、" 
        content += f"共艦{ship}艘" if ship is not None else "沒有共艦數量"
            
        formatted_raw_content = news_content.replace('二、','').replace('\r','').rstrip()
        result["content"] = content + f" \n{formatted_raw_content} \n[資料來源](<{url}>)"

    except Exception as e:
        result.update({
            "status": "🐞",
            "header": "🐞",
            "content": f"module error, please fix the bug \n{str(e)[:200]}"
        })
        
    return result

if __name__ == "__main__":
    print(run())
