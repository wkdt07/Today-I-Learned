import copy

T  = int(input())


'''
아침에 할 수 있는 일
1. 씨 심기 (로봇이 다음 농지로 이동할 수 있는 경우, 지금 있는 위치에
2. 다음으로 이동할 수 없고, 현재가 빈 농지면 가만히
3. 현재 농지에 씨가 열릴 경우, 수확한다. 수확하면 여기 값은 0으로
'''



# def mor(arr,s,cur_dir):
#     global cnt
#     days = M
#     next_pos = False
#
#     while days:
#         days -= 1
#         i,j = s
#         di, dj = cur_dir
#         next_pos = False #다음에 갈 수 있는지 여부 갱신
#         # 씨앗 갱신
#         for seed in seed_point:
#             if arr[seed[0]][seed[1]] < 4: # 덜 자란 애들만
#                 arr[seed[0]][seed[1]] += 1 # 4일 째 되면 수확물이 다 자란다
#
#         # 다음 방향 조정
#         if dj:
#             dir_cands = [[dj, di], [di, dj], [-dj, di], [-di, -dj]]  # dj가 0이 아닐 때 맞음
#             for d in dir_cands:
#                 ni, nj = i + d[0], j + d[1]
#                 if (0 <= ni < N and 0 <= nj < N) and (arr[ni][nj] == 0 or arr[ni][nj] == 4): # 범위 내에서 농산물이 있거나, 아무것도 안 심은 농지일 때
#                     next_d = d
#                     next_pos = True
#                     break  # 얜 밖에 있는게 맞다.
#         else:
#             dir_cands = [[dj, -di], [di, dj], [dj, di], [-di, -dj]]
#             for d in dir_cands:
#                 ni, nj = i + d[0], j + d[1]
#                 if (0 <= ni < N and 0 <= nj < N) and (arr[ni][nj] == 0 or arr[ni][nj] == 4):
#                     next_d = d
#                     next_pos = True
#                     break  # 얜 밖에 있는게 맞다.
#
#         # 현재 위치에 농산물이 없이, 0 일 때
#         if not arr[i][j]:
#             if next_pos: #다음 위치가 존재할 때, 씨앗 심기
#                 arr[i][j] = 1 # 씨 심기
#                 seed_point.append([i,j])
#                 ni,nj = i+next_d[0], j+next_d[1]
#                 cur_dir = next_d
#                 s = ni,nj
#                 continue
#
#
#         else: # 현재 위치가 농산물이 있는 경우
#             if arr[i][j] == 4:
#                 arr[i][j] = 0
#                 seed_point.remove([i,j])
#                 cnt += 1
#                 arr[i][j] = 0
#                 ni, nj = i + next_d[0], j + next_d[1]
#                 cur_dir = next_d
#                 s = ni, nj
#                 continue
#
#     return cnt
#
# for tc in range(1,T+1):
#     max_v = 0  # 최대값 초기화
#     N,M = map(int,input().split()) # N은 줄 수, M은 일 수
#     arr = [list(map(int,input().split())) for _ in range(N)]
#     dir = [(1,0),(0,-1),(-1,0),(0,1)]
#
#     start_lst = []
#     for i in range(N):
#         for j in range(N):
#             if not arr[i][j]:
#                 start_lst.append([i,j])
#
#
#     # print(start_lst)
#
#     max_v = 0
#     cnt_lst = [0]
#     for s in start_lst:
#         for c in range(4):
#             # sum_v = 0
#             # level = 0
#             seed_point = [] # 씨를 심은 장소
#             cur_dir = dir[c]
#             arrcopy = copy.deepcopy(arr)
#             cnt = 0
#             rst = mor(arrcopy,s,cur_dir)
#             # max_v = max(rst,max_v)
#             cnt_lst.append(rst)
#
#     print(f'#{tc} {max(cnt_lst)}')

# ** ydir, xdir, face는 직접 그려보면서 왜 이런 값이 나오는지를 확인해보길 바람.
# 지금 보는 방향에서 오앞왼뒤 이동했을때의 y offset
ydir = [
    # 오앞왼뒤
    (1, 0, -1, 0),  # 오
    (0, -1, 0, 1),  # 앞
    (-1, 0, 1, 0),  # 왼
    (0, 1, 0, -1)  # 뒤
]
# 지금 보는 방향에서 오앞왼뒤 이동했을때의 x offset
xdir = [
    # 오앞왼뒤
    (0, 1, 0, -1),  # 오
    (1, 0, -1, 0),  # 앞
    (0, -1, 0, 1),  # 왼
    (-1, 0, 1, 0)  # 뒤
]
# 지금 보는 방향에서 오앞왼뒤 이동하고 나서 보는 방향
face = [
    # 오앞왼뒤
    (3, 0, 1, 2),  # 오
    (0, 1, 2, 3),  # 앞
    (1, 2, 3, 0),  # 왼
    (2, 3, 0, 1)  # 뒤
]


