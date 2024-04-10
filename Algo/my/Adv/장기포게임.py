# from collections import deque
#
# T = int(input())  # 테스트 케이스의 수 입력
#
# for tc in range(1, T + 1):  # 각 테스트 케이스에 대해 반복
#     N = int(input())  # 장기판의 크기 입력
#     arr = [list(map(int, input().split())) for _ in range(N)]  # 장기판 정보 입력
#
#     # 포의 시작 위치 찾기
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 2:  # 포 발견
#                 sy = i
#                 sx = j
#                 break
#
#     # 상하좌우 이동을 위한 방향 설정
#     dy = [-1, 1, 0, 0]
#     dx = [0, 0, -1, 1]
#
#     q = deque([[sy, sx]])  # 큐 초기화 및 시작 위치 추가
#     visited = [[0] * N for _ in range(N)]  # 방문 여부를 기록할 배열 초기화
#     visited[sy][sx] = 1  # 시작 위치 방문 표시
#
#     lst = []
#     def BFS():
#         while q:  # 큐가 빌 때까지 반복
#             y, x = q.popleft()  # 큐에서 위치 추출
#             for d in range(4):  # 상하좌우 방향에 대해 반복
#                 is_jump = False  # 뛰어넘기 여부 초기화
#                 for k in range(1, N):  # 이동 거리에 따라 반복
#                     ny = y + dy[d] * k  # 다음 위치의 행 좌표 계산
#                     nx = x + dx[d] * k  # 다음 위치의 열 좌표 계산
#                     # 다음 위치가 유효하고, 현재 위치보다 이동 횟수가 적거나 같은 경우에만 진행
#                     if 0 <= ny < N and 0 <= nx < N and visited[y][x] <= 3 and visited[ny][nx] <= visited[y][x]:
#                         if arr[ny][nx] == 1:  # 쫄을 만난 경우
#                             if is_jump == False:  # 첫번째 쫄을 만남
#                                 is_jump = True  # 뛰어넘기 가능하도록 표시
#                             else:  # 두번째 쫄을 만남
#                                 if not visited[ny][nx]:  # 방문한 적 없는 경우에만 처리
#                                     visited[ny][nx] = visited[y][x] + 1  # 이동 횟수 갱신
#                                     q.append([ny, nx])  # 큐에 다음 위치 추가
#                                     lst.append((ny,nx))
#                                     break
#                         if arr[ny][nx] == 0 and is_jump == True and arr[ny][nx] == 0 and not visited[ny][nx]:
#                             visited[ny][nx] = visited[y][x] + 1  # 이동 횟수 갱신
#                             q.append([ny, nx])  # 큐에 다음 위치 추가
#
#         kill = 0  # 잡은 쫄의 수 초기화
#         for i in range(N):
#             for j in range(N):
#                 if arr[i][j] == 1 and 0 < visited[i][j] <= 4:
#                     kill += 1
#         return kill  # 잡은 쫄의 수 반환
#
#     print(arr)
#     print(visited)
#     print(f'#{tc}', BFS())  # 결과 출력


from copy import deepcopy as dc

T = int(input())

def game(s,vst,cnt = 0):
    global max_v
    # global eat
    global eat_lst

    i,j = s

    if cnt == 3:
        return


    for d in dir:
        p = 1 # 첫 번째 돌이 나오는 경우를 p1, 두번 째를 p2로 하고, p1+1~p2까지만 움직일 수 있음
        di,dj = d
        # ni,nj = i+di*p,j+dj*p
        st = 0
        st_lst = []
        while st <=2: # 움직일 수 있는 범위인 p1과 p2 구하기
            ni, nj = i + di * p, j + dj * p

            if not(0<=ni<N and 0<=nj<N): # 끝까지 가버렸으면
                break
            if st == 2: # 돌을 2개 발견했으면
                break
            if vst[ni][nj] == 1:
                st += 1
                st_lst.append(p)
            p += 1

        # 돌이 1개 이상인 경우에만 움직일 수 있다.
        if st_lst:
            if len(st_lst) == 1:
                p1 = st_lst[0]
                p2 = p-1 # 끝까지 간 경우

            elif len(st_lst) == 2:
                p1 = st_lst[0]
                p2 = st_lst[1]


            for k in range(p1+1,p2+1): # 갈 수 있는 모든 방향에 대해서
                ni,nj = k*di+i,k*dj+j
                if vst[ni][nj] == 1: # 갈 수 있는 공간에 돌이 있다면
                    # if (ni,nj) not in eat_lst:
                    vst[ni][nj] = 2
                    eat_lst.append((ni,nj))
                    game((ni,nj),vst,cnt+1)
                    vst[ni][nj] = 1
                    # eat_lst.remove((ni,nj))


                if not vst[ni][nj]: # 공간 없이 그냥 갈 수 있는 곳이면
                    vst[ni][nj] = 2 # 방문표시만 한다
                    game((ni,nj),vst,cnt+1)
                    vst[ni][nj] = 0

for tc in range(1,T+1):
    N = int(input())
    arr= [list(map(int,input().split())) for _ in range(N)]
    cha_lst = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                s = (i,j)
    # max_v = -float('inf')
    vst = dc(arr)
    dir  = [(1,0),(0,1),(-1,0),(0,-1)]
    # 포는 최대 3번까지 이동 가능
    eat_lst = []

    game(s,vst)
    # print(eat_lst)
    eat_lst = set(eat_lst)
    eat = len(eat_lst)
    print(f'#{tc} {eat}')

