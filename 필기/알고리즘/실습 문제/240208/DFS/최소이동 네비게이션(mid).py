arr = [[],
       [3,5,6],
       [1,4]
    ,[5]
    ,[1]
    ,[1]
    ,[]]

# print(arr)

s,e = map(int,input().split())

visited = [0] * (len(arr) + 1)
cnt_lst = []

# 현재 계속 arr[s][0]로 가는 문제 발생, visited 만들어서 만약 1이라면 다음으로 가는 걸로 경로 변경
def dfs(s,e,cnt):

    rst = s
    visited[s] = 1
    if rst == e:
        cnt_lst.append(cnt)
        # cnt -= 1
        return

    if arr[s] != []:
        K = len(arr[s])
        for k in range(K):
            if visited[s] == 1:
                return

            else:
                s = arr[s][k]
                dfs(s, e, cnt + 1)
    else: return

dfs(s,e,1)
print(cnt_lst)

'''
def dfs(s,e):
    cnt = 0
    min_v = float('inf')
    # visited[s] = 1
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
'''