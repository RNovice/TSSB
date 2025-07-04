import requests
from bs4 import BeautifulSoup

def run():
    url = "https://travel.state.gov/content/travel/en/traveladvisories/traveladvisories/taiwan-travel-advisory.html"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch page. Status code: {response.status_code}")

    soup = BeautifulSoup(response.content, "html.parser")
    

    level_element = soup.find("h3", class_="tsg-rwd-emergency-alertheader-title")
    level_text = level_element.get_text(strip=True) if level_element else "Travel Level Not Found"

    return  level_text

if __name__ == "__main__":
    run()
