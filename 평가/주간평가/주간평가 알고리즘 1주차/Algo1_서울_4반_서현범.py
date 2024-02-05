T = int(input())

for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    di = [1,-1,0,0] # 상하
    dj = [0,0,1,-1] # 좌우

    sum_lst = [] #보너스 점수 모음

    for i in range(N):
        for j in range(N):
            sum_v = 0 # 보너스 점수
            max_v = 0
            if (i != 0) and (j != 0) and (i != N - 1) and (j != N - 1): # 만약 i,j 가 가장자리라면 그냥 sum_v(보너스점수)는 0
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]

                    if (0<=ni<N) and (0<=nj<N): # 인덱스를 벗어나지 않도록
                        sum_v += arr[ni][nj] # 상하좌우의 합
                sum_v -= arr[i][j] #상하좌우를 합친 값에서 맞힌 부분을 뺀다
                if sum_v % 2 == 0: # 2의 배수라면 2배
                    sum_v *= 2
                if sum_v < 0 : # 음수라면 0
                    sum_v = 0

            sum_lst.append(sum_v)

    sum_lst.sort() # sum_lst 오름차순 정리

    max_v = sum_lst[len(sum_lst)-1] # 정렬된 sum_lst의 마지막 항이 최댓값

    print(f'#{t} {max_v}') # 보너스 점수 모음 중 최대값 출력