n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]

lst = [[] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            lst[i].append(j)
        # else:
        #     lst[i+1].append(0)


# print(lst)

# stack

def dfs(i,V):
    visited = [0]*(V+1)

    stack = []

    visited[i] = 1
    print(i,end=' ')

    while True:

        for w in lst[i]:
            if visited[w] == 0:
                stack.append(i)
                i = w
                visited[i] = 1
                print(i,end=' ')
                break

        else:
            if stack:
                i = stack.pop()

            else:
                break


dfs(0,n)