w,h = map(int,input().split()) # w: 가로길이(x) h:세로길이(y)
# arr = [[0]*(w+1) for _ in range(h+1)]
# 나머지
x,y = map(int,input().split()) #현재 위치

t = int(input()) #움직이는 시간

nx = x + t
ny = y + t

if nx <= w and ny <= h:
    pass
else:
    nx %= 2 * w
    ny %= 2 * h
    if nx > w:
        nx = 2*w - nx
    if ny > h:
        ny = 2*h - ny

print(nx,ny)







