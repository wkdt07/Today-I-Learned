# -*- coding:utf-8 -*-

from collections import deque as dq

# 시작은 0,0

N = int(input()) # 보드의 크기

K = int(input()) # 사과의 갯수

apples = []
for _ in range(K):
    i,j = map(int,input().split())
    i -= 1
    j -= 1
    apples.append((i,j))

L = int(input()) # 회전 횟수

rules = dq() # 시간과 방향
for _ in range(L):
    x,turn = input().split()
    x = int(x)
    rules.append((x,turn))

time = 0

direction = [(0,1),(1,0),(0,-1),(-1,0)] # 오른쪽으로 돌면 +1 ,왼쪽으로 돌면 -1

now_d = direction[0] # 현재 진행방향

# 그럴거면 그냥 snake라는 하나의 deque로 만들자
snake = dq([(0,0)])
# head는 snake[0], tail은 snake[-1], 움직일 때, 머리는 appendleft, 꼬리는 popleft
while True:
    i,j = snake[0]
    time += 1
    ni, nj = i + now_d[0], j + now_d[1]
    # 변하는건 해당 시간이 '끝난 뒤에'
    if rules:
        x,turn = rules[0]
    else:
        x,turn = 0,0
    if time == x:
        rules.popleft()
        idx = direction.index(now_d)
        if turn == 'D':

            if idx == 3:
                idx -= 4
            now_d = direction[idx+1]
        else:
            now_d = direction[idx-1]


    if (ni,nj) in snake or ni not in range(N) or nj not in range(N): # 다음으로 가는 곳이 뱀의 영역이면, 혹은 영역 밖이면
        break
    else:
        if (ni,nj) in apples:
            apples.remove((ni,nj))
            snake.appendleft((ni,nj))
        else: # 그냥 맨 바닥일 떄
            snake.pop() # 꼬리 한 칸 없어지고
            snake.appendleft((ni,nj))

print(time)







