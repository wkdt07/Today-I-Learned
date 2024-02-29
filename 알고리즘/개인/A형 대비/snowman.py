# 최초 리밋을 단순 수직 아래로
# 해당 층에서 가장 인접한 층에 있는 1을 확인
# 갈 수 있는지 확인( 땅이 포개져 있는지,)  - j 고정한 채로 i 확인, i가 층이므로 이걸 인자로 가져가야함
# -다음 층에서 반복
# - 만약 포개져 있지 않으면, 연결이 되어 있는지(j를 움직이면) 가능한지. 거기까지 움직여보고

N,M = map(int,input().split()) # j 한계 N , i 한계 M

arr = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            snow = (i,j)
        if arr[i][j] == 3:
            dia = (i,j) # 이걸 start로


limit = dia[0] # 무식하게 갔을 때 층, 이게 초기값


s = dia
def jump(s,limit_new = limit):
    global limit
    y_now,x_now = s
    if limit > dia[0]:
        return
    while True:
        dir_x = [(0,1),(0,-1)]
        left_x = 0
        right_x = 0
        p = 1
        for d in dir_x:



        for j in range(p)
        for i in range(y_now-limit,y_now+limit+1):


