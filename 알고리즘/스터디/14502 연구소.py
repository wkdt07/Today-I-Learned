# -*- coding:utf-8 -*-

from itertools import combinations as cb
from copy import deepcopy as dp

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

dir = [(0,1),(1,0),(0,-1),(-1,0)]

def virus(v,arr): # 싹 다 감염시키는 함수
    i,j = v # 바이러스의 좌표
    for d in dir:
        k = 0
        while True:
            k += 1
            ni,nj = i+k*d[0],j+k*d[1]
            if arr[ni][nj] == 1:
                break
            elif arr[ni][nj] == 2:
                continue
            else:
                arr[ni][nj] == 2

    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                cnt += 1

    return cnt

cases = list(cb(targets,3))

def solution():
    vst = dp(arr)
    for case in cases:
        vst[]


print(cases)







