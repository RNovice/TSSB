[中文指南](README.zh.md)

## Fork for GitHub action automation

1. [Fork this project](https://github.com/RNovice/TSSB/fork)
2. Set up repository secrets:
   - Go to: **Settings** > **Secrets and variables** > **Actions**
   - Add a new repository secret:
     - Name: `DISCORD_WEBHOOK`
     - Secret: Your Discord webhook URL
   - (Optional) Add another secret:
     - Name: `FLIGHTS_API_KEY`
     - Secret: Your aviationstack API key
   - > FLIGHTS_API_KEY is optional. The script will skip flight-related data if not provided.
   <!-- - New repository secret > Name `DISCORD_WEBHOOK` > Secret: `your discord webhook url`
   - New repository secret > Name `FLIGHTS_API_KEY` > Secret: `your aviationstack api key`
   - `FLIGHTS_API_KEY` is optional, script well skip if not setup -->
3. Enable GitHub Actions workflows:

   - Navigate to: **Actions**
   - Click: "I understand my workflows, go ahead and enable them"
   - Find **Daily Alert Report**, then click **Enable workflow**

4. Manual test
   - In the **Actions** tab, choose **Daily Alert Report**
   - Click **Run workflow**, wait for completion, and check the result

## Local usage

> Note: Use `python3` and `pip3` if required by your OS.

### Optional: Create a virtual environment

```bash
python -m venv env
# macOS/Linux
source env/bin/activate
# Windows
env\Scripts\activate
```

### Set up environment variables

Create a .env file in the root directory:

```env
DISCORD_WEBHOOK={{your discord webhooks url}}
FLIGHTS_API_KEY={{your aviationstack api key}}
```

> Omit FLIGHTS_API_KEY if not using flight data.

### Install dependencies and run

```bash
pip install -r requirements.txt
python main.py
```

## Analyze source

- U.S. DEPARTMENT of STATE - [Travel.State.Gov](https://travel.state.gov/content/travel.html)
- Aviationstack Global Aviation Data - [Aviationstack](https://aviationstack.com)
- Taiwan Ministry of National Defense - [mnd.gov.tw](https://www.mnd.gov.tw/)
- fawazahmed0/exchange-api - [currency-api](https://github.com/fawazahmed0/exchange-api)
- Google News - [news.google.com](https://news.google.com/)
