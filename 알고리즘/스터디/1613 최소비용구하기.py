from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N = int(input()) # 도시 갯수
INF = int(1e9)
cities = [INF] * (N+1)
M = int(input()) # 버스 갯수
arr = [[] for _ in range(N+1)]
for m in range(M):
    s,e,w = map(int,input().split())
    arr[s].append([w,e])
start,end = map(int,input().split())
q = []
cities[start] = 0
heappush(q,[0,start]) # w와 now
while q:
    w,now = heappop(q)
    if cities[now] < w:
        continue
    for w_next,next in arr[now]:
        new_w = w + w_next
        if new_w < cities[next]:
            cities[next] = new_w
            heappush(q,[new_w,next])

print(cities[end])

