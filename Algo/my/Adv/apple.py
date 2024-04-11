T = int(input())

from collections import deque as dq

def eat(cnt = 0):
    t = 0
    now = 0,0
    while t < apple_num:
        next_target = apples[t]
        i,j = now
        ni,nj = next_target

        di = -(ni-i) # 둘의 곱이 -가 되려면 이렇게 해야함
        dj = -(nj-j)

        now_d = cnt % 4 # 현재 이동 방향

        turn_i = 0
        turn_j = 0

        d_tmp = now_d
        if di:
            while dir[d_tmp][0] * di >= 0:
                turn_i += 1
                d_tmp = (cnt+turn_i) % 4

        d_tmp = now_d
        if dj:
            while dir[d_tmp][1] * dj >= 0:
                turn_j += 1
                d_tmp = (cnt+turn_j) % 4

        turn = max(turn_i,turn_j)

        now = next_target

        cnt += turn

        t += 1
    return cnt
for tc in range(1,T+1):
    N = int(input())

    arr = [list(map(int,input().split())) for _ in range(N)]

    apple_num = 0
    apples = [[] for _ in range(11)]
    for i in range(N):
        for j in range(N):
            if arr[i][j]: # 값이 존재하면
                apples[arr[i][j]].append(i)
                apples[arr[i][j]].append(j)
                apple_num = max(apple_num,arr[i][j])

    apples = apples[1:apple_num+1] # 사과들 좌표(리스트 형태
    # print(apples)
    dir = [(0,1),(1,0),(0,-1),(-1,0)]

    cnt = 0
    result = eat()
    print(f'#{tc} {result}')
    # d = cnt%4 #시작할 때 방향 고정

