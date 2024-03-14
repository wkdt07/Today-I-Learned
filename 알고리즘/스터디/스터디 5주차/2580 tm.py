# 스도쿠
# -*- coding:utf-8 -*-
from collections import deque as dq
N = 9
from copy import deepcopy as dcopy
arr = [list(map(int,input().split())) for _ in range(9)]

target_lst = [] # 0이 있는 위치를 i,j로
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            target_lst.append((i,j))

# cands = [i for _ in range(1,10)]
# 행과 열과 3*3 결과 검사의 교집합이 해당 좌표에 들어갈 수 있는 값

vst = dcopy(arr)
finish = False # 한 번만 하려고
def candidate(arr,target): # candidate를 생성하는 함수
    cands = [_ for _ in range(1,10)]
    i,j = target
    # 행 검사
    for nj in range(N):
        if arr[i][nj] in cands:
            cands.remove(arr[i][nj])
    for ni in range(N):
        if arr[ni][j] in cands:
            cands.remove(arr[ni][j])
    k_i = i // 3
    k_j = j // 3
    for ni in range(3*k_i,3*k_i+3):
        for nj in range(3*k_j,3*k_j+3):
            if arr[ni][nj] in cands:
                cands.remove(arr[ni][nj])
    return cands

def bt(vst,target_lst=target_lst):
    global finish

    if finish: # 딱 한 번만 출력
        return

    if not target_lst:
        finish = True
        for l in range(9):
            print(*vst[l])
        return

    # for target in target_lst:
    target = target_lst.pop()
    cands = candidate(vst,target)# 사용 가능한 candidate
    if not cands:
        return
    cands = dq(cands)
    cand = cands.popleft()
    i,j = target
    vst[i][j] = cand
    bt(vst,target_lst)
    cands.append(cand)
    target_lst.append(target)
    return
bt(vst)

# 행 검사
# 열 검사
# 3*3 검사 -> 해당 좌표 확인


