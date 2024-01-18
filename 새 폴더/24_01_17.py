# #<함수>

# 1. 함수 정의

# def 함수명(매개변수):
#     code.....
#     return 반환값

# 2.함수 호출

# 함수명(함수인자)

# 함수 유형에는 총 4가지가 있다.
# 매개변수가 있을 수 있고, 없을 수 있다.
# 반환값이(return) 있을 수도 있고, 없을 수 있다.

# 함수 장점: 재사용성, 가독성, 유지보수성 -> 디버깅하기 좋다.
# ex) 4중, 5중 중첩 for문 -> 함수로 for문을 분리해서 디버깅에 용이하게.


# def get_sum(num1, num2):
#     return num1 + num2

# num1 = 5
# num2 = 3
# result = get_sum(num1, num2)
# print(result)


# #실습 1. 매개변수가 없는 함수로 바꿔보세요.

# def get_sum_2():
#     a = 5
#     b = 3
#     return a + b

# print(get_sum_2())

# #실습 2. 반환값이 없는 함수로 바꿔보세요.

# def get_sum_2(n1, n2):
#     result = n1 + n2
#     print(result)

# get_sum_2(5, 3)



#================================================================

# #파이썬이 제공하는 함수 (built-in function = 내장함수)

# print()

# ctrl + 클릭 하면 내장함수 확인 가능

#===========================================

# # default 인자 -> 매개변수에 기본값을 할당


# #키워드 인자: 인자의 순서를 바꿔도 결과는 같다.
# def greet(name,age):
#     print(f'안녕하세요, {name}님! {age}살이시군요.')

# greet(name='Dave',age=34)
# greet(age=34, name='Dave') #가능
# greet(name='Dave',34) #SyntaxError: positional argument follows keyword argument
# greet('Dave',age=34)

# #가변인자 : 매개변수 앞에 *(에스터리스크)를 붙여 여러 개의 인자를 tuple로 처리
# ex) print 함수

# #가변 키워드 인자: 매개변수 앞에 **를 붙여 여러 개의 인자를 dict로 묶어 처리



#=======================================================================

# #<함수 scope>

# #로컬 스코프 vs 노출 스코프

# def outer_func():
#     x = 1 # 로컬변수
#     def inner_func():
#         y = 2 # 로컬변수
#         sum_v = x + y #로컬 스코프에서 x와 y에 접근 가능
#         print(sum_v)
    
#     inner_func()
    
#     #로컬 스코프에서 x에는 접근 가능하지만 y에는 접근할 수 없다. why? y가 더 로컬스코프 , 이게 핵심

# outer_func()
# inner_func() #얜 아예 없는 애처럼 취급됨. inner_func이 outer_func 정의 끝나고 사라진거니깐
# 여기서 x가 노출 스코프에 있다.
# inner_func에서 x에 접근할 때, 노출 스코프에 있는 x에 접근하고 있다.

#이러면 맨 안에 있는 inner func만 사용 가능


#===============================================================================

# a,b,c=1,2,3

# def enclosed():
#     a,b,c=4,5,6

#     def local(c):
#         print(a,b,c) #이건 헷갈릴 수 있는 4 5 500이다.
    
#     local(500) #4 5 500
#     print(a,b,c)
# enclosed() #4 5 6
# print(a,b,c) #1 2 3 

# #if) global을 사용하면?

# a,b,c=1,2,3

# def enclosed():
#     global a,b,c #서로 변수에 할당된 값을 공유(Local과 Global을 연결해주는 것), LEGB 룰에 의해 우선순위

#     a,b,c=4,5,6 #재할당이라 생각 why? 로컬이 더 우선순위

#     def local(c):
#         print(a,b,c) 
    
#     local(500)
#     print(a,b,c)
# enclosed() #4 5 6
# print(a,b,c) #4 5 6 


# ws_3_2

# number_of_people = 0

# def increase_user():
#     number_of_people=0
#     number_of_people += 1
#     return number_of_people



# def create_user():
#     pass

# print(number_of_people) #0 얘는 global
# print(increase_user()) #1 얘는 호출하므로 local

#========================================================================================================

# #<재귀함수>
# 사용 예시 : DFS(깊이 우선 탐색) - 재귀함수(재귀호출)
# def facto(n):
#     if n == 0:
#         return 1 #break 타이밍 종료조건 
    
#     return n * facto(n-1)

# result = facto(5)
# # 5 * facto(4) -> 5 * 4 * facto(3) -> 5 * 4 * 3 * facto(2) -> 5 * 4 * 3 * 2 * facto(1) -> 5 * 4 * 3 *2 * 1
# print(result)

#===============================================================================================================

# # <map zip lambda>

# # map(function,iterable)

# #람다 함수는 1회성 

# def sq_number(x):
#     return x ** 2

# numbers = [1, 2, 3, 4, 5]

# sq_numbers = map(lambda x : x ** 2, numbers)
# print(list(sq_numbers))

# #zip 함수 -> 반복문에서 주로 사용

# girls = ['jane', 'ashley']
# boys = ['peter', 'jay']
# pair = zip(girls, boys) # 튜플로 들어감, 물론 zip은 보려면 하나 꺼내야 함 [('jane','ashley'),('peter','jay')]
# print(list(pair))
# for i in pair:
#     print(i,j)


#===============================================

#패킹 : 여러 값을 튜플로 묶는다(x) -> 여러 값을 하나의 시퀀스로 묶는 과정 -> 튜플

#언패킹 : 1) *를 활용 2) **를 활용


#==========================================================


##ws_3_2 

# number_of_people = 0



# def increase_user():
#     number_of_people=0
#     number_of_people += 1
#     return number_of_people



# def create_user(name,age,address):
#     user_info = {
#         'user_name' : name,
#         'user_age' : age,
#         'user_address' : address
#     }
        
#     return user_info #이제 함수 호출하면 그걸로 만들어진 딕셔너리가 그 결과물


# print(f'현재 가입 된 유저 수 : {number_of_people}')
# print(f"{create_user('홍길동','30','서울')['user_name']}님 환영합니다!") #그래서 create_user('홍길동','30','서울')가 user_info가 되는거임/ 만약 여기서
# # print(f"{user_info['user_name']}님 환영합니다!") 으로 하게 된다면 지금 글로벌 영역에 있으므로 local에 있는 user_info와는 아예 다른 변수가 되어서 오류남
# print(create_user('홍길동','30','서울'))
# print(f'현재 가입 된 유저 수 : {increase_user()}')