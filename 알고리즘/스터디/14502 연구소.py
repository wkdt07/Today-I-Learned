 #-*- coding:utf-8 -*-

from itertools import combinations as cb
from copy import deepcopy as dp
from collections import deque as dq
N,M = map(int,input().split()) # N:행 갯수, M: 열 갯수

arr = [list(map(int,input().split())) for _ in range(N)]

viruses = []
targets = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            targets.append((i,j))
        elif arr[i][j] == 2:
            viruses.append((i,j))
safe_zone_fst = len(targets)
dir = [(0,1),(1,0),(0,-1),(-1,0)]

cases = cb(targets,3)

max_v = -float('inf')

def virus(case):
    global max_v
    vst = dp(arr)
    for c in case:
        ci,cj = c
        vst[ci][cj] = 1
    q = dq(viruses)
    cnt = 0
    while q:
        i,j = q.popleft()
        for d in dir:
            k = 0
            while True:
                k += 1
                ni,nj = i + k*d[0], j + k * d[1]
                if not(0 <= ni < N and 0 <=nj<M):
                    break
                if vst[ni][nj] == 0:
                    vst[ni][nj] = 2
                    q.append((ni,nj))
                    cnt += 1
                elif vst[ni][nj] == 1:
                    break
                # 어차피 1이면 break 해야하고, 2면 continue 해야함 아니면 의미가 없어서
    safe_zone = safe_zone_fst - cnt - 3
    max_v = max(max_v, safe_zone)


for case in cases:
    virus(case)

print(max_v)




# 이 방법의 문제점 -> 감염된 놈이 다시 감염시키는걸 생각 안 함
# def virus(v,arr): # 싹 다 감염시키는 함수
#     global cnt
#     i,j = v # 바이러스의 좌표
#     for d in dir:
#         k = 0
#         while True:
#             k += 1
#             ni,nj = i+k*d[0],j+k*d[1]
#             if not(0 <= ni < N and 0 <=nj<N):
#                 break
#             if arr[ni][nj] == 1:
#                 break
#             elif arr[ni][nj] == 2:
#                 continue
#             else:
#                 arr[ni][nj] = 2
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] == 0:
#                 cnt += 1





# def solution(case):
#     global max_v
#     vst = dp(arr)
#     # for case in cases: # 벽을 세울 수 있는 곳의 좌표
#     for c in case:
#         i,j = c
#         vst[i][j] = 1
#     cnt = 0
#     for v in viruses:
#         virus(v,vst)
#     max_v = max(cnt,max_v)

# for case in cases:
#     # solution(case)









