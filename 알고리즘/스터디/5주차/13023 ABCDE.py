N,M = map(int,input().split())
friend = [[] for _ in range(N)]

for _ in range(M):
    i,j = map(int,input().split())
    friend[i].append(j)
    friend[j].append(i)
print(friend)

vst = [0] * N
def dfs():
    for i in range(N):

