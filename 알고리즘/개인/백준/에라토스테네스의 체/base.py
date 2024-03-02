'''
#https://nahwasa.com/entry/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98-%EC%B2%B4-%ED%98%B9%EC%9D%80-%EC%86%8C%EC%88%98%ED%8C%90%EC%A0%95-%EC%8B%9C-%EC%A0%9C%EA%B3%B1%EA%B7%BC-%EA%B9%8C%EC%A7%80%EB%A7%8C-%ED%99%95%EC%9D%B8%ED%95%98%EB%A9%B4-%EB%90%98%EB%8A%94-%EC%9D%B4%EC%9C%A0
- 코드 구현
https://nahwasa.com/entry/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98-%EC%B2%B4-%ED%98%B9%EC%9D%80-%EC%86%8C%EC%88%98%ED%8C%90%EC%A0%95-%EC%8B%9C-%EC%A0%9C%EA%B3%B1%EA%B7%BC-%EA%B9%8C%EC%A7%80%EB%A7%8C-%ED%99%95%EC%9D%B8%ED%95%98%EB%A9%B4-%EB%90%98%EB%8A%94-%EC%9D%B4%EC%9C%A0
- 제곱근 사용 이유

n 이하의 소수를 구하기 위해선 단순히 2부터 시작하여 i의 배수를 지워버리면 된다.
그럼 i는 어디까지 계산되어야 하냐?
sqrt(i)까지.
왜?
n = a*b = m*m이라 하면 다음 3가지 경우가 존재
1. a<m , b>m
2. a>m , b<m
3. a=m , b = m
우리는 a와 b 중 *더 작은 수까지만* i를 늘려주면 된다. why? 어차피 a의 배수가 b라 이미 지워진 상태에서 b를 고려할 필요는 없다.(이건 아닌거 같은데)
최악의 경우라 해봤자 n의 약수가 1, m, n(=m*m) 이렇게 3개밖에 없으니, m까지만 계산하면 어차피 다 해결된다.
(편의상 a를 더 작은 값이라 하면)
a의 최대값은 m이다.
m = sqrt(n) 까지만 i를 계산하면 끝난다.

arr = [i for i in range(n)]
0과 1은 그냥 False
2부터 시작
'''
# n = int(input())
# m = int(n**(0.5)) # 해당 값을 int로 바꿔줘야 한다. 이러면 내림 처리됨.
# print(m)
# arr = [True for i in range(n+1)]
# arr[0],arr[1] = False,False
#
# for k in range(2,m+1): # 이건 왜 m+1일까?
#     j = 2
#     while k * j <= n: # 인덱스로 들어가서 n+1이 아니라 n이 되어야 한다.
#         arr[k*j] = False
#         j += 1
#
# print(arr)


import sys
from math import isqrt

def sieve_of_eratosthenes(N):
    prime_num = [True] * (N + 1)
    prime_num[0] = False
    prime_num[1] = False
    for i in range(2, isqrt(N) + 1):
        if prime_num[i]: # 만약 i가 소수라면
            for j in range(i*i, N+1, i): #i*i부터 거른다 i의 배수를 모두 거른다. why? i*a에서 a가 i보다 작은 수들은 이미 a의 배수에서 모두 걸러짐
                prime_num[j] = False
    return prime_num

N = int(sys.stdin.readline())
prime_num = sieve_of_eratosthenes(N)