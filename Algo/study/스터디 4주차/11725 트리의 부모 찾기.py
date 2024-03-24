import sys

sys.setrecursionlimit(10**6) # 재귀 횟수 늘리는 법
N = int(sys.stdin.readline()) # 노드의 수

arr = [[] for _ in range(N+1)]

for _ in range(N-1):
    s,e = map(int,sys.stdin.readline().split())
    arr[s].append(e)
    arr[e].append(s)

# vst = [0]*(N+1)
par =[0]*(N+1) # 얘를 vst로 쓸 수도 있다.


def make(s):
    # if 0 not in par[1:]:
    #     return
    for k in arr[s]:
        if not par[k]:
            par[k] = s
            make(k) # 어차피 다 탐색하면 알아서 끝나는데 뭐 하러 위에 코드를 넣음
make(1)
for i in range(2,N+1):
    print(par[i])
# stack = []
# while 0 in vst[1:]:
#     s = 1
#     vst[s] = 1
#     stack.append(arr[s])
#     t = stack.pop()
#
