from config import DISCORD_WEBHOOK
from modules import news_monitor, evacuation_monitor, travel_alerts, flights, forex, adiz
from utils.discord import send_to_discord
from utils.content import handle_content

def main():
    status = []
    header = []
    
    travel_section = handle_content(status, header, travel_alerts.run())
    
    status = "".join(status)
    if len(status) == 0: status = "✅☮️"
    report = f'{status}\n> {" | ".join(header)}\n\n{travel_section}\n\n'

    send_to_discord(report, DISCORD_WEBHOOK)

if __name__ == "__main__":
    main()
