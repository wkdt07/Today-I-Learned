# -*- coding:utf-8 -*-

from itertools import combinations as cb
from copy import deepcopy as dp
from collections import deque as dq



from itertools import combinations
from collections import deque
from copy import deepcopy

# 상하좌우 방향배열
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def 좌표받기():
    for row in range(N):
        for col in range(M):
            if matrix[row][col] == 2:
                virus_list.append((row, col)) # 바이러스 위치 virus_list
            if matrix[row][col] == 0:
                empty_list.append((row, col)) # 타겟 위치 empty_list
            # else:
            #     visited[row][col] = 1


def bfs(temp,viruses):
    # global max_v
    temp_v = 0
    q = deque(viruses)
    # q.append((y, x))
    while q:
        cy, cx = q.popleft()
        for dir in direction:
            ny, nx = cy+dir[0], cx+dir[1]
            if ny not in range(N) or nx not in range(M): # 범위 내가 아니라면
                continue # dir 바꿔라
            if temp[ny][nx] != 0: # 감염시킬 수 있는 공간이 아니면
                continue # 방향 바꿔라
            # if visited[ny][nx] == 1:
            #     continue
            q.append((ny, nx))
            temp[ny][nx] = 2
            temp_v += 1 # 감염

    return temp


N, M = map(int, input().split())
# 맵 그리기
matrix = [list(map(int, input().split())) for _ in range(N)]

# 2 좌표 가져오기
virus_list = []
# 0 좌표 가져오기
empty_list = []
# 최대 크기 max_v
max_v = -float('inf')
좌표받기()

# matrix deepcopy

for idx in combinations(empty_list, 3):

    # print(idx)
    temp = deepcopy(matrix)
    # 벽으로 만들고
    for i in range(3):
        temp[idx[i][0]][idx[i][1]] = 1 # 벽으로 만들기

    # 바이러스 돌 때마다 다시 돌리고
    # for virus in virus_list:
    #     temp = bfs(virus[0], virus[1],temp)
        # 바이러스 싹 다 감염시키고 나서 계산해야함
    temp = bfs(temp,virus_list)
    safe_zone = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                safe_zone += 1
    # print(temp)
    max_v = max(max_v,safe_zone)
print(max_v)

    # matrix 초기화
    # matrix = deepcopy(temp)
    # visited = deepcopy(temp)
# print(max_v)
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









