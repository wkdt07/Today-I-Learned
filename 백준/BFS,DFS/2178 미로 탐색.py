# 미로 통과하는 최소 경로, BFS

# 주의, 인덱스가 n-1,m-1 까지임

# 노드 단위 선택

from collections import deque
N,M = map(int,input().split())

arr = []

for i in range(N):
    lst = [0]+list(map(int,input()))
    arr.append(lst)

arr.reverse()
arr.append([0]*M)
print(len(arr))

print(len(arr[0]))
print(arr)

'''
s = ([1,1,0])
vst = [s]
q = deque([s])
# e = N,M
arr[N][M] = 1
print(*arr)

dir = [(0,1),(0,-1),(1,0),(-1,0)]
def bfs():
    level = 0
    while q:
        t = q.popleft()
        level = t[2]

        i, j = t[0], t[1]
        if i==N and j == M:
            return level+2

        for d in range(4):
            ni,nj = i + dir[d][0],j+dir[d][1]

            # if (ni,nj) == (N,M):
            #     return

            if 1<=ni<=N and 1<=nj<=M and (ni,nj) not in vst:
                if arr[ni][nj] == 1:
                    q.append((ni,nj,level+1))
                    vst.append((ni,nj))

'''