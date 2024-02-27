T = int(input())


def cart(i, cnt, sum_v):
    global min_v

    if cnt == N - 1:
        min_v = min(min_v, sum_v + arr[i][0])
        return
    if sum_v > min_v:
        return

    else:
        # vst[i] = 1
        for j in range(1, N):
            if not vst[j] and j != i:
                # sum_v += arr[i][j]
                vst[j] = 1
                cart(j, cnt + 1, sum_v + arr[i][j])
                vst[j] = 0


for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    i = 0
    vst = [0]*N
    vst[0] = 1
    sum_v = arr[0][0]

    min_v = float('inf')

    cart(i,0,sum_v)

    print(f'#{t} {min_v}')

