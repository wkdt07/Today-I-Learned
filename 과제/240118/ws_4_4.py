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
company_list = []
for dic in parsed_data:

    
    name = dic["name"]
    companyname = dic['company']["name"]
    company_list.append(companyname)

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

# print(dummy_data)


black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]


# can_use = []

# for user in company_list:
    
#     if user not in black_list:
#         can_use.append(user) 

# print(can_use) #이용 가능한 회사

def create_user(dummy_data):
    can_use = []
    for user in company_list:
    
        if user not in black_list:
            can_use.append(user) 

    if companyname in can_use:
        #굳이 can_use list 안 쓰고 그냥 바로 not in 써도 될거 같다.

    pass


def censorship():
    pass
