import requests

# 설정할 매개변수
market = "KRW-BTC"  # 예시 마켓 코드
unit = 1  # 분 단위
count = 200  # 가져올 캔들의 개수

# API 요청 URL 구성
url = f"https://api.upbit.com/v1/candles/minutes/{unit}?market={market}&count={count}"

# 요청 및 응답
response = requests.get(url)
data = response.json()

# 초기 고가와 저가 설정
max_high_price = data[0]['high_price']
min_low_price = data[0]['low_price']

# 응답 데이터 출력 및 최고가/최저가 계산
for candle in data:
    print(f"시간(KST): {candle['candle_date_time_kst']}, 시가: {candle['opening_price']}, 종가: {candle['trade_price']}, 고가: {candle['high_price']}, 저가: {candle['low_price']}")

    # 최고가 갱신
    if candle['high_price'] > max_high_price:
        max_high_price = candle['high_price']

    # 최저가 갱신
    if candle['low_price'] < min_low_price:
        min_low_price = candle['low_price']

# 최고가와 최저가 출력
print(f"\n가장높은 고가: {max_high_price}, 가장 낮은 저가 : {min_low_price}")