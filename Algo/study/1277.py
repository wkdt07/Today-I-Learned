
# 갈 수 있는 곳을 모두 찾아서 pq에 넣은 후 다익스트라


from math import sqrt as rt

import sys

input = sys.stdin.readline

N,W = map(int,input().split()) # N은 발전소 수. W는 전선 수
# N = int(N)
M = float(input()) # 줄의 제한 길이
# arr = [[] for _ in range()]
plants = []
# j,i = map(int,input().split())
# start = (i,j)
for _ in range(N):
    j,i = map(int,input().split())
    plants.append((i,j))

start,end = 0,N-1

# plants.sort(key = lambda x : x[0]) # i 기준으로 정렬

tunnel = {} # 이미 연결되어 있는 발전소
for _ in range(W):
    i,j = map(int,input().split())
    i -= 1
    j -= 1

    if tunnel.get(i): # 이미 키가 존재한다면
        tunnel[i].append(j)
    else:
        tunnel[i] = [j]

    if tunnel.get(j): tunnel[j].append(i)
    else: tunnel[j] = [i]




INF = float('inf')

dist = [INF] * N

dist[0] = 0

from heapq import heappush,heappop

pq = []


pq.append([0,0]) # 처음 거리와 시작점 인덱스를 pq에 연결
# 인덱스 기준으로 생각해야한다.

while pq:
    now_dist,now = heappop(pq)

    if now_dist > dist[now]:
        continue

    if now_dist > dist[-1]: # 현재 거리가 우리 최종 거리보다 길다면 더 볼 필요 없음
        continue

    i,j = plants[now]

    if tunnel.get(now): # 만약 연결되어 있는 곳이 있다면
        tun_lst = tunnel[now]

    # 이제 여기서 어떻게 연결을 해주냐...
    for next_node in range(N): # 싹 다 계산
        if not dist[next_node]: # 만약 0이라면 더이상 줄어들게 없으므로 continue -> 대형이 아이디어
            continue

        if now == next_node: # 현재랑 같은 값이면 continue
            continue


        if tunnel.get(now): # 만약 둘 사이가 연결되어 있다면
            if next_node in tun_lst:
                flag = False # 값이 바뀌었는지 여부. 이거 체크 안 하면 무한루프 남
                if dist[next_node] > now_dist:
                    flag = True
                    dist[next_node] = now_dist
                # dist[next_node] = min(dist[next_node],now_dist)
                if flag:
                    heappush(pq,[dist[next_node],next_node]) # 바뀌었다면 힙
                    continue
        ni,nj = plants[next_node]
        next_d = rt((ni-i)**2 + (nj-j)**2) # 연결되는 줄의 길이
        if next_d > M: # 줄의 길이가 너무 길다면
            continue

        next_dist = now_dist + next_d
        if next_dist >= dist[next_node]: # 계산한 값이 이미 계산되어 있는 값보다 크거나 같다면
            continue # 갱신해줄 필요 없음

        dist[next_node] = next_dist

        heappush(pq,([next_dist,next_node]))

print(int(dist[-1]*1000))