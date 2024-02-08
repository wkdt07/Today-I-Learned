arr = [[],
       [3,5,6],
       [1,4]
    ,[5]
    ,[1]
    ,[1]
    ,[]]

# print(arr)

s,e = map(int,input().split())
visited = [0]*(len(arr)+1)



def dfs(s,e):
    cnt = 0
    min_v = float('inf')
    visited[s] = 1
    for w in arr[s]:
        if len(arr[w])>=1 :

            if visited[w] == 0:
                visited[w] = 1
                cnt += 1
                s = w
                dfs(s,e)
            else:
                continue

    if s == e:
        min_v = min(cnt,min_v)

    return min_v
print(dfs(4,6))