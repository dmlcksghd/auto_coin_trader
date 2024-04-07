import requests

# 설정할 매개변수
market = "KRW-BTC"
count = 100     # 가져올 캔들 수

# API 요청 URL 구성
url = f"https://api.upbit.com/v1/candles/days?market={market}&count={count}"

# 요청 및 응답
response = requests.get(url)
data = response.json()

# 응답 데이터 출력
for candle in data:
    print(f"날짜(KST): {candle['candle_date_time_kst']}, 시가: {candle['opening_price']}, 고가: {candle['high_price']}, 저가: {candle['low_price']}, 종가: {candle['trade_price']}, 누적 거래량: {candle['candle_acc_trade_volume']}")