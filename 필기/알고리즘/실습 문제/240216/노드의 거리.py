# 간선 수 구하기

from collections import deque
T = int(input())

def bfs(s,e):
    q = deque([])
    q.append(s)
    vst[s] = 1

    while q:
        t = q.popleft()
        for k in arr[t]:
            if not vst[k]:
                q.append(k)
                vst[k] = vst[t] + 1
    if vst[e]:
        return vst[e] -1
    else:
        return 0

for t in range(1,T+1):
    V,E = map(int,input().split())
    vst = [0] * (V+1)
    arr = [[] for _ in range(V+1)]
    for _ in range(E):
        i,j = map(int,input().split())
        arr[i].append(j)
        arr[j].append(i)
    S,G = map(int,input().split()) #s,e
    print(f'#{t} {bfs(S,G)}')

