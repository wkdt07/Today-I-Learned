T = int(input())

def dfs(i,j,ans,cnt = 1):
    # ans += arr[i][j]
    if cnt == 7:
        ans_set.add(ans)
        return
    for d in dir:
        ni,nj = i+d[0],j+d[1]
        if ni in range(4) and nj in range(4):
            dfs(ni,nj,ans+arr[ni][nj],cnt+1)

for t in range(1,T+1):
    arr =[input().split() for _ in range(4)]
    ans_set = set()
    dir = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(4):
        for j in range(4):
            dfs(i,j,arr[i][j])

    print(f'#{t} {len(ans_set)}')