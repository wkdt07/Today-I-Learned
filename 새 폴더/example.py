#서버로부터 데이터를 가져와보세요


# https://fakestoreapi.com/carts

#남들이 만들어놓은 코드를 가져다가 쓰자!   ->  라이브러리


import requests
import pprint
API_key = '87246d75e1ce26e1392a087b3d1d88c5'
#서울의 위도
lat = 37.56

#서울의 경도
lon = 126.97

url =f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'
data = requests.get(url).json()
pprint.pprint(data) 

print(data['weather'][0]['description'])




