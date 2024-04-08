# 농지마다 싹이 나는데 걸리는 시간이 있다.
# k번째의 경우 3+k일 후에 곡식이 열린다, 얘도 농지에 정보로 넣어놔야 한다.

# 오전 ->
# 현재 농지가 빈 농지이고, 로봇이 다음 농지로 이동할 수 있는 경우, 씨를 심는다
# 현재 농지가 빈 농지이고, 로봇이 이동할 수 없는 경우, 아무것도 안 하고 현재 위치
# 현재 농지에 곡식이 열린 경우(flag == True), 수확하고 빈 농지로 만듦
# 1. 곡식이 열렸는지, 2. 이동 가능한지

# 오후 -> 이동하는 곳
# 상하좌우로 움직일 수 있음
# 이동 가능한 곳이 여러 개일 경우, 로봇이 바라보는 방향의 오앞왼뒤 순으로 이동
# 이동 가능한 곳이 없는 경우, 로봇은 이동하지 않고 현재 위치에 머무름

# 가장 많이 수확할 수 있는 시작 위치와 방향을 정하고, 이 때 수확횟수를 출력

# 시작 위치와 시작 방향 정하기.
# BFS로 level == M이라면 stop  # 날짜가 M이라면

# 시작 가능 위치와 방향이 곧 인자.
from collections import deque as dq
T = int(input())



for tc in range(1,T+1):
    N,M = map(int,input().split()) # N은 지형 가로세로, M은 일수

    arr = [list(map(int,input().split())) for _ in range(N)]


    toil = [] # 경작할 수 있는 수
    for i in range(N):
        for j in range(N):
            if not arr[i][j]:
                toil.append((i,j))
    dir = [(0,1),(-1,0),(0,-1),(1,0)] # (앞이 위로(-1,0)일 때의 기준 오앞왼뒤)
    max_v = 0
    # start_direction : 인덱스 형태
def bfs(start,start_direction,cnt = 0):
    global max_v
    now_v = 0
    agri = arr[:]  # 몇 번 경작했는지 확인용
    q = [(start,start_direction,cnt)]
    q = dq(q)
    while q:
        now,now_dir,now_day = q.popleft() # 현재위치, 현재 방향, 현재 날짜
        if now_day == M+1: # 가동일수 M일이 끝난다면
            max_v = max(now_v.max_v)
            break
        flag = False # 움직일 수 있는지 판단 여부

        i,j = now

        # 오전
        if arr[i][j] == agri[i][j] + 3 - 1: # 수확 가능하면, # 시작 값이 0이기 때문에 그냥 -1 해줌
            now_v += 1
            arr[i][j] = 0
            agri[i][j] += 1
        else:
            # 움직일 수 있는지 여부 확인
            # 방향을 4의 나머지로
            pass

        # 오후












