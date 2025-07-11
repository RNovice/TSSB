import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")
FLIGHTS_API_KEY = os.getenv("FLIGHTS_API_KEY")

if __name__ == "__main__":
  print(DISCORD_WEBHOOK)
  print(FLIGHTS_API_KEY)
  
