from config import DISCORD_WEBHOOK, FLIGHTS_API_KEY
from modules import evacuation, news, travel_alerts, flights, forex, adiz, stock
from utils.discord import send_to_discord
from utils.content import handle_content

def main():
    status = []
    header = []
    
    travel_section = handle_content(status, header, travel_alerts.run())
    adiz_section = handle_content(status, header, adiz.run())
    if FLIGHTS_API_KEY:
        flights_section = handle_content(status, header, flights.run(FLIGHTS_API_KEY))
    else:
        flights_section = ""
        
    news_section = handle_content([], [], news.run())
    
    status = "".join(status)
    if len(status) == 0: status = "✅☮️"
    report = f'{status}\n> {" | ".join(header)}\n\n{travel_section}\n\n{adiz_section}\n\n{flights_section}\n\n{news_section}\n\n'

    send_to_discord(report, DISCORD_WEBHOOK)

if __name__ == "__main__":
    main()
