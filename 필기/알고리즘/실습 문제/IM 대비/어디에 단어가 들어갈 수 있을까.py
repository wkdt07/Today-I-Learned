T = int(input())

for t in range(1,T+1):
    N,K = map(int,input().split())
    arr = [list(map(int,input().split()))+[0] for _ in range(N)]
    k = [[0] * (N+1)]  # 마지막 항 보정용
    arr += k

    ans = 0
    # print(arr)
    '''
    이러면 4짜리도 측정하게 됨
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
                if cnt == K:
                    ans += 1
                    cnt = 0
    '''
    for i in range(N+1):
        cnt = 0
        for j in range(N+1):
            if arr[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    ans += 1 # 만약 마지막 항이 0이 아니면 갯수가 세어지질 않음
                cnt = 0



    for i in range(N+1):
        cnt = 0
        for j in range(N+1):
            if arr[j][i] == 1:
                cnt += 1
            else:
                if cnt == K:
                    ans += 1
                cnt = 0

    print(f'#{t} {ans}')
