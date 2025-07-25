from config import DISCORD_WEBHOOK, FLIGHTS_API_KEY
from modules import news, travel_alerts, flights, forex, adiz
from utils.discord import send_to_discord
from utils.content import handle_content

def main():
    status, header, sections = [], [], []
    
    for module in [travel_alerts, adiz, forex]:
        sections.append(handle_content(status, header, module.run()))
        
    if FLIGHTS_API_KEY:
        flights_section = handle_content(status, header, flights.run(FLIGHTS_API_KEY))
        sections.append(flights_section)
    else:
        flights_section = ""
        
    news_section = handle_content([], [], news.run())
    sections.append(news_section)
    
    report_status = "".join(status) or "✅☮️"
    report_header = f'> {" | ".join(header)}' if header else ''
    report_body = "\n\n".join(sections)
    report_footer = "### 備註\n>>> - ⚠️：稍有異常，注意總體狀況交叉比對\n - 🚨：嚴重異常，提高警覺隨時做好準備\n - 🐞：模組報錯，需要修復，Fork者可等待修復後使用 `Sync fork` 更新\n - 新聞數量不會有警告"
    report = f'{report_status}\n{report_header}\n\n{report_body}\n\n{report_footer}'

    send_to_discord(report, DISCORD_WEBHOOK)

if __name__ == "__main__":
    main()
