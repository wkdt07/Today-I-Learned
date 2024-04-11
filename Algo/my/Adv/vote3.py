from itertools import combinations as cb
from collections import deque as dq

T = int(input())

def connected(group):
    # flag = False
    vst = [0]*N
    # no_group = []
    # for x in range(N):
    #     if x not in group:
    #         flag = True
    #         no_group.append(x)
    #
    #
    # if not flag:
    #     return False
    x = group[0]
    q = [x]
    q = dq(q)
    vst[x] = 1
    cnt = 0
    num = len(group)
    # num_of_none = N-len(group)
    while q:
        now = q.popleft()
        if cnt == num -1:
            return True
        for next in arr[now]:
            if next in group and not vst[next]:
                vst[next] = 1
                q.append(next)
                cnt += 1
    return False
for tc in range(1,T+1):
    N = int(input())
    adj = [list(map(int,input().split())) for _ in range(N)]
    arr = [set() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if adj[i][j]:
                arr[i].add(j)
                arr[j].add(i)
    nums = list(map(int,input().split()))
    total = sum(nums)
    combs = []
    for k in range(1,N):
        combs += cb(range(N),k)
    # print(combs)
    min_v = float('inf')
    for group in combs:
        no_group = []
        for x in range(N):
            if x not in group:
                # flag = True
                no_group.append(x)
        if connected(group) and connected(no_group):
            sum_group = 0
            for g in group:
                sum_group += nums[g]
            sum_else = total - sum_group
            sum_v = abs(sum_group - sum_else)
            min_v = min(min_v,sum_v)

    print(f'#{tc} {min_v}')

