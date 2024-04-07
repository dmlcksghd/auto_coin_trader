# 연습문제
# 1. 업비트는 마켓코드(KRW-BTC)를 통해 주문을 수행
# REST API 코드를 사용해서 원화 시장에서 거래가 가능한 가상화폐의 마켓코드를
# 파이썬 리스트로 저장

# REST API
import requests

# url = "https://api.upbit.com/v1/market/all?isDetails=true"
url = "https://api.upbit.com/v1/market/all"
response = requests.get(url)
data = response.json()     # JSON
# print(data)
# print(len(data))    # 309개 존재

krw_tickers = []

for coin in data:
    ticker = coin['market']     # coin is dict
    # print(ticker)

    if ticker.startswith("KRW"):
        krw_tickers.append(ticker)

print(krw_tickers)
print(len(krw_tickers))     # 119개 존재
