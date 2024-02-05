T = int(input())

for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    lst = []
    for i in range(N):
        for j in range(N):
            # direct = [(1,0),(1,1)]
            # for dir in direct:
            #     dj,di =dir
                # for k in range(1,N+1):
                #     for l in range(N+1):
                #         ni = i + k*di
                #         nj = j + l*dj
                #         if (i == ni and j == nj):
                #             continue
                #         if (0<=ni<N and 0<=nj<N) and (arr[i][j] == arr[ni][nj]):
                #             area = (ni-i+1)*(nj-j+1)
                #             lst.append(area)
            for ni in range(i+1,N):
                for nj in range(j,N):
                    if (i == ni and j == nj):
                        continue
                    if (0<=ni<N and 0<=nj<N) and (arr[i][j] == arr[ni][nj]):
                        area = (ni-i+1)*(nj-j+1)
                        lst.append(area)

            # 어차피 1씩 늘어나는거면 for문 안 쓰고 range 처리 해도 된다.


    max_v = max(lst)
    cnt = lst.count(max(lst))
    print(f'#{t} {cnt}')


