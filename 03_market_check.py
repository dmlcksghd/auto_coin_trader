# 마켓 코드 조회
import pyupbit
import requests

# tickers = pyupbit.get_tickers()
# tickers = pyupbit.get_tickers(fiat="BTC")
# print(tickers)
# print(len(tickers))

url = "https://api.upbit.com/v1/market/all?isDetails=true"
resp = requests.get(url)
data = resp.json()     # JSON

krw_tickers = []

for coin in data:
    ticker = coin['market']     # coin is dict
    warning = coin['market_warning']    # 유의 종목 / NONE (해당 사항 없음), CAUTION(투자유의)
    # print(ticker)

    # KRW, BTC, USDT 사용 가능
    if ticker.startswith("KRW"):
        krw_tickers.append(ticker)

# print(krw_tickers)
# print(len(krw_tickers))     # 119개 존재
