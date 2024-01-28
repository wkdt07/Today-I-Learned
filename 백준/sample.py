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

# a,b,c = map(int,input().split())




# a,b,c = 1,2,3


# if (a == b) and (b == c):
#     p = 10000 + 1000 * a

# elif (a == b) or (b == c) or (c == a):
#     p = 1000 + 


# a, b, c = map(int,input().split())

# L = [a,b,c]
# L.sort()

# for i in range(1,7):
#     if a==i and b == i and c == i:
#         p = 10000 + 1000 * i 
    
#     elif (a == i and b == i) or (a==i and c == i ) or (b==i and c ==i):
#         p = 1000 + 100 * i 
    
#     elif a != b and b != c and c != a:
#         p = 100 * L[2]

# print(p)

'''
a, b, c = map(int, input().split())

lst = [a, b, c]
lst.sort()
set_1 = set(lst)

if len(set_1) == 1:
    num = set_1.pop()
    print(10000 + num * 1000)
elif len(set_1) == 2:
    if lst[0] == lst[1]:
        print(1000 + lst[0]*100)
    elif lst[1] == lst[-1]:
        print(1000 + lst[-1]*100)
elif len(set_1) == 3:
    max = lst[-1]
    print(max*100)


    #갯수를 이용해 풀고 싶다면 set을 쓸 수도 있었다.
'''


# =================================================

'''
2739 구구단
'''

# n = int(input())

# i = 1

# while i < 10:
#     print(f'{n} * {i} = {n*i}')
#     i += 1


'''
10950 A+B-3
'''

# t = int(input())

# for i in range(t):
#     a, b = map(int,input().split())
#     print(a+b)



'''
8393 합
'''

# n = int(input())

# a = range (1,n+1)

# print(sum(a))

'''
25304 영수증
'''

# total = int(input())

# n = int(input())  
""" 이래야 총 몇 번 계산해야되는지 알 수 있다.  """

# calc = 0

# for i in range(n):
#     a,b = map(int,input().split()) 
#     calc += a*b

# if total == calc:
#     print('Yes')

# else:
#     print('No')


'''
25314 코딩은 체육 과목입니다
'''

# n = int(input())

# a = n//4

# t = 'long '* a

# print(f'{t}int')



"""
A+B -7
"""

# T = int(input())

# for t in range(1,T+1):
#     a,b = map(int,input().split())
#     print(f'Case #{t}: {a} + {b} = {a+b}')


'''
2438 별 찍기 - 1
'''

# n = int(input())

# for i in range(1,n+1):
#     a =' '*(n-i) + '*'*i
#     print(a)

''' *
   **
  ***
 ****
*****'''
'''
a = int(input())
for i in range(a-1,-1,-1):
  print(' '*i,'*'*(a-i),sep='')
  '''


# ================================

""" 
10807 개수 세기
 """

# a = int(input())

# L = list(map(int,input().split()))

# b = int(input())

# print(L.count(b))


'''
10871 x보다 작은 수
'''

# n , x =map(int,input().split())

# lst = list(map(int,input().split()))

# lst2 = []

# for i in lst:
#     if i < x:
#         lst2.append(i)

# print(*lst2)


'''
10818 최소, 최대
'''

# n = int(input())

# lst = list(map(int,input().split()))
# lst.sort()

# s,b = lst[0],lst[n-1]

# print(s,b)

'''
2562 최댓값과 인덱스
'''

# a = []

# for i in range(9):
#     n = int(input())
#     a.append(n)

# b = a[:]
''' 얕은 복사라도 하지 않으면 a랑 b 랑 같이 바뀜. 가변인자라 '''


# a.sort()

# x = a[8]
# idx = b.index(x)+1

# print(x)
# print(idx)


'''
### 10810 공 넣기 ### 다시봐라
'''

# n,M = map(int,input().split())

# lst = list(0 for _ in range(n))

# for m in range(M):
#     i, j, k = map(int,input().split())
#     for a in range(i-1,j):
#         lst[a] = k

# print(*lst)



'''
10813 공바꾸기
'''

# n , M = map(int,input().split())

# lst = list(i for i in range(1,n+1))

# for m in range(M):
#     i , j = map(int,input().split())
#     lst[i-1],lst[j-1] = lst[j-1],lst[i-1]

# print(*lst)


'''
5597 과제 안 내신 분..? 
'''

# lst = [i for i in range(1,31)]

# for j in range(28):
#     a = int(input())
#     lst.remove(a)

# lst.sort()

# print(lst[0])
# print(lst[1])


