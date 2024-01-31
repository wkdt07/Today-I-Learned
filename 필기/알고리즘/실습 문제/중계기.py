T = int(input())
import math

for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N+1)]
    # print(*arr)
    h_lst = []
    for i in range(N+1):
        for j in range(N+1):
            if arr[i][j] == 2:
                dev_i,dev_j = (i,j)
            if arr[i][j] == 1:
                h = (i,j)
                h_lst.append(h)
    # print(dev)
    # print(h_lst)

    dst_lst = []
    for h in h_lst:
        h_i,h_j = h
        di = h_i - dev_i
        dj = h_j - dev_j
        d = math.sqrt(di**2 + dj**2)
        dst_lst.append(d)

    # print(dst_lst)

    r = math.ceil(max(dst_lst))
    print(f'#{t} {r}')




