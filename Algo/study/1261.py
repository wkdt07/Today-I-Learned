import sys
input = sys.stdin.readline
from heapq import heappush, heappop


M,N = map(int,input().split()) # j범위와 i 범위

# arr = []

arr = [list(map(int,input().strip())) for _ in range(N)]
# print(arr)
start = (0,0)
end = (N-1,M-1)

dir = [(1,0),(0,1),(-1,0),(0,-1)]

INF = int(1e9)

distance = [[INF for _ in range(M)] for _ in range(N)]
vst = [[0]*M for _ in range(N)]

distance[0][0] = 0
pq = []
heappush(pq,(0,start))

while pq:
    now_dist,(now_i,now_j) = heappop(pq)
    if (now_i,now_j) == end:
        break
    if vst[now_i][now_j]:
        continue
    if now_dist > distance[now_i][now_j]:
        continue
    vst[now_i][now_j] = 1
    # distance[now_i][now_j] = now_dist
    for d in dir:
        ni,nj = now_i + d[0],now_j + d[1]
        if ni in range(N) and nj in range(M):
            new_dist = now_dist + arr[ni][nj]
            if new_dist > distance[ni][nj]:
                continue
            distance[ni][nj] = new_dist
            heappush(pq, (new_dist,(ni,nj)))

print(distance[end[0]][end[1]])