'''
3052 나머지
'''

# lst = []

# for i in range(10):
#     num = int(input())
#     div = num % 42
#     lst.append(div)

# set_lst = set(lst)

# print(len(set_lst))


'''
10811 바구니 뒤집기
'''

# N , M = map(int,input().split())

# lst = [ _ for _ in range(1,N+1) ]
# lst_rev = lst[::]
# for m in range(M):
#     i,j = map(int,input().split())
#     i -= 1
#     j -= 1
#     # lst_rev[i:j+1] = lst[j:i-1:-1] 슬라이싱은 추출을 해버린다. 
#     # print(lst_rev) [3, 4, 5]
#     for k in range(i,j+1):
#         lst_rev2 =lst_rev[::]
#         if i == j:
#             pass
#         else:
#             lst_rev[k] = lst_rev2[i+j-k]
#         print(lst_rev)



# N , M = map(int,input().split())

# lst = [ _ for _ in range(1,N+1) ]

# for m in range(M):
#     i,j = map(int,input().split())
#     temp = lst[i-1:j]
#     temp.reverse()
#     lst[i-1:j] = temp

# print(*lst)


'''
1546 평균
'''

# n = int(input())

# lst = list(map(int,input().split()))

# lst.sort()

# M = lst[n-1]



# # for i in lst:
# #     i = i/M*100
# ''' 이거 자동으로 안에 있는 값이 바뀌지 않는다'''

# # print(lst)
# # total = sum(lst)/len(lst)

# # print(total)
    
# for i in range(len(lst)):
#     lst[i] = lst[i]/M*100 #인덱스로 접근해야 그 값이 수정된다

# total = sum(lst)/len(lst)

# print(total)

# ============================================

'''
27866 문자와 문자열
'''

# words = input()

# idx = int(input())

# print(words[idx-1])


'''
2743 단어 길이 재기
'''

# words = input()

# print(len(words))


'''
9086 문자열
'''

# T = int(input())

# for t in range(1,T+1):
#     words = input()

#     print(f'{words[0]}{words[len(words)-1]}')

'''
11720 숫자의 합
'''

# N = int(input())

# lst = list(map(int,input()))
# print(sum(lst))

'''
10809 알파벳 찾기
'''

# string = 'abcdefghijklmnopqrstuvwxyz'

# alp_lst = [_ for _ in string]

# chk = input()

# for alp in alp_lst:
#     print(chk.find(alp), end = ' ')


'''
2675 문자열 반복
'''

# T = int(input())

# for t in range(T):
#     N,S = map(str,input().split())
#     n = int(N)


'''
1152 단어의개수
'''
# words = input().strip()
# word_lst = list(words.split())
# print(len(word_lst))


'''
2908 상수
'''

# a,b = input().split()

# num1 = int(a[::-1])
# num2 = int(b[::-1])

# num_lst = [num1,num2]
# print(max(num_lst))

'''
5622 다이얼
'''

# alp_dic = {
#     'A':2,
#     'B':2,
#     'C':2,
#     'D':3,
#     'E':3,
#     'F':3,
#     'G':4,
#     'H':4,
#     'I':4,
#     'J':5,
#     'K':5,
#     'L':5,
#     'M':6,
#     'N':6,
#     'O':6,
#     'P':7,
#     'Q':7,
#     'R':7,
#     'S':7,
#     'T':8,
#     'U':8,
#     'V':8,
#     'W':9,
#     'X':9,
#     'Y':9,
#     'Z':9
# }

# string = input().strip()
# alp_lst = [s for s in string]
# num_lst = [] 

# for alp in alp_lst:
#     num_lst.append(alp_dic[alp])
# total = sum(num_lst)+len(num_lst)
# print(total)    

'''
11718 그대로 출력하기 try와 except 활용!
'''

# while True:
#     try:
#         a=input()
#         print(a)
#     except:
#         break

'''
3003 킹, 퀸, 룩, 비숍, 나이트, 폰
'''

# right_dic = {
#     'k':1,
#     'q':1,
#     'l':2,
#     'b':2,
#     'n':2,
#     'p':8
# }

# chs_lst = [1,1,2,2,2,8]

# lst = list(map(int,input().split()))

# cor_lst = []
# for i in range(len(lst)):
#     num = chs_lst[i]-lst[i]
#     cor_lst.append(num)

# print(*cor_lst)

'''
10988 팰린드롬
'''

# words = input()
# rev = words[::-1]

# if words == rev:
#     print(1)
# else:
#     print(0)