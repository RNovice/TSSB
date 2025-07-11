import requests

def run(API_KEY: str):
  result = {
    "name": "今日飛往桃園機場航班",
    "symbol": "✈️",
    "status": "",
    "header": "☮️",
    "content": "模組異常"
  }
  try:
    url = 'http://api.aviationstack.com/v1/flights'
    sourceUrl = 'https://aviationstack.com/'
    params = {
      'access_key': API_KEY,
      'arr_icao': 'RCTP',
      'limit': 0, 
    }
    
    response = requests.get(url, params=params)
    if response.status_code != 200:
      raise Exception(f"URL error, status code: {response.status_code}")
    total = response.json()
    if total.get("error", None):
      raise Exception(f"API error, {total['error']['code']}")
    totalAmount = int(total["pagination"]["total"])
      
    response2 = requests.get(url, params={**params, 'flight_status': 'cancelled'})
    if response2.status_code != 200:
      cancelledAmount = None
    else:
      cancelled = response2.json()
      if cancelled.get("error", None):
        cancelledAmount = None
      else:
        cancelledAmount = int(cancelled["pagination"]['total'])
      
    cancelledContent = f'取消{cancelledAmount}班' if cancelledAmount is not None else "取消航班取得失敗"
    if totalAmount < 700 or (cancelled and cancelledAmount > 10):
      result.update({
        "status": "⚠️",
        "header": "⚠️",
        "content": f"航班數量偏低或取消數量偏多。總計{totalAmount}班，{cancelledContent} \n[資料來源](<{sourceUrl}>)"
      })
    elif totalAmount < 500 or (cancelled and cancelledAmount > 20):
      result.update({
        "status": "🚨",
        "header": "🚨",
        "content": f"航班數量過低或取消數量過多。總計{totalAmount}班，{cancelledContent} \n[資料來源](<{sourceUrl}>)"
      })
    else:
      result.update({
        "content": f"一切正常。總計{totalAmount}班，取{cancelledContent} \n[資料來源](<{sourceUrl}>)"
      })

  except Exception as e:
    result.update({
      "status": "🐞",
      "header": "🐞",
      "content": f"module error, please fix the bug \n{e}"
    })
      
  return result


if __name__ == "__main__":
  import os
  from dotenv import load_dotenv
  load_dotenv()
  print(run(os.getenv("FLIGHTS_API_KEY")))
