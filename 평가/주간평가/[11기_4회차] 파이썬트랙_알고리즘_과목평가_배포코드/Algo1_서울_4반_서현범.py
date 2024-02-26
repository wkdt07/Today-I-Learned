T = int(input())

for t in range(1,T+1):
    N = int(input())

    arr = [list(map(int,input().split())) for _ in range(N)]
    P = 2 # 보너스 획득 범위

    max_v = 0 # 최대 점수 할당
    dir = [(0,1),(0,-1),(1,0),(-1,0)] # 방향
    for i in range(N):
        for j in range(N):
            sum_v = arr[i][j] # 누적합에 일단 현재 자리 할당
            for d in dir:
                for p in range(1,P+1):
                    ni = i +d[0]*p # 다음 i값
                    nj = j + d[1]*p # 다음 j 값
                    if (0<=ni<N) and (0<=nj<N): # 다음 좌표들이 범위 내에 존재하면
                        sum_v += arr[ni][nj] # 누적합에 포함

            if sum_v >= max_v: # 만약 누적합이 현재의 최대 누적합보다 크면
                max_v = sum_v # 재할당

    print(f'#{t} {max_v}')
