T = int(input())


# def bridge(n,m):
#     '''
#     for i in range(1,m-n+1):
#         for j in range(i,m-n):
#     '''
#     cnt = 0
#     while j>0 and i <= m-n:
#         j = m-n+1
#         i = 0
#
#         i += 1
#         j -= 1
#         cnt += 1
#
#     return cnt

# for t in range(T):
#     n,m = map(int,input().split())
#

'''
첫 번째가 선택할 수 있는 경우의 수 -> 1번~m-n-1번, 선택한걸 i라 한다면
두 번째가 선택할 수 있는 경우의 수 -> i+1번~m-n번, j
세 번째가 선택할 수 있는 경우의 수 -> j+1번~m-n+1번 , k
.
.
.

'''