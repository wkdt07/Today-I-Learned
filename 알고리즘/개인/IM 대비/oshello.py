T = int(input())


dir = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

def swap(i,j,c):

        for d in dir:
            p = 1
            ni = i + p * d[0]
            nj = j + p * d[1]
            while 0<=ni<N and 0<=nj<N:
                if arr[ni][nj] == c:
                    for p2 in range(1,p): # 뒤집기
                        if arr[i+d[0]*p2][j+d[1]*p2] != c:
                            arr[i+d[0]*p2][j+d[1]*p2] = c
                    break
                p += 1
                ni = i + p * d[0]
                nj = j + p * d[1]



for t in range(1,T+1):
    N,M = map(int,input().split())
    arr = [[0]*N for _ in range(N)]
    k = N//2
    arr[k-1][k-1],arr[k][k] = 2,2
    arr[k-1][k],arr[k][k-1] = 1,1

    # print(*arr)


    for m in range(M):
        j,i,c = map(int,input().split())
        i -= 1
        j -= 1
        arr[i][j] = c
        swap(i,j,c)

    cnt_b = 0
    cnt_w = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                cnt_b += 1
            elif arr[i][j] == 2:
                cnt_w += 1


    print(f'#{t} {cnt_b} {cnt_w}')


'''
B = 1
W = 2

dir = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]

#뒤집을 돌의 좌표를 구해주는 함수

def get_reverse_stone(y,x,bang,color):
    result = []
    dy,dx = dir[bang]
    ny,nx = y,x
    
    while True: # 같은 색 돌을 발견하는 순간 break
        ny,nx = ny+dy,nx+dx
        #1. 범위 벗어난 경우
        if nx<0 or ny<0 or nx>=N or ny>=N : return [] # 빈 배열
        
        #2. 돌이 없는 경우(빈칸인 경우)
        if board[ny][nx] == 0: return []
        
        if board[ny][nx] == color: break
        
        result.append((ny,nx))
        
T = int(input())

for t in range(1,T+1):
    N,M = map(int,input().split())
    board = [[0]*N for _ in range(N)]
    
    
    # 보드에 초기돌 4개 세팅
    mid = N//2
    board[mid-1][mid-1] = W
    board[mid-1][mid-0] = B
    board[mid-0][mid-1] = B
    board[mid-0][mid-0] = W
    
    for _ in range(M):
        x,y,color = map(int,input().split())
        y,x = y-1,x-1
        
        # 돌을 둔다
        board[y][x] = color
        
        #8방향 선택
        for bang in range(8):
            target_stones = get_reverse_stone(y,x,bang,color) #뒤집을 돌들의 좌표 배열을 얻는다
            
            # 뒤집을 돌이 있다면, 돌을 하나씩 뒤집는다.
            
            if target_stones:
                for ry,rx in target_stones:
                    if color == B:
                        board[ry][rx] == B
                    else:
                        board[ry][rx] == W
        
        b_cnt,w_cnt = 0,0
        
        for i in range(N):
            for j in range(N):
                if board[i][j] == B:
                    b_cnt += 1
                if board[i][j] == W:
                    w_cnt += 1
                    
        print(f'#{t} {b_cnt} {w_cnt}')
'''