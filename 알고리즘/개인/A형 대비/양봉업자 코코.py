T = int(input())

dir = [(1,0),(0,1),(-1,0),(0,-1)]

def dfs(s,ans,path,lev=0):

    global ans_lst
    if lev == 3:
        ans_lst.append(ans)
        return

    i,j = s

    for d in dir:
        ni = i + d[0]
        nj = j + d[1]
        if (ni,nj) not in path:
            if 0<=ni<N and 0<=nj<M:
                path.append((ni,nj))
                dfs((ni,nj),ans+arr[ni][nj],path,lev+1)
                path.pop()


def t_shape(s):
    global ans_lst
    i,j = s
    if j%2: # 짝수일 때

        i1,j1 = i-1,j-1
        i2,j2 = i+1,j
        i3,j3 = i-1,j+1

        i4,j4 = i,j-1
        i5,j5 = i-1,j
        i6,j6 = i,j+1

        if (0<=i1<N and 0<=i2<N and 0<=i3<N) and (0<=j1<M and 0<=j2<M and 0<=j3<M) :
            k1 = arr[i][j] + arr[i1][j1]+ arr[i2][j2] + arr[i3][j3]
            ans_lst.append(k1)
        if (0 <= i4 < N and 0 <= i5 < N and 0 <= i6 < N) and (0 <= j4 < M and 0 <= j5 < M and 0 <= j6 < M):
            k2 = arr[i][j] + arr[i4][j4]+ arr[i5][j5] + arr[i6][j6]
            ans_lst.append(k2)
    else: #홀수일 때

        i1,j1 = i,j-1
        i2,j2 = i+1,j
        i3,j3 = i,j+1

        i4, j4 = i-1,j
        i5,j5 = i+1,j-1
        i6,j6 = i+1,j+1

        if (0<=i1<N and 0<=i2<N and 0<=i3<N) and (0<=j1<M and 0<=j2<M and 0<=j3<M) :
            k1 = arr[i][j] + arr[i1][j1]+ arr[i2][j2] + arr[i3][j3]
            ans_lst.append(k1)
        if (0 <= i4 < N and 0 <= i5 < N and 0 <= i6 < N) and (0 <= j4 < M and 0 <= j5 < M and 0 <= j6 < M):
            k2 = arr[i][j] + arr[i4][j4]+ arr[i5][j5] + arr[i6][j6]
            ans_lst.append(k2)














for t in range(1,T+1):
    # path = []
    ans_lst = []
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            path = [(i,j)]
            dfs((i,j),arr[i][j],path)
            t_shape((i,j))

    # print(path)
    print(f'#{t} {max(ans_lst)}')
