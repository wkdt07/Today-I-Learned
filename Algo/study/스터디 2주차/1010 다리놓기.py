# from math import factorial as fac
import sys

T = int(sys.stdin.readline())

def fac(n):
    result = 1
    if n == 0 or n == 1:
        return result

    return n * fac(n-1)

for t in range(1,T+1):
    n,m = map(int,sys.stdin.readline().split())
    result = int(fac(m)/(fac(m-n)*fac(n)))
    print(result)

'''
첫 번째가 선택할 수 있는 경우의 수 -> 1번~m-n-1번, 선택한걸 i라 한다면
두 번째가 선택할 수 있는 경우의 수 -> i+1번~m-n번, j
세 번째가 선택할 수 있는 경우의 수 -> j+1번~m-n+1번 , k
.
.
.
그냥 뽑아놓으면 알아서 정렬된다
mCn
'''