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
    report = f'{report_status}\n{report_header}\n\n{report_body}'

    send_to_discord(report, DISCORD_WEBHOOK)

if __name__ == "__main__":
    main()
