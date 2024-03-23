# -*- coding:utf-8 -*-
import sys
input = sys.stdin.readline
from collections import deque as dq
# 빙산의 갯수를 인덱스로 하는 vst 리스트를 만들고 거기에 죄표를 넣은 후, cnt가 거기에 닿으면 녹는 값을 넣는다
# arr외에도 각 좌표에 빼줘야하는 가중치 값을 넣어둘 이차원 배열이 하나 필요하다.
# 딕셔너리로 {좌표 : [현재 빙하 크기, [주위 빙산 좌표들], 가중치 = 4-len(좌표들)} 넣어둘까? 근데 가중치는 가장자리들의 경우엔 불가능.
# 만약 최악의 경우라도 두쪽나는건 10 이하로밖에 안 나옴
# 햇수 바뀔때마다 DFS 돌리면 된다.

dir = [(1,0),(0,1),(-1,0),(0,-1)]
# ice_set = set()

N,M = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]

# arr_cp = arr[:]
# ice_cnt = 0
# ice_lst = []

def bfs(i,j):
    global cnt
    cnt += 1
    q = dq()
    q.append([i,j])
    while q:
        i,j = q.popleft()
        for d in dir:
            ni,nj = i+d[0],j+d[1]
            if ni in range(N) and nj in range(M):
                if not vst[ni][nj] and arr[ni][nj]:
                    vst[ni][nj] = 1
                    q.append([ni,nj])
                elif not arr[ni][nj]:
                    melting_arr[i][j] += 1



year = 0
while True:
    cnt = 0
    vst = [[0] * M for _ in range(N)]
    melting_arr = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                # ice_cnt += 1 # 얼음의 총 갯수
                if not vst[i][j]:
                    vst[i][j] = 1
                    bfs(i,j)
    # melt_cnt = 0
    # todo 다 녹았는데도 아무것도 없을 때
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                arr[i][j] = max(0,arr[i][j]-melting_arr[i][j])
                # melt_cnt += 1

    if cnt >= 2:
        print(year)
        break
    if not cnt:
        print(0)
        break
    year += 1


# dir = [(1,0),(0,1),(-1,0),(0,1)]
# # ice_set = set()
#
# N,M = map(int,input().split())
#
# arr = [list(map(int,input().split())) for _ in range(N)]
# melting_arr= [[0]*M for _ in range(N)]
# arr_cp = arr[:]
# # ice_cnt = 0
# ice_lst = []
#
# for i in range(N):
#     for j in range(M):
#         if arr[i][j]: # 얼음이 있다면
#             melting = 0
#             for d in dir:
#                 ni,nj = i+d[0],j+d[1]
#                 if ni in range(N) and nj in range(M) and not arr[ni][nj]:
#                     melting += 1
#             ice_lst.append([i,j])
#             melting_arr[i][j] = melting
# def closed_dfs(i,j): # 없어질 때마다 확인하게 하는 함수
#     global ice_set
#     # global flag
#
#     for d in dir:
#         ni,nj = i + d[0],j+d[1]
#         if ni in range(N) and nj in range(M):
#             if arr[ni][nj] and not vst[ni][nj]:
#                 # cnt += 1 # cnt수는 무조건 빙산보다 많거나 같아야 함
#                 ice_set.add((ni,nj)) # 이 크기가 빙하 수랑 같아야 함. 아니라면 떨어져있는거
#                 vst[ni][nj] = 1
#                 closed_dfs(ni,nj)
#                 vst[ni][nj] = 0
# vst = [[0] * M for _ in range(N)]
#
# i,j = ice_lst[0]
#
# year = 1
# flag = True
# melting_copy = melting_arr[:]
# while flag:
#     year += 1
#     flag = True
#     melting_arr = melting_copy
#     for ice in ice_lst:
#         i,j = ice
#         arr_cp[i][j] = max(arr_cp[i][j]-melting_arr[i][j], 0)
#         # melting 갱신해줘야 하는데...
#         if not arr_cp[i][j]: # 얼음이 녹으면
#             for d in dir: # 녹는 정도 조절
#                 ni,nj = i+d[0],i+d[1]
#                 if ni in range(N) and nj in range(M) and melting_copy[ni][nj]:
#                     melting_copy[ni][nj] = melting_copy[ni][nj]+1
#             ice_lst.remove([i,j])
#             ice_set = set()
#             vst = [[0] * M for _ in range(N)]  # todo 스타트 부분 vst 해줘야 함, 이게 여기 들어가면 안됨. 체크할 때마다 해줘야지.
#             vst[i][j] = 1
#             ice_set = set()
#             closed_dfs(i,j)
#             # print(len(ice_set))
#             # print(len(ice_lst))
#             if len(ice_set) != len(ice_lst):
#                 flag = False
#
#         if not flag:
#             print(year)
#             exit(0)
#         if not ice_lst:
#             print(0)
#             exit(0)
#
#






# todo ice_set 생성해야함

