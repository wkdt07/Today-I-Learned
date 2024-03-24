# -*- coding:utf-8 -*-

N,M = map(int,input().split())
friend = [[] for _ in range(N)]

for _ in range(M):
    i,j = map(int,input().split())
    friend[i].append(j)
    friend[j].append(i)
# print(friend)

# vst = [0]*N
rst = 0
def dfs(s,path): # 디폴트 인자로 들어가면 다음 탐색 때 path가 []가 아니라 [0]로 들어가게 됨
    global rst # 결과인지 아닌지 확인용

    if len(set(path)) == 5:
        rst = 1
        return

    for next in friend[s]:
        if rst: # 가지치기용
            break
        if next not in path:
            dfs(next,path+[next])

# 함수 그냥 N번 돌리자
for i in range(N):
    if not rst:
        path = [i]
        dfs(i,path)
    else:
        break

print(rst)


# print(path)

# while not rst:
#     if len(set(path)) == N-1:
#         rst = 1
#         return
#
#     else:
#         for s in range(N):
#             if not
