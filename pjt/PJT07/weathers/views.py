from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
import requests # 외부 url에서 데이터 받아올 수 있도록, JS의 Axios 같은 거임

# Create your views here.
# A. 서울의 5일 치 예보 데이터 확인
from django.conf import settings
api_key = settings.WEATHER_API_KEY

def index(request):
    
    city_name = 'Seoul,KR'    

    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}'
    response = requests.get(url).json()
    return JsonResponse(response)


# B. 원하는 데이터만 DB에 저장
# @api_view
from .serializers import WeatherSerializer
def save_data(request):
    city_name = 'Seoul,KR'    
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}'
    response = requests.get(url).json()
    
    for li in response.get('list'):
        #원하는 데이터 추출하기
        dt_txt = li.get('dt_txt')
        temp = li.get('main').get('temp')
        feels_like = li.get('main').get('feels_like')
        
        save_data = {
            'dt_txt' : dt_txt,
            'temp' : temp,
            'feels_like': feels_like,
        }
        # 확인하려면 print 해봐라
        
        # 저장할 수 있도록 변환/ 포장(serialize) -> is_valid() 하다면 save()
        
        # 유효성 검증 
        # 포장 -> serializers.py
        # 유효하다면, 저장
        
        serializer = WeatherSerializer(data = save_data)
        
        # 포장이 잘 됐는지 확인
        if serializer.is_valid(raise_exception = True):
            # 유효하다면 저장
            serializer.save()
        
    return JsonResponse({'message':'completed!'})

# C. 저장된 전체 데이터 조회


from .models import Weather
from rest_framework.decorators import api_view


@api_view(['GET'])
def list_data(request):
    weathers = Weather.objects.all() # 리스트 -> 2개 이상 가능성 -> many = True
    serializers = WeatherSerializer(weathers,many = True)
    
    return Response(serializers.data)
    # Response 는 rest.framework꺼라서 api 함수로 구현한 것. -> api_view 데코레이터 써야 json으로 나옴
    # jsonresponse는 장고꺼라 이게 필요 없음 
    
    # 정보 : rest_framework는 Installed Apps에 등록해야함
    
    
# D. 특정 조건에 따라 출력

@api_view(['GET'])
def hot_weathers(request):
    # 가장 단순한 방법
    # 1. 전체를 가져온다.
    # 2. 새로운 리스트에다가 조건에 맞는 데이터만 추가한다
    # 3. 포장해서 반환한다. 
    
    
    '''
    # 1. 전체를 가져온다.   
    weathers = Weather.objects.all()
    hot_weathers = []
    # 2. 새로운 리스트에다가 조건에 맞는 데이터만 추가한다
    for weather in weathers:
        # 섭씨 온도가 30도가 넘으면 hot_weathers에 추가
        celsius = round(weather.temp - 273.15,2)
        if celsius > 30:
            hot_weathers.append(weather)
    # 3. 포장해서 반환한다. 
    serializers = WeatherSerializer(hot_weathers,many = True) # 리스트도 포장 가능
    
    return Response(serializers.data)
    '''
    
    # 효율적으로? 권장방식?
    # 굳이 전체를 가져올 필요 없다.
    # 새로 필터링해서 넣는것도 시간 든다
    # ORM 공부의 필요성
    # 잘 모르면 지피티 써라
    weathers = Weather.objects.filter(temp__gt=(30+273.15)) # __gt는 초과 # 얘는 쿼리셋 방식
    serializers = WeatherSerializer(weathers,many = True)
    return Response(serializers.data)

    

