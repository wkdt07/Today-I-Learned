N,M = map(int,input().split())

K = int(input())

arr = []

for i in range(N):
    lst = []
    lst.extend(input())
    arr.append(lst)
for i in arr:
    print(*i)

for lst in arr:
    cnt_y = []
    for i in range(len(lst)):
        cnt_x = []
        if lst[i] == '#':
            cnt_x.append(i)
        cnt_y.append(cnt_x)
print(cnt_y)
# [[], [], []]
# for y in range(N):
#     for x in range(M):
#         bomb_dir = [(-1,0),(1,0),(0,1),(0,-1),(0,0)]
asd = []
for i in range(n):
    asd.append([char for char in input()])
