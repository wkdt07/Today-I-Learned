# 다익스트라
# 최소 연료 존재
# 터널이 존재 -> 얘 때문에 힙큐에서 계속 왕복할 수 있기 때문에 조심해야함
# vst를 쓰는게 좋음


from heapq import heappush, heappop


def ds():
    start = (0,0)
    sum_v = 0
    q = []
    heappush(q,[sum_v,start])
    dp[0][0] = 0
    vst = [start]
    dir = [(1,0),(0,1),(-1,0),(0,-1)]
    while q:
        # print(q)
        sum_v,now= heappop(q)
        i,j = now
        # if sum_v > dp[N-1][N-1]:
        #     continue
        if now == (N-1,N-1):
            return dp[i][j]
        if tunnel.get(now):
            for tun in tunnel[now]:
                ni,nj,fuel = tun
                if dp[ni][nj] > sum_v+fuel:
                    dp[ni][nj] = sum_v+fuel
                    heappush(q,[sum_v+fuel,(ni,nj)])
        for d in dir:
            ni,nj = i+d[0],j+d[1]
            if ni in range(N) and nj in range(N):
                dh = heights[ni][nj] - heights[i][j]
                if dh < 0 :
                    dh = 0
                elif dh > 0:
                    dh *= 2
                else:
                    dh = 1

                if dp[ni][nj] > sum_v + dh:
                    dp[ni][nj] = sum_v + dh
                    heappush(q,[sum_v+dh,(ni,nj)])


T = int(input())


for tc in range(1,T+1):
    N,M = map(int,input().split()) # N은 가로세로, M은 터널 갯수
    heights = [list(map(int,input().split())) for _ in range(N)]
    tunnel = {}
    for _ in range(M):
        ai,aj,bi,bj,fuel = map(int,input().split())
        ai,aj,bi,bj = ai-1,aj-1,bi-1,bj-1
        if tunnel.get((ai,aj)):
            tunnel[(ai,aj)].append((bi,bj,fuel))
        else: tunnel[(ai,aj)] = [(bi,bj,fuel)]

        if tunnel.get((bi, bj)):
            tunnel[(bi, bj)].append((ai, aj, fuel))
        else:
            tunnel[(bi, bj)] = [(ai, aj, fuel)]
    # print(tunnel)
    INF = float('inf')
    dp = [[INF]*N for _ in range(N)]
    dp[0][0] = 0

    min_v = ds()

    print(f'#{tc} {min_v}')