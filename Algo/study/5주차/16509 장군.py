from collections import deque as dq

s = tuple(map(int,input().split())) # 상의 위치
e = tuple(map(int,input().split())) # 왕의 위치

'''
4 2
2 5
'''
dir = {
    (1,0) : [(1,-1),(1,1)],
    (0,1) : [(-1,1),(1,1)],
    (-1,0) : [(-1,-1),(-1,1)],
    (0,-1) : [(-1,-1),(1,-1)]
}
# level = 0

def bfs(s,e,level=0):
    i,j = s
    q = dq([(i,j,level)])
    vst = []
    while q:

        t = q.popleft()
        i,j,level= t # 1

        if t[0:2] == e:
            return level

        # 먼저 4방향으로 움직이고, 이후에 대각선 2방향
        dir1 = [(1,0),(-1,0),(0,1),(0,-1)]
        # dir2 = [(1,1),(1,-1),(-1,-1),(-1,1)]
        for d1 in dir1:
            ni1,nj1 = i + d1[0],j + d1[1]
            if (0<=ni1<10 and 0<=nj1<9) and (ni1,nj1) != e:
                for d in dir[d1]:
                    ni,nj = ni1+2*d[0],nj1+2*d[1]
                    if (0<=ni<10 and 0<=nj<9) and (ni1+d[0],nj1+d[1]) != e and (ni,nj) not in vst:
                        vst.append((ni,nj))
                        q.append((ni,nj,level+1))

        # level += 1 #2
print(bfs(s,e))