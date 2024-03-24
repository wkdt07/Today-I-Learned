import sys
from math import isqrt

def prime(N):
    prime_num = [True] * (N + 1)
    prime_num[0] = False
    prime_num[1] = False
    for i in range(2, isqrt(N) + 1):
        if prime_num[i]: # 만약 i가 소수라면
            for j in range(i*i, N+1, i): #i*i부터 거른다 i의 배수를 모두 거른다. why? i*a에서 a가 i보다 작은 수들은 이미 a의 배수에서 모두 걸러짐
                prime_num[j] = False
    return prime_num

N = int(sys.stdin.readline())
prime_num = prime(N)

stack = True # stack, B일 떄
cnt_b = 1
cnt_s = 0
if N > 1:
    for i in range(2,N+1):
        if not prime_num[i]:
            cnt_b += 1
            stack = True
        else:
            if stack:
                cnt_b -= 1
                stack = False
            else:
                stack = False



cnt_s = N - cnt_b

print(cnt_b,cnt_s)


# stack = 'B' # stack
# cnt_b = 1
# cnt_s = 0
# if N > 1:
#     for i in range(2,N+1):
#         if not prime_num[i]:
#             cnt_b += 1
#             stack = 'B'
#         else:
#             if stack == 'B':
#                 cnt_b -= 1
#                 stack = 'S'
#             else:
#                 stack = 'S'
#
# cnt_s = N - cnt_b
#
# print(cnt_b,cnt_s)

# words = ['B']
#
# for i in range(2,N+1):
#     if not prime_num[i]:
#         words.append('B')
#     else:
#         if words[-1] == 'B':
#             words.pop()
#             words.append('S')
#             words.append('S')
#         else:
#             words.append('S')
#             words.reverse()
#
# s = words.count('S')
# b = N - s
# print(b,s)
# if N == 1:
#     b = 1
#     s = 0
# elif N == 2:
#     b = 0
#     s = 2
# elif N == 3:
#     s = 3
#     b = 0
# else:
#     words_new = ['B' if not prime_num[i] else 'S' for i in range(4,N+1)]
#     words = ['S','S','S'] + words_new
#     b = words.count('B')
#     s = N - b
# print(b,s)


# import sys
# from math import sqrt as rt
#
# N = int(sys.stdin.readline())
#
#
# prime_num = [True] *(N+1)
# prime_num[0] = False
# prime_num[1] = False
#
# if N > 1:
#     m = int(rt(N))
#     for i in range(2,m+1):
#         if prime_num[i]:
#             j = 2
#             while i*j <=N:
#                 prime_num[i*j] = False
#                 j += 1
#
# words = ['B']
#
# for i in range(2,N+1):
#     if not prime_num[i]:
#         words.append('B')
#     else:
#         if words[-1] == 'B':
#             words.pop()
#             words.append('S')
#             words.append('S')
#         else:
#             words.append('S')
#             words.reverse()
#
# s = words.count('S')
# b = words.count('B')
#
# print(b,s)
#
# stack = 'B' # stack
# cnt_b = 1
# cnt_s = 0
# if N > 1:
#     for i in range(2,N+1):
#         if not prime_num[i]:
#             cnt_b += 1
#             stack = 'B'
#         else:
#             if stack == 'B':
#                 cnt_b -= 1
#                 stack = 'S'
#             else:
#                 stack = 'S'
#
# cnt_s = N - cnt_b
#
# print(cnt_b,cnt_s)

