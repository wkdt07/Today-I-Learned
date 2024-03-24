# 항상 다음 값이 더 커야 한다.
# bfs로 다음 값 구하기
# 만약 더 이상 갈 공간이 없거나, q가 다 떨어지면 종료
# level이 최대인 경우만 필요
# lev_1 lev_2 lev_3에서 현재 lev_4로 간다면 lev_1과 lev_2는 아예 필요가 없다.
# 단순 bfs로 풀 수도 있다만... 굳이?
# 특정 칸에 도달하고, 거기서 앞으로 갈 수 있는 최장길이의 값을 안다면 굳이 더 갈 이유가 없다.

import sys

sys.setrecursionlimit(250001) # N의 최대값은 50000이고, N*N의 최대 경우의 수
# -*- coding:utf-8 -*-
N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

dir = [(0,1),(1,0),(0,-1),(-1,0)]

# 이 문제에서 중요한건 '더 이상 안 가겠다'

dp = [[0]*N for _ in range(N)]

max_v = 1
def dfs(s):
    global max_v
    i,j = s

    if dp[i][j]: # 탐색해서 최장거리가 나와있는 위치라면, 혹은 이미 갔던 곳이라면
        return dp[i][j]

    dp[i][j] = 1
    for d in dir:
        ni,nj = i+d[0],j+d[1]
        if (0 <= ni < N and 0 <= nj < N) and arr[ni][nj] > arr[i][j]:
            dp[i][j] = max(dp[i][j],dfs((ni,nj))+1) # 1과 / 이후 최장거리와의 합 비교
            max_v = max(max_v, dp[i][j])
    return dp[i][j]


for i in range(N):
    for j in range(N):
        dfs((i,j))

print(max_v)

'''
4
14 9 12 10
1 11 5 4
7 15 2 13
6 3 16 8
'''
# 매번 dfs로 확인하는건 좀...
# def bfs(s,level = 0):
#     global max_level
#     vst = [s]
#     si,sj = s
#     s = (si,sj,level)
#     q = dq([s])
#
#     while q:
#         i,j,level = q.popleft()
#         max_level = max(max_level,level)
#         for d in dir:
#             ni,nj= i+d[0],j+d[1]
#             if (0<=ni<N and 0<=nj<N) and arr[ni][nj]>arr[i][j] and (ni,nj) not in vst:
#                 vst.append((ni,nj))
#                 q.append((ni,nj,level+1))
#
#
# max_level = -float('inf')
#
# for i in range(N):
#     for j in range(N):
#         s = i,j
#         bfs(s)
#
# print(max_level)

