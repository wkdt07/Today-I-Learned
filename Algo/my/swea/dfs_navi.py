arr = [[],[3,5,6],[1,4],[5],[1],[1],[]]

vst = [0]*7

from collections import deque as dq

stack = dq()

a,b = map(int,input().split())

stack.append([a,1])

# cnt = 0
# cnt = 0
while stack:

    v,cnt = stack.popleft()

    if vst[b]:
        print(vst[b]-1) # 처음에 not 방지하기 위해서 그냥 1부터 시작
        break

    if not vst[v]:
        vst[v] = cnt
        for next in arr[v]:
            if not vst[next]:
                stack.append([next,cnt+1])

if not vst[b]:
    print(vst[b])
