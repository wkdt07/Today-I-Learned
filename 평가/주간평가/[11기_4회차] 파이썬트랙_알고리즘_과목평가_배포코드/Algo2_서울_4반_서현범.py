T = int(input())

def vst(s):
    global sum_v # 합해지는 값
    global cnt # 재귀 횟수
    i,j = s
    now = arr[i][j] # 현재 값
    next = now # 해당 범위 내에서 최대 값
    for k in range(M):
        for l in range(M):
            ni, nj = i + k, j + l # 다음 자리 탐색
            if 0 <= ni < N and 0 <= nj < N: # 범위 내에 존재하면
                next_temp = arr[ni][nj] # 다음 자리 값을 할당

            if next_temp > next: # 만약 다음 값이 현재 최대 값보다 크면
                next = next_temp # 최대값에 재할당
                s = ni,nj # 다음으로 탐색할 곳

    if next == now: # 현재값 == 최대값이면
        if cnt == 0: # 재귀 없이 바로 탐색이 끝나는 경우 현재 자리를 더해줘야한다
            sum_v += arr[i][j]
        return # 끝
    else:
        sum_v += next # 만약 재할당을 받았다면 최대값을 누적합에 더해준다
        cnt += 1 # 재귀횟수 +1
        vst(s) # 재귀

for t in range(1,T+1):
    N,M = map(int,input().split()) # N: 전체 행렬 크기, M: 탐색 행렬 크기
    arr = [list(map(int,input().split())) for _ in range(N)] # 행렬
    sum_v = 0 # 누적합
    cnt = 0 # 재귀횟수
    vst((0,0))
    print(f'#{t} {sum_v}')