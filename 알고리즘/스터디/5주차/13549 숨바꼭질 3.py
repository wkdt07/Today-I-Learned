# BFS로 최단 레벨 구하기

from collections import deque as dq

s,e = map(int,input().split()) # N:현재위치, K:목표지점

level =0

vst = [0] * 100001

def bfs(s,e):
    level = 1 # 방문 표시를 위해 혹시 몰라서 더해둠
    q = dq()
    q.append((s,level))
    vst[s] = 1
    while q:
        t = q.popleft()
        now = t[0]
        level = t[1]

        if now == e:
            return level-1

        if now*2 in range(0,100001) and vst[now*2] > level: # 이게 level을 최대한 줄일 수 있어서 q에 우선 넣어야함
            vst[now*2] = level
            q.append((now*2,level))

        if now + 1 in range(0,100001) and vst[now+1] > level:
            vst[now+1] = level
            q.append((now+1,level+1))

        if now-1 in range(0,100001) and vst[now-1] > level:
            vst[now-1] = level
            q.append((now-1,level+1))

print(bfs(s,e))
