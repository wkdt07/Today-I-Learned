N = int(input()) # 노드의 수

adj = [list(map(int,input().split())) for _ in range(N)]

arr = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if adj[i][j]:
            arr[i].append(j)


ans = [0]

def dfs(now=0,cnt=0):
    if cnt == 2:
        print(*ans)
        return

    for k in arr[now]:
        ans.append(k)
        dfs(k,cnt+1)
        ans.pop()

dfs()