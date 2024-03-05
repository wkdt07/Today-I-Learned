T = int(input())

for t in range(1,T+1):
    N,W = map(int,input().split())
    lst = list(map(int,input().split()))

    sum_v = 0
    for i in range(W):
        sum_v += lst[i]
    max_v = sum_v
    max_i = 0
    max_e = W-1
    for i in range(N-W):
        sum_v += lst[i+W]
        sum_v -= lst[i]

        if max_v < sum_v:
            max_v = sum_v
            max_i = i+1  # todo 이거 인덱스 잘 생각해봐라
            max_e = i+W

    print(f'#{t} {max_i} {max_e} {max_v}')

