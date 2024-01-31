
# for i in range(N):
#     lst = []
#     lst.extend(input())
#     arr.append(lst)

# for i in arr:
#     print(*i)

N,M = map(int,input().split())

K = int(input())

arr = []
for i in range(N):
    arr.append([char for char in input()])

bomb = []
for lst in arr:
    cnt_x = []
    for i in range(len(lst)):
        if lst[i] == '@':
            cnt_x.append(i)
    bomb.append(cnt_x)
# print(bomb)


for b_y in range(len(bomb)):
    for b_x in bomb[b_y]:
        x = b_x
        y = b_y
        # print(y,x)
        dx = [-1,1,0,0]
        dy = [0,0,1,-1]
        arr[y][x] = '%'
        # bomb_dir = [(-1,0),(1,0),(0,1),(0,-1)]
        # for dir in bomb_dir:
        #     dx,dy = dir
        for i in range(4):
            for k in range(1,K+1):
                nx = x + k*dx[i]
                ny = y + k*dy[i]
                if 0 <= nx < M and 0 <= ny < N:

                    if arr[ny][nx] == '#':
                        break
                    arr[ny][nx] = '%'


for i in arr:
    string = ''.join(i)
    print(string)




'''
# for문 append 연습
asd = []
for i in range(n):
    asd.append([char for char in input()])
'''