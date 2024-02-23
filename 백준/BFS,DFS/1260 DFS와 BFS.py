# DFS와 BFS로 탐색한 결과를 출력
from collections import deque
N,M,V = map(int,input().split()) # N : 정점 수 , M: 간선수 , V: 시작 정점


vst_b = [0] * (N+1)
vst_d = [0] * (N + 1)
arr = [[]for _ in range(N+1)]

for m in range(M):
    s,e = map(int,input().split())
    arr[s].append(e)
    arr[e].append(s)

for n in range(N+1):
    arr[n].sort()

def dfs(s):
    stack = []
    vst_d[s] = 1
    print(s,end = ' ')
    while True:
        for w in arr[s]:
            if not vst_d[w]:
                print(w, end=' ')
                stack.append(s)
                s = w
                vst_d[s] = 1
                break
        else:
            if stack:
                s = stack.pop()
            else:
                break

def bfs(s):
    q = deque()
    q.append(s)
    vst_b[s] = 1
    print(s, end=' ')
    while q:
        t = q.popleft()
        for ns in arr[t]:
            if not vst_b[ns]:
                q.append(ns)
                vst_b[ns] = 1
                print(ns,end = ' ')
            else: continue
dfs(V)
print()
bfs(V)


'''재귀
from collections import defaultdict, deque
n, m, v = map(int, input().split())
adj_list = defaultdict(set)
for _ in range(m):
    s, e = map(int, input().split())
    adj_list[s].add(e)
    adj_list[e].add(s)
   
# 정렬부분 추가
for key in adj_list:
    adj_list[key] = sorted(adj_list[key])

visited1 = [False for _ in range(n+1)]
visited2 = [False for _ in range(n+1)]
    
def DFS(start):
    visited1[start] = True
    print(start, end=' ')
    for i in adj_list[start]:
        if visited1[i] == False:
            DFS(i)
def BFS(start):
    q = deque([start])
    visited2[start] = True
    while q:
        node = q.popleft()
        print(node, end=' ')
        for i in adj_list[node]:
            if visited2[i] == False:
                visited2[i] = True
                q.append(i)

DFS(v)
print()
BFS(v)
'''

'''
재귀 bfs

def recursiveBFS(graph, q, discovered):
 
    if not q:
        return
 
    # 프론트 노드를 큐에서 빼내고 출력
    v = q.popleft()
    print(v, end=' ')
 
    # 모든 에지(v, u)에 대해 수행
    for u in graph.adjList[v]:
        if not discovered[u]:
            #는 발견된 것으로 표시하고 대기열에 넣습니다.
            discovered[u] = True
            q.append(u)
            
    # 각 레벨을 모두 확인하고 q를 가져간다.
    recursiveBFS(graph, q, discovered)
'''

# https://www.techiedelight.com/ko/breadth-first-search/