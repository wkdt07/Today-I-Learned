# Kruskal

T = int(input())

for tc in range(1,T+1):


    V,E = map(int,input().split()) # V는 노드, E는 간선 갯수
    V += 1
    # 노드 번호는 0번부터 V번까지
    edges = [] # 간선 정보

    for _ in range(E):
        edges.append(list(map(int,input().split()))) # s,e,w를 간선 정보로 입력

    # 1. 정렬
    edges.sort(key=lambda x:x[2])

    parents = list(range(V))
    def find_set(x):
        if x == parents[x]:
            return x
        parents[x] = find_set(parents[x])
        return parents[x]


    def union(x,y):
        x = find_set(x)
        y = find_set(y)
        if x==y:
            return

        if x>y:
            parents[x] = y
        if x<y:
            parents[y] = x

    cnt = 0 # 노선 갯수가 V-1이 되면 그만둬야하니깐.
    sum_v = 0

    for s,e,w in edges:

        # 사이클 처리
        if find_set(s) == find_set(e):
            continue

        # 사이클이 아니라면

        cnt += 1
        sum_v += w

        # 방문처리
        union(s,e)

        # 종료조건
        if cnt == V-1:
            break

    print(f'#{tc} {sum_v}')