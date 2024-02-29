# 운전자의 상황에 따라 좌표의 이동 방향이 달라진다.

# 경우는 4개.

# 기울기로?

# 최소 칸 수는 구할 수 있다, 턴 수도 미리 구할 수 있나?

# 현재 지점과 목표 지점을 확인한 후 di와 dj의 부호에 따라서 턴 수가 정해진다.

# 경우의 수는 몇 개?

# 우회전의 수만 따지면 된다.

# 우회전 수가 4의 배수가 되면 다시 일반 방향으로 바뀐다.

T = int(input())

for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    target = [[] for _ in range(11)]
    tc = 0 # 타겟들의 갯수 -> 타겟은 1부터 target_cnt 까지
    for i in range(N):
        for j in range(N):
            if arr[i][j]>0:
                target[arr[i][j]].append(i)
                target[arr[i][j]].append(j)
                tc +=1
    # print(target)
    # print(tc)
    s = [0,0]
    cnt = 0 # 지금까지 우회전 수
    dir = [(0,1),(1,0),(0,-1),(-1,0)]
    for ta in range(1,tc+1):
        i,j = s
        next_target = target[ta]
        ni,nj = next_target
        di,dj = ni-i,nj-j
        d = cnt%4 #dir[d]가 현재 움직이고 있는 방향
        now_d = dir[d]
        cnt_temp_i = 0
        cnt_temp_j = 0
        temp = d # 최대 방향 맞추기 위해서
        if di:
            while dir[temp][0]*di <=0:
                temp += 1
                cnt_temp_i += 1
                temp %= 4
        temp = d
        if dj:
            while dir[temp][1]*dj <= 0:
                temp += 1
                cnt_temp_j += 1
                temp %= 4
        cnt_temp = max(cnt_temp_i,cnt_temp_j)

        cnt += cnt_temp

        s = ni,nj

    print(f'#{t} {cnt}')