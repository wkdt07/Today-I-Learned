# import math

# print(math.pi)

# print(int(math.pi))

# print(math.sqrt(4))


# from math import pi,sqrt
# print(pi)

# import my_math

# print(my_math.add(3,4))

#================================================

#                                                                          #모듈


#모듈과 패키지의 집합이 라이브러리

# ctrl 좌클릭하면 상세 정보 확인 가능 (모듈을 사용하면 파일이 열림)

# import random

# print(random.randint(1,10)) #1부터 10까지 랜덤 정수 하나

# from random import * #random.py 부터 모든 매서드를 가져오는 것

# print(randint(1,10)) #random. 안 써도 됨

# from my_package.math import my_math
# from my_package.statistics import tools

# print(my_math.add(1,2))
# print(tools.mod(4,3))

# ###주의! 같은 디렉토리에 있어야 한다.


#===============================

###                                                 <PSL, Python Standard Library> <-> 사용자 설치 라이브러리:직접 다운받아야함


# pip (Python Package Installer): pip 명령어를 통해서 패키지를 설치, 삭제, 관리 

# pip install -> 어디에 설치? 파이썬 기본 위치. 이거 직접 찾아봐야한다. 

#전역환경(pip) vs 가상환경 >> 어느 경우에 나눠서 쓸까?

#=================================================================================

##                   <0119 예습 - json visualization on https://jsonviewer.stack.hu/>
# import requests
# url = 'https://random-data-api.com/api/v2/users'
# response = requests.get(url).json()
# print(response)



# json viwer에서 결과물을 정리할 수 있음.
# {'id': 3756, 'uid': '20c7ef8f-2dc3-4ca9-9920-89b6b4b5cba9', 'password': 'JYnmrSXHlb', 'first_name': 
# 'Josef', 'last_name': 'Ritchie', 'username': 'josef.ritchie', 'email': 'josef.ritchie@email.com', 'avatar': 'https://robohash.org/repellendusdoloremqueillum.png?size=300x300&set=set1', 'gender': 'Female', 'phone_number': '+255 482-757-4145 x52962', 'social_insurance_number': '311470009', 'date_of_birth': '1984-07-23', 'employment': {'title': 'Forward Construction Orchestrator', 'key_skill': 'Networking skills'}, 'address': {'city': 'Kochborough', 'street_name': 'McClure Oval', 'street_address': 
# '99090 Christiansen Run', 'zip_code': '44928', 'state': 'Connecticut', 'country': 'United States', 'coordinates': {'lat': 24.707401324826705, 'lng': 96.97163972402996}}, 'credit_card': {'cc_number': '6771-8945-6278-6129'}, 'subscription': {'plan': 'Silver', 'status': 'Blocked', 'payment_method': 'Money transfer', 'term': 'Full subscription'}}


# print(response['address']['country']) #Unitied States


#==================================================================

###                           <제어문>


#if 조건식 : 조건식이 True일 경우 code를 실행
#if의 부정 elif, elif의 부정 else


# dust = int(input())

# if dust > 150 :
#     print('매우 나쁨')

# elif dust > 80 : #if 150>= dust > 80
#     print('나쁨')

# else :  # if dust <= 80
#     print('좋음')


'''
실습문제 : 연도를 입력받아 윤년 판별하기. 윤년이면 'leap year' 출력
그렇지 않으면 'common year' 출력

1. 연도가 4로 나누어 떨어지지만 100으로는 나누어 떨어지지 않는다.
2. 연도가 400으로 나누어 떨어진다.

'''

# year = int(input())

# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print('leap year')

# else:
#     print('common year')


##                   <for 반복문>

# for 변수 in 반복 가능한 객체(iterable)
# iterable ->list , tuple , str , range 등등


# 변수 -> i , j , k ... y, x (y,x는 행렬에서 자주 씀)

# numbers = [1, 2, 3, 4, 5]

# for num in numbers: #변수를 직관적으로 지어라


'''
실습 문제: 정수 n을 입력 받아 n단의 왼쪽 직각 이등변 삼각형 그리는 프로그램을 작성
'''

'''for문 하나'''
# num = int(input('n : '))

# for i in range(1, num+1):
#     print('*' * i)


'''중첩for문으로'''
# num = int(input('n : '))
# for i in range(num):
#     for j in range(i+1):
#         print('*', end = '')
#     print() # 줄바꾸기용


#==========================================================================


##                     <while문>

# 1. 초기식

# while 2.조건식 :

#     code.....

#     3. 증감식


# 1. while 문은 조건식이 참일 동안 반복(=조건식이 거짓일 때까지)

# 2. 프로그램 종료 조건 '반드시 필요'

# --continue : 반복문에서 일부 코드를 건너 뛰는 역할, 주로 while 안에 if 를 넣어서 사용, 조건이 만족하면 해당 반복은 한 번 건너뜀

'''실습 1. while문 + continue를 사용하여 1부터 10까지 정수 중 홀수만 출력하기'''

# n = 1
# while n < 10 : #n==10인게 종료조건
#     if n % 2 == 0:
#         n += 1
#         continue
#     print(n)
#     n += 1

#이렇게 하거나 

# '''
# i = 0

# while i < 10:
#     i += 1
#     if i % 2 == 0:
#         continue
#     print(i , end = ' ')
# '''


"""
실습 2. 'shell we close(y/n)' 문구에 y를 입력하면 반복문을 종료하고,
 'the end'를 출력하는 프로그램을 작성해보세요.
"""

# while True: #무한반복
#     title = input('shell we close(y/n)')
#     if title == 'y':
#         print('The End')
#         break #무한반복 깨는거
#     print('Repeat')



#========================================================================


###                   <List Comprehension>

rows = int(input()) #행
cols = int(input()) #열

'''2차원 리스트 컴프리헨션을 사용하여 0으로 최과된 2차원 리스트 생성'''



'''

matrix = [[0 for _ in range(cols)] for _ in range(rows)]


'''

# for row in matrix:
#     print(row)

'''
리스트 컴프리헨션 안 쓰면 이렇게 써야한다.

rows = int(input())
cols = int(input())

matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(0)
    matrix.append(row)

리스트 컴프리헨션 안 쓰면 이렇게 써야한다.
'''