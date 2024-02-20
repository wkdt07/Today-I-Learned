w,h = map(int,input().split())
arr = [[0]*(w+1) for _ in range(h+1)]
# 나머지
p,q = map(int,input().split())

t = int(input())

dx = t//w
dy = t//h

if p + dx >= w:
    ddx = p+dx-w

