T = int(input())

for t in range(1,T+1):
    N,P = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    M = len(arr[0])
    direct = [(1,0),(-1,0),(0,1),(0,-1)]
    cnt_lst = []
    for i in range(N):
        for j in range(M):
            cnt = arr[i][j]
            for dir in direct:
                for p in range(1,P+1):
                # for p in range(P+1): # cnt = 0 으로 하고 이렇게 하면 방향마다 한 번씩 (i,j) 항이 4번 더해진다
                    dj,di = dir
                    ni = i + p*di
                    nj = j + p*dj

                    if 0<= ni < N and 0 <= nj < M:
                        cnt += arr[ni][nj]
            cnt_lst.append(cnt)

    maxv = max(cnt_lst)

    print(f'#{t} {maxv}')

