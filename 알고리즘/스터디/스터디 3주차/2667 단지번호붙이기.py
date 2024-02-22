from collections import deque



N = int(input())



arr = [input() for _ in range(N)]

l_lst = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == '1':
            l_lst.append((i,j))

dir = [(0,1),(0,-1),(1,0),(-1,0)]
visited = []
def bfs(s): #(i,j)
    global cnt
    q = deque([s])
    # print(s)
    visited.append(s)
    while q:
        x = q.popleft()
        # print(x)
        i,j = x
        for d in dir:
            ni,nj = i+d[0],j+d[1]
            if 0<=ni<N and 0<=nj<N and ((ni,nj) not in visited) and arr[ni][nj] == '1':
                cnt += 1
                q.append((ni,nj))
                visited.append((ni,nj))
                l_lst.remove((ni,nj))
                bfs((ni,nj))

cnt_lst = []

while l_lst:
    s = l_lst[-1]
    # print(s)
    cnt = 1
    bfs(s)
    cnt_lst.append(cnt)

print(cnt_lst)








dir = [(1,0),(-1,0),(0,1),(0,-1)]


