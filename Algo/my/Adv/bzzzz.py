# j에 따라 dir이 다르다
# T 모양은 따로 계산해야함
# 얻을 수 있는 벌집의 최대값

T = int(input())

def dfs(i,j,sum_v,cnt=1):
    global max_v
    # global vst
    if cnt == 4:
        max_v = max(max_v,sum_v)
        return
    if j % 2:
        dir = [(0,1),(1,0),(-1,0),(0,-1),(1,-1),(1,1)]
    else:
        dir = [(0,1),(1,0),(-1,0),(0,-1),(-1,-1),(-1,1)]
    for d in dir:
        ni,nj = i+d[0],j+d[1]
        if ni in range(N) and nj in range(M) and (ni,nj) not in vst:
            vst.append((ni,nj))
            dfs(ni,nj,sum_v+hive[ni][nj],cnt + 1)
            vst.remove((ni,nj))

def t_shape(i,j):
    global max_v
    sum_T = 0
    sum_t = 0
    if j%2: # 홀수
        #T
        i1,i2,i3 = i,i,i+1
        j1,j2,j3 = j-1,j+1,j

        #ㅗ
        i4,i5,i6 = i-1,i+1,i+1
        j4,j5,j6 = j,j-1,j+1

        if i1 in range(N) and i2 in range(N) and i3 in range(N):
            if j1 in range(M) and j2 in range(M) and j3 in range(M):
                sum_T = hive[i][j] +  hive[i1][j1] +  hive[i2][j2] +  hive[i3][j3]
        if i4 in range(N) and i5 in range(N) and i6 in range(N):
            if j4 in range(M) and j5 in range(M) and j6 in range(M):
                sum_t = hive[i][j] + hive[i4][j4] + hive[i5][j5] + hive[i6][j6]
        max_v= max(max_v,sum_T,sum_t)
    else: # 짝수
        # T
        i1, i2, i3 = i-1, i-1, i + 1
        j1, j2, j3 = j - 1, j + 1, j

        # ㅗ
        i4, i5, i6 = i - 1, i, i
        j4, j5, j6 = j, j - 1, j + 1
        if i1 in range(N) and i2 in range(N) and i3 in range(N):
            if j1 in range(M) and j2 in range(M) and j3 in range(M):
                sum_T = hive[i][j] +  hive[i1][j1] +  hive[i2][j2] +  hive[i3][j3]
        if i4 in range(N) and i5 in range(N) and i6 in range(N):
            if j4 in range(M) and j5 in range(M) and j6 in range(M):
                sum_t = hive[i][j] + hive[i4][j4] + hive[i5][j5] + hive[i6][j6]
        max_v= max(max_v,sum_T,sum_t)



for tc in range(1,T+1):
    N,M = map(int,input().split()) # i와 j의 최대값

    hive = [list(map(int,input().split())) for _ in range(N)]

    vst = []
    group = []
    max_v = -float('inf')
    for i in range(N):
        for j in range(M):
            vst = [(i,j)]
            dfs(i,j,hive[i][j])
            t_shape(i,j)

    print(f'#{tc} {max_v}')

