# union-find
# parents가 같다면 상관 없음
import sys
input = sys.stdin.readline

N = int(input())# 도시의 수
M = int(input()) #여행 계획

arr = [[0]+list(map(int, input().split())) for _ in range(N)]

relation = [[] for _ in range(N+1)]



parents = list(range(N+1))

def find_set(x):
    if x == parents[x]:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]

def union_set(x, y):
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return
    if x > y:
        parents[x] =y
    else:
        parents[y] = x

for i in range(N):
    for j in range(N):
        if arr[i][j]:
            union_set(i, j)

vac = list(map(int,input().split()))

flag = parents[vac[0]]
i = 1
ans = True
while i < M:
    if flag != parents[vac[i]]:
        ans = False
        break
    i += 1


if ans:
    print('YES')
else: print("NO")

