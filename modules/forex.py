import requests
from datetime import date, timedelta

# ── USD/TWD 波動門檻計算結果（過去 1 年、250 日滾動）──
# 【單日】 μ = 0.003787, σ = 0.005578
#   → 異常值 (μ+2σ) = 0.014942
#   → 反常值 (μ+3σ) = 0.020520
#   → 95% 分位 = 0.011802, 99% 分位 = 0.024832

# 【雙日】 μ = 0.005986, σ = 0.007420
#   → 異常值 (μ+2σ) = 0.020826
#   → 反常值 (μ+3σ) = 0.028246
#   → 95% 分位 = 0.016874, 99% 分位 = 0.038009

# 【單週】 μ = 0.010474, σ = 0.010827
#   → 異常值 (μ+2σ) = 0.032128
#   → 反常值 (μ+3σ) = 0.042955
#   → 95% 分位 = 0.022514, 99% 分位 = 0.071741

def get_usd_to_twd(date_obj):
  date_str = date_obj.isoformat()
  url = f"https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@{date_str}/v1/currencies/usd.json"
  try:
    response = requests.get(url)
    response.raise_for_status()
    return response.json().get('usd', {}).get('twd')
  except Exception:
    return None


def volatility(cur, his): 
  return round((cur - his) / his * 100, 2) if cur and his else None

def run():
  result = {
    "name": "美元對台幣波動",
    "symbol": "💵",
    "status": "",
    "header": "☮️",
    "content": "模組異常"
  }
  try:
    today = date.today()
    rates = {
      str(offset): get_usd_to_twd(today - timedelta(days=offset))
      for offset in [0, 1, 2, 7]
    }
    
    cur_rate = rates['0']
    if cur_rate is None: 
      raise Exception("現價取得失敗")
    
    vol_1d = volatility(cur_rate, rates['1'])
    if vol_1d is None: 
      raise Exception("波動取得失敗")
    
    vol_2d = volatility(cur_rate, rates['2'])
    vol_7d = volatility(cur_rate, rates['7'])
    
    report = (
      f"現價：{round(cur_rate, 2)}\n"
      f"單日：{vol_1d}%、"
      f"雙日：{vol_2d if vol_2d is not None else '未知'}%、"
      f"單週：{vol_7d if vol_7d is not None else '未知'}%"
    )
    
    content = "一切正常。"
    if vol_1d > 1.5 or (vol_2d and vol_2d > 2):
      result.update({
        "status": "⚠️",
        "header": "⚠️",
      })
      content = "漲幅異常，單日超過1.5%或雙日超過2%，建議比對其他項目。 \n"
    elif vol_1d > 3 or (vol_2d and vol_2d > 4):
      result.update({
        "status": "🚨",
        "header": "🚨",
      })
      content = "漲幅反常，單日超過3%或雙日超過4%，提高警覺。 \n"
      
    
    result["content"] = f"{content}{report} \n[資料來源](<https://github.com/fawazahmed0/exchange-api>)"

  except Exception as e:
    result.update({
      "status": "🐞",
      "header": "🐞",
      "content": f"module error, please fix the bug \n{str(e)[:200]}"
    })
      
  return result

if __name__ == "__main__":
    print(run())