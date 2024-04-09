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
from copy import deepcopy as dc
T = int(input())
# todo 수확할 수 있는 공간이면 통과할 수 있다는걸 적용해야함
def bfs(start,start_direction,cnt = 1):
    global max_v
    now_v = 0
    agri = dc(arr)  # 몇 번 경작했는지 확인용
    arr_tmp = dc(arr)
    q = [(start,start_direction,cnt)]
    q = dq(q)
    seed = [] # 씨를 심어놓은 좌표
    while q:
        # todo 현재 농지가 빈 농지이고, 로봇이 다음 농지로 이동할 수 없을 경우 아무것도 하지 않고 현재 위치에서 머무른다.
        for si,sj in seed:
            arr_tmp[si][sj] += 1 # 씨앗 키우기

        now,now_dir,now_day = q.popleft() # 현재위치, 현재 방향, 현재 날짜

        i, j = now
        # 우선 움직임 여부부터 확인
        if now_day == M+1: # 가동일수 M일이 끝난다면
            # if arr_tmp[i][j] >= agri[i][j]+3:
            #     now_v += 1 # 마지막날까지 수확
            max_v = max(now_v,max_v)
            break

        for p in range(-1,3):
            flag = False
            next_dir = (now_dir + p) % 4
            next_d = dir[next_dir]
            ni,nj = now[0] + next_d[0],now[1] + next_d[1]
            if ni in range(N) and nj in range(N):
                if (not arr_tmp[ni][nj] and (ni,nj) not in seed) or arr_tmp[ni][nj] >= agri[ni][nj] + 3 : # 빈 농지거나, 수확이 가능하면 -> 거기로 움직일 수 있음
                    flag = True # 움직일 수 있는 공간이 있음
                    break # 움직일 방향을 잡아놓고 끝
        # flag = False # 움직일 수 있는지 판단 여부

# todo 이미 씨가 뿌려져 있는데 0으로 나오는 지역이 있을 수 있으니깐 이거 조심
        # 오전
        if arr_tmp[i][j] >= agri[i][j] + 3: # 수확 가능하면, # 시작 값이 1이기 때문에 그냥 +1 해줌 todo 확인 필요
            now_v += 1
            arr_tmp[i][j] = 0
            seed.remove((i,j))
        else: # 수확할 수 없으면 -> 이 안에 다음 방향이 들어가면 안되지.
            # 경작지 확인
            if not arr_tmp[i][j] and (i,j) not in seed: # 현재가 경작할 수 있는 지역이면
                if flag: # 이동이 가능할 경우
                    seed.append((i,j))
                    agri[i][j] += 1 # todo 여기서 씨 심기 횟수를 늘려놔야 한다.
                    arr_tmp[i][j] = -1 # 씨 심기
                else:
                    pass

            # else: # 현재 농지가 수확할 수도 없고, 빈 농지도 아니라면 -> 경우가 없음

        # 움직일 수 있는지 여부 확인
        # 방향을 4의 나머지로
        # 방향은 인덱스가 a라면 -1,0,1,2 순서

            #     pass

        # 여기부턴 오후
        if flag: # 움직일 수 있는 공간이 있으면
            next_node = (ni, nj)
            q.append((next_node, next_dir , now_day+1))
        else:
            q.append((now,now_dir,now_day+1))

        # 모든 씨 심은 곳 값 += 1

for tc in range(1,T+1):
    N,M = map(int,input().split()) # N은 지형 가로세로, M은 일수

    arr = [list(map(int,input().split())) for _ in range(N)]


    toil = [] # 경작할 수 있는 수
    for i in range(N):
        for j in range(N):
            if not arr[i][j]:
                toil.append((i,j))
    # print(toil)
    dir = [(0,1),(-1,0),(0,-1),(1,0)] # (앞이 위로(-1,0)일 때의 기준 오앞왼뒤)
    max_v = 0

    for start in toil:
        for start_direction in range(4):
            bfs(start,start_direction)

    # bfs((3,3),2)

    print(f'#{tc} {max_v}')
    # start_direction : 인덱스 형태















