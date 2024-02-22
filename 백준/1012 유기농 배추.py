from collections import deque

T = int(input())

dir = [(0,1),(0,-1),(1,0),(-1,0)]
def bfs(s):
    q = deque([s])
    while q:
        t = q.popleft()
        i,j = t[0],t[1]
        for d in range(4):
            ni,nj = i+dir[d][0],j+dir[d][1]
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 1:
                q.append([ni,nj])
                arr[ni][nj] = 0
                c_lst.remove([ni, nj])



for t in range(1,T+1):
    M,N,K =map(int,input().split()) #가로,세로,배추 갯수
    arr=[[0]*M for _ in range(N)]
    c_lst = []
    for k in range(K):
        j,i = map(int,input().split())
        c_lst.append([i,j])
        arr[i][j] = 1
    cnt = 0
    while c_lst:
        s = c_lst.pop()
        i,j =s[0],s[1]
        arr[i][j] = 0
        bfs(s)
        cnt += 1
    print(cnt)


'''
DFS

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

T=int(input())

def dfs(x, y):
    #동->남->서->북 순서
    dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
    for dir_num in range(4):
        nx=x+dx[dir_num]
        ny=y+dy[dir_num]
        if 0<=nx<M and 0<=ny<N:
            if ground[ny][nx] == 1:
                ground[ny][nx] = 0
                dfs(nx, ny) # 다음 점도 1인지 확인. 아니면? 그냥 아무것도 없이 끝남

for _ in range(T):
    M, N, K=map(int, input().split())
    count=0
    ground = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        X, Y=map(int, input().split())
        ground[Y][X]=1
    for y in range(N):
        for x in range(M):
            if ground[y][x] == 1:
                dfs(x, y) # 1인 모든 점에 대해서 이 지랄을 돌린다, 함수 내에서 방문한 점은 0으로 만듦으로, 만약 1인 점이 있다면 그건 떨어져있는 1의 값
                count += 1
    print(count)
'''

'''
훨씬 깔끔한 bfs

from collections import deque
import sys


t = int(input())

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for _ in range(t):
    m, n, k = map(int, input().split())

    plot = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())

        plot[y][x] = 1

    count = 0
    for i in range(n):
        for j in range(m):
            if not plot[i][j]:
                continue

            q = deque([(i, j)])
            plot[i][j] = 0
            while q:
                x, y = q.popleft()
                for dx, dy in d:
                    a = x + dx
                    b = y + dy
                    if 0 <= a < n and 0 <= b < m and plot[a][b]:
                        q.append((a, b))
                        plot[a][b] = 0

            count += 1

    print(count)

'''