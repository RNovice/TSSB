import yfinance as yf
import pandas as pd
import numpy as np

def fetch_close(symbol='USDTWD=X', period='1y'):
    data = yf.download(symbol, period=period, interval='1d', progress=False)
    close = data['Close'].dropna()
    return close

def compute_returns(close):
    """
    對數日報酬率 r_t = ln(P_t / P_{t-1})。
    """
    r = np.log(close / close.shift(1)).dropna()
    return r

def compute_volatility(r, window=250):
    abs_r = r.abs()

    mu_1d    = abs_r.rolling(window).mean().iloc[-1]
    sigma_1d = abs_r.rolling(window).std().iloc[-1]
    thresh1d_anom    = mu_1d + 2*sigma_1d
    thresh1d_extreme = mu_1d + 3*sigma_1d
    pct95_1d = np.percentile(abs_r[-window:], 95)
    pct99_1d = np.percentile(abs_r[-window:], 99)

    vol_2d = np.sqrt(r**2 + r.shift(1)**2).dropna()
    mu_2d    = vol_2d.rolling(window).mean().iloc[-1]
    sigma_2d = vol_2d.rolling(window).std().iloc[-1]
    thresh2d_anom    = mu_2d + 2*sigma_2d
    thresh2d_extreme = mu_2d + 3*sigma_2d
    pct95_2d = np.percentile(vol_2d[-window:], 95)
    pct99_2d = np.percentile(vol_2d[-window:], 99)

    vol_5d = r.rolling(5).apply(lambda x: np.sqrt((x**2).sum()), raw=True).dropna()
    mu_5d    = vol_5d.rolling(window).mean().iloc[-1]
    sigma_5d = vol_5d.rolling(window).std().iloc[-1]
    thresh5d_anom    = mu_5d + 2*sigma_5d
    thresh5d_extreme = mu_5d + 3*sigma_5d
    pct95_5d = np.percentile(vol_5d[-window:], 95)
    pct99_5d = np.percentile(vol_5d[-window:], 99)

    return {
        'mu_1d': mu_1d, 'sigma_1d': sigma_1d,
        'thresh1d_anom': thresh1d_anom, 'thresh1d_extreme': thresh1d_extreme,
        'pct95_1d': pct95_1d, 'pct99_1d': pct99_1d,
        'mu_2d': mu_2d, 'sigma_2d': sigma_2d,
        'thresh2d_anom': thresh2d_anom, 'thresh2d_extreme': thresh2d_extreme,
        'pct95_2d': pct95_2d, 'pct99_2d': pct99_2d,
        'mu_5d': mu_5d, 'sigma_5d': sigma_5d,
        'thresh5d_anom': thresh5d_anom, 'thresh5d_extreme': thresh5d_extreme,
        'pct95_5d': pct95_5d, 'pct99_5d': pct99_5d,
    }


def main():
    close = fetch_close()
    r = compute_returns(close)
    stats = compute_volatility(r)

    print("── USD/TWD 波動門檻計算結果（過去 1 年、250 日滾動）──")
    print(f"【單日】 μ = {float(stats['mu_1d']):.6f}, σ = {float(stats['sigma_1d']):.6f}")
    print(f"  → 異常值 (μ+2σ) = {float(stats['thresh1d_anom']):.6f}")
    print(f"  → 反常值 (μ+3σ) = {float(stats['thresh1d_extreme']):.6f}")
    print(f"  → 95% 分位 = {float(stats['pct95_1d']):.6f}, 99% 分位 = {float(stats['pct99_1d']):.6f}\n")

    print(f"【雙日】 μ = {float(stats['mu_2d']):.6f}, σ = {float(stats['sigma_2d']):.6f}")
    print(f"  → 異常值 (μ+2σ) = {float(stats['thresh2d_anom']):.6f}")
    print(f"  → 反常值 (μ+3σ) = {float(stats['thresh2d_extreme']):.6f}")
    print(f"  → 95% 分位 = {float(stats['pct95_2d']):.6f}, 99% 分位 = {float(stats['pct99_2d']):.6f}\n")

    print(f"【單週】 μ = {float(stats['mu_5d']):.6f}, σ = {float(stats['sigma_5d']):.6f}")
    print(f"  → 異常值 (μ+2σ) = {float(stats['thresh5d_anom']):.6f}")
    print(f"  → 反常值 (μ+3σ) = {float(stats['thresh5d_extreme']):.6f}")
    print(f"  → 95% 分位 = {float(stats['pct95_5d']):.6f}, 99% 分位 = {float(stats['pct99_5d']):.6f}")

if __name__ == "__main__":
    main()
