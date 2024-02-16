# 1번 지역에서 N번 지역으로 출근
# T번 지역을 피하는 최소 환승횟수(간선수=visited -1)
from collections import deque

N,M = map(int,input().split()) # N은 지역수, M은 관계 수
vst = [0] *(N+1)
arr = [[] for _ in range(N+1)]

for _ in range(M):
    i,j = map(int,input().split())
    arr[i].append(j)
    arr[j].append(i)

T = int(input())

# print(arr)

def bfs(s,N,T):
    q = deque([])
    q.append(s)
    vst[s] = 1
    while q:
        t = q.popleft()
        if t ==  N:
            return vst
        if t ==  T:
            continue
        else:
            for k in arr[t]:
                if not vst[k]:
                    q.append(k)
                    vst[k] = 1 + vst[t]

    return -1

result = bfs(1,N,T)[N] - 1
print(result)