from config import DISCORD_WEBHOOK
from modules import news_monitor, evacuation_monitor, travel_alerts, flights, forex, adiz
from utils.discord import send_to_discord

def main():
    report = []
    
    travel_result = travel_alerts.run()
    report.append(travel_result)

    send_to_discord("\n".join(report), DISCORD_WEBHOOK)

if __name__ == "__main__":
    main()
