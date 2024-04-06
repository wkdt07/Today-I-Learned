from heapq import heappush, heappop
import sys
input = sys.stdin.readline

V,E = map(int,input().split()) #  노드 수와 간선 수

start = int(input())

arr = [[] for _ in range(V+1)]
for _ in range(E):
    s,e,w = map(int,input().split())
    arr[s].append([w,e])

pq = []

INF = float('inf')
vst = [INF]*(V+1)
vst[start] = 0
come = [0]*(V+1)
pq.append([0,start])
while pq:

    now_dist,now = heappop(pq)
    if come[now]:
        continue
    come[now] = 1

    if vst[now] < now_dist:
        continue
    for new_w,next in arr[now]:


        dist = now_dist + new_w
        if dist > vst[next]:
            continue
        vst[next] = dist
        heappush(pq,[dist,next])

for v in range(1,V+1):
    if vst[v] == INF:
        print('INF')
    else:
        print(vst[v])

