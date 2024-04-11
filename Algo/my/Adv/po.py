from copy import deepcopy as dc

T = int(input())

def dfs(now ,cnt = 0):
    global eat_lst
    if cnt == 3:
        eat_lst.extend(eat_tmp)
        return
    i,j = now
    # p = 0
    # st = []
    for d in dir:
        p = 1
        p1,p2 = 1,1
        st = 0
        p_lst = []
        while True:

            ni,nj = i+p*d[0],j+p*d[1]
            if st == 2:
                break
            if ni not in range(N) or nj not in range(N): # 범위 밖을 벗어날 정도로 멀리 갔을 경우
                break
            if vst[ni][nj]==1:
                p_lst.append(p)
                st += 1
            p += 1
        # 만약 돌이 아예 없다면?
        if not st: # 아예 못 움직임
            continue
        elif st == 1: # 끝까지 가버린거(두번째 돌이 안 나온거
            p1 = p_lst[0]
            p2 = p-1
        elif st == 2:
            p1 = p_lst[0]
            p2 = p_lst[1]

        for k in range(p1+1,p2+1): # p1부터 p2 까지
            ni,nj = i+k*d[0],j+k*d[1]
            if vst[ni][nj] == 1:
                eat_tmp.append((ni,nj))
                vst[ni][nj] = 2
                dfs((ni,nj),cnt + 1)
                vst[ni][nj] = 1
                eat_tmp.remove((ni,nj))
            elif vst[ni][nj] == 0:
                vst[ni][nj] = 2
                dfs((ni,nj),cnt + 1)
                vst[ni][nj] = 0







for tc in range(1,T+1):
    N = int(input())

    arr = [list(map(int,input().split())) for _ in range(N)]

    stones = []
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                if arr[i][j] == 1:
                    stones.append((i,j))
                else:
                    start = (i,j)
    eat_lst = []
    eat_tmp = []
    vst = dc(arr)
    dir  = [(1,0),(0,1),(-1,0),(0,-1)]

    # print(arr)
    # print(start)
    # print(stones)
    dfs(start)
    eat_lst = set(eat_lst)
    result = len(eat_lst)
    print(f'#{tc} {result}')

