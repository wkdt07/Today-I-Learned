# 솔직히 이거 combination으로도 풀긴 하겠다

# from itertools import permutations


def connected(num_lst): # 연결되어있는지
    global flag
    flag = False
    for x in range(N): # 해당 num_lst 안에 있지 않은 제 2 지역구 중 하나
        if x not in num_lst:
            break

    q = [x] # 현재 노드와 간선 수
    q = dq(q)
    v_cnt =0
    vst_2 = [0]*N
    vst_2[x] = 1
    num_of_other = N - len(num_lst)
    while q:
        now = q.popleft()
        if v_cnt == num_of_other - 1:
            flag = True
            return
        for next_node in arr[now]:
            if next_node not in num_lst and not vst_2[next_node]:
                v_cnt += 1
                vst_2[next_node] = 1
                q.append(next_node)
def dfs(now,sum_v):
    global min_v
    step = False
    for finish_node in arr[now]:
        if finish_node not in vst:
            step = True
            break
    if not step: # 다 찾아봤는데도 없다 -> 마지막 노드임
        connected(vst)
        if flag:
            min_v = min(min_v, abs((total - sum_v) - sum_v))
        return

    # if sum_v >= half:
    #     connected(vst)
    #     if flag:
    #         min_v = min(min_v,abs((total-sum_v)-sum_v))
    #     return



    for next_node in arr[now]:
        if next_node not in vst:
            vst.append(next_node)
            dfs(next_node,sum_v+numbers[next_node])
            vst.remove(next_node)


T = int(input())

from collections import deque as dq

for tc in range(1,T+1):
    N = int(input()) # 마을의 수
    adj = [list(map(int,input().split())) for _ in range(N)]
    arr = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if adj[i][j]:
                arr[i].append(j)
                # arr[j].append(i)
    numbers = list(map(int,input().split())) # 각 지역의 유권자
    # print(*arr)
    total = sum(numbers)
    half = total//2
    # todo 나누기 -> 이후에 connected 함수로 나눠지는지 여부 확인
    # dfs로 할거면 싹 다 돌려봐야 함. 아니면 오류 있을 수 있음.

    min_v = float('inf')
    for now in range(N):
        vst = [now]
        dfs(now,numbers[now])



    print(f'#{tc} {min_v}')








    # parents = list(range(N)) # 각 지역의 부모들
    # flag = False
    # # other_num_lst = [] # todo
    # num_of_other = len(other_num_lst)

    # def parenting(x, other_nums_lst):  # 지역구로 묶이지 않은 애들은 인자로 받음
    #     if x == parents[x]:
    #         return
    #     else:
    #         if parents[x] < x:
    #
    #     pass