def sim(y, x, dir):
    days = M
    cnt = 0
    seedcnt = [[0 for _ in range(N)] for _ in range(N)]  # seedcnt : 각 (y,x) 좌표에 몇번째 (K) 씨앗이 심어졌는지 기록
    seeds = []  # 씨앗들

    # M일동안 simulation
    while days > 0:
        harvested = False
        days -= 1  # 하루가 지났다
        size = len(seeds)
        # 모든 씨앗들 업데이트
        for _ in range(size):
            now = seeds.pop(0)  # 맨 앞에거 빼고
            now[2] += 1  # 날짜 하루 추가
            # K + 3일이 지났다면
            if now[2] == (3 + seedcnt[now[0]][now[1]]): #  3일 + K(심은 날짜)
                mapcopy[now[0]][now[1]] = 3  # 수확 가능하도록 설정
            else:
                seeds.append(now)  # 아니면 다시 queue(list)에 삽입
        # 지금 위치가 수확이 가능하다면
        if mapcopy[y][x] == 3:
            cnt += 1  # 수확 + 1
            mapcopy[y][x] = 0  # 빈 땅으로 변경
            harvested = True  # 이번 턴에 수확했다! 기록
        # 다음 위치 / 방향 확인
        nextdir = -1 # 이게 다음 방향의 디폴트값. 불가능할 때 -1
        for i in range(4):
            ny = y + ydir[dir][i]
            nx = x + xdir[dir][i]
            # 산이거나, 싹이 튼곳이면 못간다. (테두리는 모두 1이니 범위 검사는 필요 없음)
            if mapcopy[ny][nx] == 1 or mapcopy[ny][nx] == 2: # 싹이 튼 곳의 mapcopy는 2
                continue
            # 오앞왼뒤 우선순위로 갈수 있는곳 찾았으면 break
            nextdir = i
            break
        # 현재 이동이 가능하지 않다면 -> 다음날로
        if nextdir == -1:
            continue
            # 이동이 가능하고, 현재 위치가 빈 땅이면서, 여기서 오늘 수확한곳이 아니라면
        if mapcopy[y][x] == 0 and harvested == False:
            mapcopy[y][x] = 2  # 씨앗을 뿌리고
            seedcnt[y][x] += 1  # 여기에 씨앗을 뿌린 횟수 늘려주고 (K)
            seeds.append([y, x, -1])  # 씨앗 추가 (y좌표, x좌표, 날짜)
        y = y + ydir[dir][nextdir]  # 다음 Y
        x = x + xdir[dir][nextdir]  # 다음 X
        dir = face[dir][nextdir]  # 다음 방향
    return cnt

import copy
T = int(input())
for tc in range(1, T + 1):
    # input
    N, M = list(map(int, input().split()))
    MAP = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    # solve - 모든 위치에서 모든 방향으로 두기
    for i in range(N):
        for j in range(N):
            # 산이라면 pass
            if MAP[i][j] == 1:
                continue
            for d in range(4):
                # 돌릴때마다 원본 맵으로 복구 -> mapcopy를 simulation용 맵으로 사용
                mapcopy = copy.deepcopy(MAP)
                temp = sim(i, j, d)
                ans = max(temp, ans)
    # output
    print(f"#{tc} {ans}")



