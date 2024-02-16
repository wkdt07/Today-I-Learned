# k번 이하의 버스 탑승으로 출근할 수 있는 지역 = 출근하기 편한 지역
# visited에서 간선 수 체크하고 그게 k인 (인덱스-1)만 뽑으면 되겠다.

from collections import deque

def bfs(s):
    q = deque([])
    q.append(s)
    visited[s] = 1

    while q:
        t = q.popleft()

        for k in arr[t]:

            if not visited[k]:
                q.append(k)
                visited[k] = visited[t] + 1
    return visited


N,M = map(int,input().split()) # N은 노드 수, M은 모든 간선 수

visited = [0] * (N+1)

arr = [[] for _ in range(N+1)]
for _ in range(M):
    i,j = map(int,input().split())
    arr[i].append(j)
    arr[j].append(i) # 방향성 없음

# print(arr)
R,K = map(int,input().split()) #R은 현재 위치

cnt = 0
for i in bfs(R)[1:]:
    if i <= K+1:
        cnt += 1

print(cnt)
