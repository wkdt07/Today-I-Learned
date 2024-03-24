N = int(input())

arr = [input() for _ in range(N)]



par = 0
for i in range(N):
    stack = 0
    for j in range(N):
        if arr[i][j] == '.':
            stack += 1
            if stack == 2:
                par += 1

        else:
            stack = 0

col = 0
for i in range(N):
    stack = 0
    for j in range(N):
        if arr[j][i] == '.':
            stack += 1
            if stack == 2:
                col += 1

        else:
            stack = 0

print(par,col)