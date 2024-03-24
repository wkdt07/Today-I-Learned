from collections import deque

N = int(input()) # 컴퓨터 수
M = int(input()) # 간선 수

arr = [[] for _ in range(N+1)]

for _ in range(M):
    i,j = map(int,input().split())
    arr[i].append(j)
    arr[j].append(i)

# print(arr)

visited = [0]*(N+1)
def bfs(n):
    q = deque()
    visited[n] = 1
    q.append(n)

    while q:
        t = q.popleft()
        for k in arr[t]:
            if visited[k] == 0:
                visited[k] = 1
                q.append(k)
    result = visited.count(1)-1
    return result

print(bfs(1))

a = set()
