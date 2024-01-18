# a1 = 1
# a2 = 2.3
# a3 = 2 + 3j
# a4 = 'hello'
# a5 = True
# a6 = [1, 2, 3]
# a7 = (1, 2, 3)
# a8 = range(1, 4)
# a9 = {1, 2, 3}
# a10 = {"apple":2,"banana":3}
# a11 = None
# a12 = lambda x, y : x + y

# for i in range(1,13):
#     var=f'a{i}'
#     var=eval(var)
#     print(type(var))


#=================================================================

# print(3.2%2)

# 이거 0이 나와야 하는데 값이 이상하게 나온다.

# 나누기 관련된 연산자들은 무조건 정수형 데이터만 사용해라


# ====================================================================


# my_list=[1, 2, 3]
# sum=0

# for i in my_list:
#     sum+=i
# print(sum)

#이러면 안됨. why? sum이란 내장함수가 이미 존재. 
#답이 나온다 해도 나중에 sum이란 함수를 못 씀.

# =============================================
#변수 x의 메모리 주소는 어떤 값을 할당하더라도 같을까? x 
# x = 36.5
# x= 36.5
    
# print(id(x))
# x= 7
# print(id(x))


#==================================================

#줄바꿈 쓰는 경우

# fruits={"apple" : 4,
#         "banana" : 3,
#         "kiwi" : 2}

# my_list= [[1, 2, 3, 4, 5],
#           [6, 7, 8, 9, 10]]

# def dfs_people():
#     pass
# #띄어쓰기
# def b():
#     pass

 
# =========================================================

# a = []
# for i in range(10):
#     a.append(i)

# print(a[10])
# IndexError: list index out of range 이런 에러가 뜬다.


#이럴 때 python tutor 쓰는거. 


#========================
#<int>

# decimal = 10
# #2진수
# binary = bin(decimal)
# binary_re = bin(decimal)[2:]
# print(binary)
# print(binary_re)

# #8진수

# octal = oct(decimal)[2:]
# print(octal)

# #16진수

# hexa = hex(decimal)[2:]
# print(hexa)

#=================================

# <실수형> -> 부동소수점이 문제 

#1) 부동소수점이 정말 작은지 확인하는 첫 번째 방법
# a = 3.2 - 3.1
# b = 1.2 - 1.1
# print(a,b) #두 값이 다르게 나온다
# print(abs(a-b) <= 1e-10) #두 값의 차이가 정말 작으면(True) 사실상 같은 수


#2) 두 수가 거의 같은지 여부 두 번째 방법

# import math
# print(math.isclose(a,b)) # 얘도 마찬가지로 둘이 거의 같으면 True

# num_a = f'{a:.1f}'
# num_b = f'{b:.1f}'

# print(num_a)
# print(num_b)

# 우리가 부동소수점을 출력할 때 f-string 포맷팅을 사용하여 정확도를 제어할 수 있다.

#=========================================

# print(314e-2)
# print(314*10**-2)

#둘이 같은 말임 e-2 == 10**-2

#=================================================

# <부동소수점 처리 on 소수>
# n=2/3
# print(f'{n:.2f}')
# srt1='hello'
# print(f'{srt1}')

#======================================================

# <Sequence Type(시퀀스 자료형)>
# str(문자열):불변 시퀀스 자료형 -> 값을 바꿀 수 없음
# list(리스트):'가변' 시퀀스 자료형
# =>sw역량테스트 1. 문자열 파싱 vs 2. 방향 배열

#======================================================

#<슬라이싱>

#====================================================

# greeting='hello world'
# #실습 1. 인덱싱 ->알파벳 w를 출력해보세요.
# #실습 2-1. 슬라이싱-> hello를 출력해보세요.
# #실습 2-2. 슬라이싱-> world를 출력해보세요.
# #실습 2-3. 슬라이싱-> 문자열을 거꾸로 출력해보세요.
# #실습 3. 내장함수(메서드)를 사용하여 문자열의 길이를 출력해보세요.
# # print(greeting[6])
# # print(greeting[0:5])
# # print(greeting[6:11])
# # print(greeting[::-1])
# # print(len(greeting))

# print(greeting[10:5:-1])


#===================================================

#<포맷팅>
# name=input()
# age=int(input())
# height=float(input())

# #1) 
# print('저의 이름은 %s, 나이는 %d, 키는 %.2f입니다.'%(name, age, height))

# #2)
# print('저의 이름은 {}, 나이는 {}, 키는 {:.2f}입니다.'.format(name, age, height))

# #3) f-string
# print(f'저의 이름은 {name}, 나이는 {age}, 키는 {height:.2f}입니다.')