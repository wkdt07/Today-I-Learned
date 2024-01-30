# a = list(list('_' for i in range(5))for _ in range(4))
#
# x = [-1,1,0]
# y = [-1,1,0]
#
# for t in range(2):
#     i, j = map(int, input().split())
#     for dx in x:
#         for dy in y:
#             try:
#                 if dx == 0 and dy == 0:
#                     break #이건 break 해야 아래로 안 감
#                 a[i+dx][j+dy] = '#'
#             except:
#                 pass
#
# for arr in a:
#     print(*arr)

a = [['_']*5 for _ in range(4)]

for t in range(2):
    y,x = map(int,input().split())
    dir_lst = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for dy,dx in dir_lst:
        ny = y + dy
        nx = x + dx
        if 0<=ny<4 and 0<=nx<5:
            a[ny][nx] = '#'

for row in a:
    print(*row)


