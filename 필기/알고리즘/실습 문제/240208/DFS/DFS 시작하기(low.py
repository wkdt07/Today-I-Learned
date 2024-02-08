n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

lst = [[] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            lst[i].append(j)

def dfs(n):
    stack = []
    visited = [0] * n
    i = 0

    visited[i] = 1
    print(i,end=' ')

    while True:
        for w in lst[i]:
            if visited[w] == 0:
                visited[w] = 1
                print(w,end=' ')
                stack.append(i)
                i = w
                break

        else:
            if stack:
                i = stack.pop()

            else:
                break

dfs(n)

