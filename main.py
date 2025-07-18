from config import DISCORD_WEBHOOK, FLIGHTS_API_KEY
from modules import evacuation, news, travel_alerts, flights, forex, adiz
from utils.discord import send_to_discord
from utils.content import handle_content

def main():
    status = []
    header = []
    sections = []
    
    travel_section = handle_content(status, header, travel_alerts.run())
    sections.append(travel_section)
    adiz_section = handle_content(status, header, adiz.run())
    sections.append(adiz_section)
    if FLIGHTS_API_KEY:
        flights_section = handle_content(status, header, flights.run(FLIGHTS_API_KEY))
        sections.append(flights_section)
    else:
        flights_section = ""
    
    forex_section = handle_content(status, header, forex.run())
    sections.append(forex_section)
        
    news_section = handle_content([], [], news.run())
    sections.append(news_section)
    
    status = "".join(status)
    section_content = "\n\n".join(sections)
    if len(status) == 0: status = "✅☮️"
    report = f'{status}\n> {" | ".join(header)}\n\n{section_content}'

    send_to_discord(report, DISCORD_WEBHOOK)

if __name__ == "__main__":
    main()
