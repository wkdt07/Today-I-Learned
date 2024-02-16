# 1은 벽 0은 통로 2 출발 3 도착
from collections import deque

T = int(input())
def bfs(s,e):
    dir = [(0,1),(0,-1),(1,0),(-1,0)]
    q = deque([])
    q.append(s)
    a = s[0]
    b = s[1]
    visited = [[0]*N for _ in range(N)]
    visited[a][b] = 1

    while q:
        t = q.popleft()
        i = t[0]
        j = t[1]
        if t == e:
            ei = e[0]
            ej = e[1]
            return visited[ei][ej] - 2
        for n in dir:
            ni = i + n[0]
            nj = j + n[1]
            if not (0<=ni<N and 0<= nj < N):
                continue
            else:
                if arr[ni][nj] == 1:
                    continue
                else:
                    if not visited[ni][nj]:
                        q.append([ni,nj])
                        visited[ni][nj] = visited[i][j] + 1

                    else:
                        continue
    return 0

for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    s = []
    e = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                s.extend((i,j))
            if arr[i][j] == 3:
                e.extend((i,j))

    print(f'#{t} {bfs(s,e)}')


