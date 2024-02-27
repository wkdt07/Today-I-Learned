T = int(input())

dir = [(0,1),(1,0)]


def min_sum(s,cnt = 1):
    global path
    global min_v
    i,j = s
    # path.append(arr[i][j])
    if min_v <= sum(path):
        return

    if s == (N-1,N-1) and cnt == 2*N -1:
        if sum(path)<min_v:
            min_v = sum(path)
        # print(path)
        return
    for d in dir:
        ni,nj = i+d[0],j+d[1]
        if 0<=ni<N and 0<=nj<N:
            path.append(arr[ni][nj])
            min_sum((ni,nj),cnt+1)
            path.pop()


for t in range(1,T+1):
    N = int(input())

    maxlev = 2*N - 1

    arr = [list(map(int,input().split())) for _ in range(N)]
    # sum_v = arr[0][0]
    s = (0,0)
    path = [arr[0][0]]
    min_v = float('inf')
    min_sum(s)
    # print(sum_lst)
    rst = min_v
    print(f'#{t} {rst}')