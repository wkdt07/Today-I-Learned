# a,b = map(int,input().split())
# print(a+b)

# print(int(input())-(2541-1998))

# a,b = input().split()
# print(int(a)*int(b[2]))
# print(int(a)*int(b[1]))
# print(int(a)*int(b[0]))
# print(int(a)*int(b))


## 1330
# a,b = map(int,input().split())

# if a>b:
#     print('>')

# elif a<b:
#     print('<')

# else:
#     print('==')


""" 9498 """
# t = int(input())

# if t>=90 and t<=100:
#     print('A')

# elif 80 <= t <= 89: #부등호 이렇게 써도 된다.
#     print('B')

# elif t>=70 and t<=79:
#     print('C')

# elif t>=60 and t<=69:
#     print('D')

# else:
#     print('F')

""" 
a= [1,2,3,4,5]
print(*a)
반복문 안 쓰고 리스트 요소 뽑아내는번
 """


""" 2753 윤년 
연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.

윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.

예를 들어, 2012년은 4의 배수이면서 100의 배수가 아니라서 윤년이다. 1900년은 100의 배수이고 400의 배수는 아니기 때문에 윤년이 아니다. 하지만, 2000년은 400의 배수이기 때문에 윤년이다.
"""

# y = int(input())

# if y % 400 == 0:
#     print(1)

# elif (y % 4 == 0) and (y % 100 != 0):
#     print(1)

# else:
#     print(0)

""" 14681 사분면 구하기 """

# x = int(input())
# y = int(input())

# if (x > 0) and (y > 0) :
#     print(1)

# elif (x<0) and (y>0):
#     print(2)

# elif (x<0) and (y<0):
#     print(3)

# elif (x>0) and (y<0):
#     print(4) 

""" 2884 알람 시계 """

# h , m = map(int,input().split())

# if (m-45) >= 0:
#     print(h, m-45)

# elif (m-45) < 0 :
#     if (h-1) < 0 :
#         h = 24
#     else:
#         h = h
#     print(h-1, m-45+60)
    

""" 2525 오븐시계 """

# h,m = map(int,input().split())
# t = int(input())

# while True :
#     if (m+t) >= 60:
#         h += 1
#         m = m + t - 60
#         if h >= 24:
#             h -= 24

#     elif (m+t)<60:
#         m += t
    
#     if (m <= 59) and  (0<=h <= 23):
#         break

# print(h,m)
# h,m = map(int,input().split())
# t = int(input())


# hp,mp = divmod(t,60)

# if (m+mp) >= 60:
#     h += hp+1
#     m = m + mp - 60

# elif (m+mp)<60:
#     h += hp
#     m += mp

# if h >= 24:
#     h -= 24


# print(h,m)


# h,m = map(int,input().split())
# t = int(input())

# a = m+t

# hp = a//60
# m = a%60
# 14
# h += hp

# if h >= 24:
#     h -= 24

# print(h,m)

""" 2480 주사위 세개 """

a,b,c = map(int,input().split())

# if (a == b) and (b == c):
#     print(3*a)

# elif (a==b) or (b == c) or (a == c):

for i in range(1,7):
    if a == i and 
