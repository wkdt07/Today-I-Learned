import sys

input = sys.stdin.readline

def find_set(x):
    if x == parents[x]:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x,y):
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return
    if x>y:
        parents[x] = y
    else:
        parents[y] = x

V,E = map(int,input().split()) # 노드의 수, 간선의 수

# arr = [[] for _ in range(V)]
parents = list(range(V+1))
edges = []
for _ in range(E):
    s,e,w = map(int,input().split())
    edges.append([s,e,w])

edges.sort(key=lambda x:x[2])

cnt = 0
sum_v = 0
for s,e,w in edges:
    # 사이클 처리
    if find_set(s) == find_set(e):
        continue

    cnt +=1
    sum_v += w
    union(s,e)

    if cnt == V-1:
        break

print(sum_v)
