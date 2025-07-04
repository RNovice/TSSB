import requests

def send_to_discord(content: str, webhook_url: str):
    payload = {
        "content": content
    }
    response = requests.post(webhook_url, json=payload)
    if response.status_code != 204:
        print(f"Failed to send Discord message: {response.text}")