'''n = int(input())

inp = [list(map(int,input().split())) for _ in range(n)]

arr = [[] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if inp[i][j] == 1:
            arr[i].append(j)

def dfs_2(n):

    visited = [0]*n
    i= 0
    visited[0] = 1
    stack = []

    temp = [i]
    while True:



        for w in arr[i]:
            if visited[w] == 0:
                stack.append(i)
                visited[w] = 1
                temp.append(w)
                i = w
                if len(temp) == 3:
                    print(*temp)
                    temp = [0]
                    break
                break



        else:
            if stack:
                i = stack.pop() # 이전 i
                if i == 0: # 0이면 굳이 다시 만들 필요 없음
                    temp = [0]
                else:
                    temp = [0,i] # 아니면 이전것도 포함

            else:
                break

dfs_2(n)'''

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

#path는 현재 탐색중인 경로를 기록
path = [0]*10

def dfs(level,now):
    if level == 2:
        for i in range(level+1):
            print(path[i],end= " ")
        print()
        return

    for i in range(n):
        if arr[now][i] == 1: #다음 경로가 존재하면
            path[level+1] = i # 경로를 기록
            dfs(level+1,i) #다음 경로로 dfs, i가 새로운 now
            path[level+1] = 0 # 탐색 끝나면(입력 끝나면) 해당 경로 초기화, 다음 경로로

dfs(0,0)