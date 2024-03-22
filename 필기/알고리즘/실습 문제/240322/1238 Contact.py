from collections import deque


T = 10
def bfs(start):
    global tmp
    q = deque() # level과 좌표
    a = (1,start)
    q.append(a)
    vst[start] = 1
    prev_lv = 1
    while q:
        now_lv,now_nd = q.popleft()
        # vst[now_nd] = 1
        if now_lv != prev_lv:
            prev_lv = now_lv
            tmp = []
        tmp.append(now_nd)
        for next_nd in arr[now_nd]:
            if not vst[next_nd]:
                vst[next_nd] = 1
                q.append((now_lv+1,next_nd))





for t in range(1,T+1):
    N,start = map(int,input().split())
    lst = list(map(int, input().split()))
    k = max(lst)
    arr = [set() for _ in range(k+1)]

    for i in range(0,len(lst),2):
        arr[lst[i]].add(lst[i+1])

    vst = [0] * (k+1)
    tmp = []
    bfs(start)
    print(f'#{t} {max(tmp)}')


