# 각 좌표마다 가중치가 다르다.
# 어차피 맨 처음 목적지에 나오는 가중치가 제일 크기 때문에, 그냥 그 때 break 하면 된다.... 아닌가?
# 일단 목적지에 도착했다, 라고 하면 그 이전에 어떤 지랄을 했던 간에 그게 가장 짧을거 같은데
# 방향은 오른쪽, 아래 2개밖에 없다

from heapq import heappop,heappush
dir = [(0,-1),(-1,0),(0,1),(1,0)]
T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    q = []
    INF = int(1e9)
    vst = [[INF]*N for _ in range(N)]
    vst[0][0] = 0
    heappush(q,[0,0,0]) # 시작 가중치와 위치
    # end = (N-1,N-1)
    while q:
        w,i,j = heappop(q) # 최종적으론 누적된 w가 출력
        now = i,j
        if w > vst[i][j]:
            continue
        # vst.append(now)
        # if now == end:
        #     break

        for d in dir:
            ni,nj = i+d[0],j+d[1]
            if not (0<=ni<N and 0<=nj<N):
                continue
            # if (ni,nj) in vst:
            #     continue
            next_w = 1
            if arr[i][j] < arr[ni][nj]:
                next_w += arr[ni][nj] - arr[i][j]
            total_w = w + next_w

            if total_w >= vst[ni][nj]:
                continue

            vst[ni][nj] = total_w
            heappush(q,[total_w,ni,nj])

    ans = vst[N-1][N-1]

    print(f'#{tc} {ans}')