# T  = int(input())
#
#
# '''
# 아침에 할 수 있는 일
# 1. 씨 심기 (로봇이 다음 농지로 이동할 수 있는 경우, 지금 있는 위치에
# 2. 다음으로 이동할 수 없고, 현재가 빈 농지면 가만히
# 3. 현재 농지에 씨가 열릴 경우, 수확한다. 수확하면 여기 값은 0으로
# '''
#
#
#
# def mor(s,arr,level,seed_point,cur_d,sum_v=0): # 현재 위치도 받아야 다음으로 움직이든 말든 한다.
#     # 아직 움직이지 않는다.
#     global max_v
#     if level == M*2:
#         if sum_v > max_v:
#             max_v = sum_v
#         return
#
#     i,j = s
#     next_pos = False
#     di,dj = cur_d
#
#     # 만약 다음 움직일 곳이 갱신이 안 된다면 얘가 문제일 가능성이 큼
#
#     if not level % 2: #아침일 때
#         #1. 다음 장소로 이동이 가능하고, 현재 위치가 0일 때.
#
#         for seed in seed_point:
#             if arr[seed[0]][seed[1]] < 5:
#                 arr[seed[0]][seed[1]] += 1 # 4일 째 되면 수확물이 다 자란다
#
#         # 먼저 seed point들을 갱신해줘야함
#         if dj:
#             dir_cands = [[dj, di], [di, dj], [-dj, di], [-di, -dj]]  # dj가 0이 아닐 때 맞음
#             for d in dir_cands:
#                 ni, nj = i + d[0], j + d[1]
#                 if ((0 <= ni < N and 0 <= nj < N) and arr[ni][nj] == 0) or ((0 <= ni < N and 0 <= nj < N) and arr[ni][nj] == 5): # 어차피 아침에 농산물 자라기 때문에 x로 가도 전혀 상관 없음
#                     next_d = d
#                     next_pos = True
#                     break  # 얜 밖에 있는게 맞다.
#         else:
#             dir_cands = [[dj, -di], [di, dj], [dj, di], [-di, -dj]]
#             for d in dir_cands:
#                 ni, nj = i + d[0], j + d[1]
#                 if ((0 <= ni < N and 0 <= nj < N) and arr[ni][nj] == 0) or ((0 <= ni < N and 0 <= nj < N) and arr[ni][nj] == 5):
#                     next_d = d
#                     next_pos = True
#                     break  # 얜 밖에 있는게 맞다.
#
#         if not arr[i][j]:
#             if next_pos: #다음 위치가 존재할 때
#                 arr[i][j] = 1 # 씨 심기
#                 seed_point.append([i,j])
#                 mor(s, arr, level + 1, seed_point, cur_d, sum_v)
#
#             elif not next_pos: # 다음 위치가 존재하지 않을 때
#                 # ni,nj = i,j
#                 mor(s, arr, level + 1, seed_point, cur_d, sum_v + 1) # 존버
#
#
#         else: # 현재 위치가 농산물이 있는 경우
#             if arr[i][j] == 5:
#                 arr[i][j] = 0
#                 seed_point.remove([i,j])
#                 mor(s,arr,level+1,seed_point,cur_d,sum_v+1)
#                 arr[i][j] = 5
#                 seed_point.append([i,j])
#
#     else: # 밤일 때
#         '''
#         저녁에 할 수 있는 일
#         1.이동 가능한 곳은 빈 농지, 또는 곡식이 열린 농지이다. 산이거나 싹이 나는 농지인 경우 이동이 불가능하다.
#
#         2.만약, 이동 가능한 곳이 여러 개인 경우, 로봇의 오른쪽, 앞쪽, 왼쪽, 뒤쪽의 순서로 가장 먼저인 이동 가능한 곳으로 이동한다.
#
#         3.만약 이동 가능한 곳이 없는 경우 로봇은 이동하지 않고 현재 위치에 머무른다.
#         '''
#         if dj:
#             dir_cands = [[dj, di], [di, dj], [-dj, di], [-di, -dj]]  # dj가 0이 아닐 때 맞음
#             for d in dir_cands:
#                 ni, nj = i + d[0], j + d[1]
#                 if ((0 <= ni < N and 0 <= nj < N) and arr[ni][nj] == 0) or ((0 <= ni < N and 0 <= nj < N) and arr[ni][nj] == 5): # 이거 생각 좀 해보자. 갈 수 있는 지역.
#                     next_d = d
#                     next_pos = True
#                     break  # 얜 밖에 있는게 맞다.
#         else:
#             dir_cands = [[dj, -di], [di, dj], [dj, di], [-di, -dj]]
#             for d in dir_cands:
#                 ni, nj = i + d[0], j + d[1]
#                 if ((0 <= ni < N and 0 <= nj < N) and arr[ni][nj] == 0) or ((0 <= ni < N and 0 <= nj < N) and arr[ni][nj] == 5):
#                     next_d = d
#                     next_pos = True
#                     break  # 얜 밖에 있는게 맞다.
#         if next_pos: # 이동 가능한 곳이 존재할 경우, 이동해라
#             mor([i+next_d[0],j+next_d[1]],arr,level+1,seed_point,next_d,sum_v)
#         else: # 이동할 수 있는 곳이 없는 경우 존버
#             mor(s, arr, level + 1, seed_point, cur_d, sum_v)
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j]:
#                 vst_arr[i][j] = 1
#             else:
#                 start_lst.append([i,j])
#
#
# for tc in range(1,T+1):
#     max_v = 0  # 최대값 초기화
#     N,M = map(int,input().split()) # N은 줄 수, M은 일 수
#     arr = [list(map(int,input().split())) for _ in range(N)]
#     vst_arr = [[0]*N for _ in range(N)]
#     dir = [(1,0),(0,-1),(-1,0),(0,1)]
#
#     start_lst = []
#     for i in range(N):
#         for j in range(N):
#             if not arr[i][j]:
#                 start_lst.append([i,j])
#
#
#     # print(start_lst)
#
#
#     for s in start_lst:
#         for c in range(4):
#             # sum_v = 0
#             # level = 0
#             seed_point = [] # 씨를 심은 장소
#             cur_dir = dir[c]
#             # arr = vst_arr
#
#             mor(s,arr,0,seed_point,cur_dir)
#
#             for seed in seed_point:
#                 if arr[seed[0]][seed[1]] >0:
#                     arr[seed[0]][seed[1]] = 0
#
#     print(f'#{tc} {max_v}')
