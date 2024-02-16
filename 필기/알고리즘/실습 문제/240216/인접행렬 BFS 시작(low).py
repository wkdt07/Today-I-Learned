from collections import deque

N = int(input())
visited = [0]*(N)

adjL = [list(map(int,input().split())) for _ in range(N)]
arr = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if adjL[i][j] == 1:
            arr[i].append(j)

def bfs(s):
    p_lst = []
    q = []
    q = deque(q)
    q.append(s)
    visited[s] = 1
    while q:
        t = q.popleft()
        p_lst.append(t)

        for k in arr[t]:
            if not visited[k]:
                q.append(k)
                visited[k] = 1

            else:
                continue
    return p_lst


print(*bfs(0))