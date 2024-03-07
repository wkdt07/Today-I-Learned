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
    companyname = dic['company']["name"]

    # small_dic = {
    #         'company' : companyname,
    #         'name': name
    #     }
    
    if  (-80 <float(dic['address']['geo']['lat'])<80) and (-80<float(dic['address']['geo']['lng'])<80):
        # small_dic['lat'] = dic['address']['geo']['lat']
        small_dic = {
            'company' : companyname,
            'lat' : dic['address']['geo']['lat'],
            'lng' : dic['address']['geo']['lng'],
            'name': name
        }
        dummy_data.append(small_dic)

    
    # else:
    #     continue
        
    # if  float(dic['address']['geo']['lng'])<80 and float(dic['address']['geo']['lng'])>-80:
    #     small_dic['lng'] = dic['address']['geo']['lng']
        
    
print(dummy_data)



