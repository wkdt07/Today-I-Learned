T = int(input())
from collections import deque as dq

def connected(group_lst):
    vst_2 = [0]*N
    flag = False
    for x in range(N):
        if x not in group_lst:
            flag = True
            break
    if not flag:
        return False
    else:
        cnt = 0
        q = [x]
        q = dq(q)
        vst_2[x] = 1

        while q:
            now = q.popleft()
            if cnt == N-len(group_lst)-1:
                return True
            for non_member in arr[now]:
                if non_member not in group_lst and not vst_2[non_member]:
                    vst_2[non_member] = 1
                    q.append(non_member)
                    cnt += 1

        return False

def group(now):#dfs로 그룹 연결
    # vst[start] = 1
    global min_v
    global group_set
    a = set(group_lst)
    if len(group_lst) == 1 and connected(group_lst) and a not in group_set: # 하나만 있을 때도 확인해봐야함
        tmp = 0
        group_set.append(a)
        for member in group_lst:
            tmp += nums[member]
        now_v = abs(tmp - (total - tmp))
        min_v = min(min_v, now_v)
    for next_node in arr[now]:
        if not vst[next_node]:
            vst[next_node] = 1
            group_lst.append(next_node)
            a = set(group_lst)
            if connected(group_lst) and a not in group_set: # 연결되어 있다면
                tmp = 0
                group_set.append(a)
                for member in group_lst:
                    tmp += nums[member]
                now_v = abs(tmp-(total-tmp))
                min_v = min(min_v,now_v) # 갱신해주고
            group(next_node) # 낀채로 다음 노드로
            vst[next_node] = 0 # 돌아오면 제거 함 해주고
            group_lst.remove(next_node)



for tc in range(1,T+1):
    N = int(input())

    adj = [list(map(int,input().split())) for _ in range(N)]

    nums = list(map(int,input().split()))
    total = sum(nums)

    arr = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if adj[i][j]:
                arr[i].append(j)
                arr[j].append(i)

    min_v = float('inf')

    group_set = []
    for start in range(N):
        group_lst = [start]
        vst = [0]*N
        vst[start] = 1
        group(start)
    print(group_set)
    print(f'#{tc} {min_v}')