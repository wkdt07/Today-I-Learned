from heapq import heappush, heappop

T = int(input())

for tc in range(1,T+1):
    N,E = map(int,input().split()) # 마지막 노드 번호, 간선 수
    V = N+1 # 노드의 갯수
    INF = int(1e9)
    vst =  [INF]*V
    arr = [[] for _ in range(V)]
    for _ in range(E):
        s,e,w = map(int,input().split())
        arr[s].append([w,e])

    start = 0
    vst[start] = 0
    q = []
    heappush(q,[0,start])
    while q:
        # 가지치기 해줘야 함
        w,now = heappop(q)
        if vst[now] < w:
            continue

        for w_add,next_node in arr[now]:
            w_temp = w + w_add
            if vst[next_node] > w_temp:
                vst[next_node] = w_temp
                heappush(q,[w_temp,next_node])

    print(f'#{tc} {vst[N]}')





