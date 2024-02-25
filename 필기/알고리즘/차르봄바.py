T = int(input())

dir = [(-1,0),(1,0),(0,-1),(0,1)]
for t in range(1,T+1):
    N,P = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # print(arr)
    maxv = 0
    for i in range(N):
        for j in range(N):
           sumv = arr[i][j]
           for d in dir:
               di = d[0]
               dj = d[1]
               for p in range(1,P+1):
                   ni = i + di*p
                   nj = j + dj*p
                   if 0<=ni <N and 0<=nj <N:
                       sumv += arr[ni][nj]
           maxv = max(maxv,sumv)

    print(f'#{t} {maxv}')
