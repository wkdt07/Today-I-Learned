

N = int(input())

_map = [input() for _ in range(N)]

# cnt => 4개의 집을 모두 들렀을 때
k_lst = []
for i in range(N):
    for j in range(N):
        if _map[i][j] == 'P':
            start = (i,j)
        if _map[i][j] == 'K':
            k_lst.append((i,j))
check_lst = [0] * len(k_lst)

arr = [list(map(int,input().split())) for _ in range(N)] # 체력적으로 가는거

vst = [[0]*N for _ in range(N)]


si,sj = start

vst[si][sj] = 1

dir  = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

# rst = float('inf')
# rst = (0,0)
rst = []

# 최저고도와 최저고도
def route(s,max_v = -float('inf'),min_v = float('inf')):
    global rst
    i,j = s

    for d in dir:

        if not check_lst.count(0): # todo 이거 어디에?
            rst.append((max_v,min_v))
            return

        ni,nj = i+d[0],j+d[1]

        if 0<=ni<N and 0<=nj<N and not vst[ni][nj]:
            vst[ni][nj] = 1

            # K를 지나면
            if (ni,nj) in k_lst:
                idx = k_lst.index((ni,nj))
                check_lst[idx] = 1
                tmp = arr[ni][nj]
                route((ni,nj),max(max_v,tmp),min(min_v,tmp))
                check_lst[idx] = 0
                vst[ni][nj] = 0

            else:
                tmp = arr[ni][nj]
                route((ni, nj), max(max_v, tmp), min(min_v, tmp))
                vst[ni][nj] = 0

            # else:
            #     if arr[ni][nj] > arr[i][j]:
            #         tmp = arr[ni][nj] - arr[i][j]
            #         route((ni, nj), max(max_v, tmp), min(min_v, tmp))
            #
            #     else:
            #         route((ni, nj), max_v, min_v)


        else:continue



route(start)
print(rst)





