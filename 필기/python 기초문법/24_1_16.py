#============================================

#<단축>

# print(bool(0))
# print(bool(1))
# print(bool(5))
# print(bool(-1))

# print(bool(''))  #False
# print(bool('t')) #True
# print(bool('false'))  #True
# print(bool('True'))   #True
# print(bool('False'))  #True
# print(bool(False))    #False

# print('a' and 'b')  #b
# print('b' and 'a')  #a
# print('a' or 'b')   #a
# print('b' or 'a')   #b
# print('' or 'a')    #a
# print('' and 'a')   #결과값 ''라서 아무것도 안 나옴
# print(False and 'a') #False

# print('a' or 'b' and False)     #a
# print(('a' or 'b') and False)   #False

#======================================
#<복합연산자>
# a=list(range(11))
# print(sum(a))
# sum_value=0
# for i in range(11):
#     sum_value += i

# print(sum_value)


#===================================================

#<명시적 형변환>


# n=input()
# print(type(n))      #input()은 무조건 str

#-로또 6번호 추첨

#======================================================


#<Sequence Type>


#list

# 가변 sequence 자료형 -> 순서o -> 인덱싱, 슬라이싱, 길이, 반복 가능


# MAP = []

# Matrix = []

# array = [[1, 2, 3],
#          [4, 5, 6],
#          [7, 8, 9]]

# #실습 1 인덱싱하여 3을 출력해보세요.

# print(array[0][2])

# #실습 2 인덱싱하여 7을 출력해보세요.

# print(array[2][0])

# #실습 3 슬라이싱하여 [2, 3]을 출력해보세요.

# print(array[0][1:3])

# # 실습 3-1 슬라이싱하여 2 3을 출력해보세요.

# print(*array[0][1:3]) #unpacking



#======================================
# 2차원 리스트를 입력받는 방법 -> 행, 열이라는 표현 -> matrix[y][x]
# 1. for문 활용
# rows = int(input("행의 개수를 입력하세요"))
# matrix = []

# for i in range(rows):
#     row = list(map(int, input().split()))
#     matrix.append(row)

# for row in matrix:
#     print(row)

# 2. 리스트 컴프리헨션
# matrix = [list(map(int, input().split())) for _ in range(rows)]

# for row in matrix:
#     print(row)


# 시퀀스 자료형 ---> 리스트, 튜플, range
# 리스트 : 가변 시퀀스 자료형
# 튜플 : 불변 시퀀스 자료형
# range : 불변 시퀀스 자료형

# 튜플 쓰이는 예시 -> 방향배열 알고리즘 문제 
# -> 여러 값을 그룹화하여 하나의 불변 객체로 만든다.

# def move_around(position):
#     x, y = position
#     direct = [(0,1), (0,-1), (1,0), (-1,0)] # 상, 하, 좌, 우

# range 쓰이는 예시 ---> 주로 반복문과 함께 쓰인다

# range(end) : 0부터 end-1까지 1씩 증가
# ex) for i in range(10): -> 10번 반복하는 반복문(0부터 시작하기 때문)

# range(start, end) : start부터 end-1까지 1씩 증가
# range(start, end, step)
# 1. start < end, step > 0 
# : start부터 end-1까지 step만큼 증가

# 2. start > end, steo < 0
# : start부터 end+1까지 step만큼 감소
#=======================================

#<DICT>

# 중복된 키를 사용하면 어떤 value가 해당 키에 적용될까요?
# 마지막에 할당된 값으로 적용

#딕셔너리 실습

# my_dict = {
#     'a1' : {'b1' : 1, 'b2' : 2, 'b3' : 3},
#     'a2' : {'b1' : 4, 'b2' : 5, 'b3' : 6},
#     'a3' : {'b1' : 7, 'b2' : 8, 'b3' : 9}
# }

# #value 5를 출력해보세요.
# value=my_dict['a2']['b2']
# value = my_dict.get('a2').get('b2')

# print(value)


#======================================

# set : 가변 비시퀀스 자료형 -> 중복을 허용하지 x -> 수학의 집합과 동일한 연산 가능

# my_set1 = {1, 2, 3, 4, 5}
# my_set2 = {3, 4, 5, 6}

# result1 = my_set1 | my_set2
# result2 = my_set1 - my_set2
# result3 = my_set1 & my_set2

# print(result1)
# print(result2)
# print(result3)

##세트의 사용 예시 : 로또 번호 6개 추출하여 출력하는 프로그램

# import random

# lottery = set()
# while len(lottery) < 6:
#     a = random.randint(1,45)
#     lottery.add(a)

# lottery=list(lottery)
# lottery.sort()

# print(lottery)

# #sort()는 재귀 못 한다.
# a=[1,3,4,2,5]
# a.sort()
# print(a)


#===========================================

#None

# None 과 Null의 차이는 뭘까?


#============================================

# #<명시적 형변환으로 안되는거>
# # n=int(input()) #3.5 입력하면 오류남

# n=3.5
# int(n)  #3

# print(int('3.5')) #에러 난다.
# # 위 아래 다름

#=======================


##<비교연산자>

# 비교연산자는 항상 부등호부터 
# ex) =>, =< (x)
#     <=, >= (o)
 

#==================
##<깊은 카피와 얕은 카피>
# import copy
# a = [1, 2, 3]
# copy_a = copy.deepcopy(a)
# b=a

# print(id(b))
# print(id(a))
# print(id(copy_a))

# print(a==b) #True
# print(a==copy_a) #True

# print(a is b) #True
# print(a is copy_a) #False why? 서로 다른 객체라(메모리 주소가 다름)

# deep copy의 장점? 원본이 바뀌어도 복사본은 그대로

#=============================================


##<멤버십 연산자 in, not in>

# 조건문에서 주로 사용

# numbers = [1,2,3,4,5]
# print(1 in numbers)
# print (1 not in numbers)
# print(not(1 in numbers))

#======================================

# 파이썬은 객체지향언어

#====================

