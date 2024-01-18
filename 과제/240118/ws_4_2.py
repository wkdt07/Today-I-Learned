import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users' #이거 주소만 바꾸면 됨.
    # API 요청
response = requests.get(API_URL)
    # JSON -> dict 데이터 변환
parsed_data = response.json()

# print(parsed_data) #list형태로 dict들 있음


dummy_data = []

for dic in parsed_data:

    name = dic["name"]

    dummy_data.append(name)

print(dummy_data)



