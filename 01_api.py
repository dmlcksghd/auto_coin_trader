# REST API
import requests

url = "https://api.upbit.com/v1/market/all?isDetails=true"
response = requests.get(url)
data = response.json()     # JSON
# print(data)
print(len(data))    # 309개 존재

