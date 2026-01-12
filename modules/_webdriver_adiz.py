import re, time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

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
            options = Options()
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")

            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)

            try:
                driver.get("https://www.mnd.gov.tw/news/plaactlist")
            except: raise Exception("URL error")
            time.sleep(5)
            try:
                driver.find_element(By.XPATH, '//div[@class="news_list_box"]//*[contains(text(), "海、空域動態")]').click()
            except: raise Exception("news title not found")
            time.sleep(5)
            url = driver.current_url
            try:
                news_content_ele = driver.find_element(By.XPATH, '//p[contains(text(), "活動動態")]')
                news_content = news_content_ele.text
            except: raise Exception("news content not matched")

            driver.quit()
        except Exception as e:
            raise Exception(f"selenium error, {str(e)}")
            
        
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
            
        result["content"] = content + f" \n{news_content.replace('二、','').rstrip()} \n[資料來源](<{url}>)"

    except Exception as e:
        result.update({
            "status": "🐞",
            "header": "🐞",
            "content": f"module error, please fix the bug \n{str(e)[:200]}"
        })
        
    return result

if __name__ == "__main__":
    print(run())
