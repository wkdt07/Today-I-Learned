from collections import deque as dq
import sys

input = sys.stdin.readline

T = int(input())

for tc in range(1,T+1):
    V,E = map(int,input().split()) # 노드와 간선

    # flag = True
    rat = [[]*(V+1) for _ in range(V+1)]
    for e in range(E):
        a,b = map(int,input().split())
        rat[a].append(b)
        rat[b].append(a)
    group = [0] * (V + 1)
    # 하나라도 True라면 True
    def bfs(s):
        global flag

        group_num = 1
        group[s] = group_num
        q = dq()
        # vst[s] = 1
        q.append([s,group_num])
        # vst_in = vst

        # if not flag:
        # vst = [0] *(V+1)
        # vst[s] = 1
        #     return
        while q:
            num,group_num = q.popleft()
            # vst = [0] *(V+1)
            # if flag:
            #     return
            for next in rat[num]:
                 # 어차피 이거부터 넣은 이후는 False
                if group[next]:
                    if group[next]== group_num: # 넣기 전에 있었는데, 그게 인접해있는 요소의 그룹이랑 같으면
                        return

                else:
                    group[next] = group_num * (-1)
                    q.append([next,group_num*(-1)])
        flag = True
        # 무사히 빠져나오면 True

    # for i in range(1,V+1):
    #     bfs(i) # 어차피 완전 탐색이라 상관 없음
    # flag = bfs(1)
    # vst = [0]*(V+1) # 3을 넣었을 때, 그 이후는 처음 넣었을 때와 이전과 같다.
    flag = False
    for i in range(1,V+1):
        if not group[i]:
            flag = False
            bfs(i) # 맞는 애라면 while문 통과해서 True로 바뀜
            if not flag:
                break
        # print(flag)
    if flag:
        print('YES')
    else:
        print('NO')


# T = int(input())
#
# for _ in range(T):
#     V,E = map(int,input().split()) # V는 정점 수, E는 간선 수
#     vst1 = [0] * (V+1) # 사용 했는지
#     vst2 = [0] * (V+1)
#     vst = [0] *(V+1)
#
#     relation = [[] for _ in range(V+1)]
#     for e in range(E):
#         s,e = map(int,input().split())
#         relation[s].append(e)
#         relation[e].append(s)
#
#
#
#     start = 1
#     while start<=V:
#         if not vst[start]:
#             vst[start] = 1
#             vst1[start] = 1
#             for end in relation[start]:
#                 if not vst[end]:
#                     vst2[end] = 1
#                     vst[end] = 1
#         start+=1
#
#     rst = 'YES'
#     def check():
#         global rst
#         for i in range(1,V):
#             if vst1[i]:
#                 for j in relation[i]:
#                     if vst1[j]:
#                         rst = 'NO'
#
#             elif vst2[i]:
#                 for j in relation[i]:
#                     if vst2[j]:
#                         rst = 'NO'
#
#                 # print('YES')
#     check()
#     print(rst)


    # v = 1
    # while v <= V:
    #     if v not in lst_2 and v not in lst_1:
    #         # vst[v] = 1
    #         lst_1.append(v)
    #         for end in relation[v]:
    #             if end not in lst_1 and end not in lst_2:
    #                 # vst[end] = 1
    #                 lst_2.append(end)
    #     v += 1
    # print(lst_1)
    # print(lst_2)