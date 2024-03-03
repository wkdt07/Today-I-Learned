from collections import deque as dq




# def bfs(level,d_tree):
#     if d_tree.count(0) == N:
#         return level
#     # 물 용량
#     level + 1
#     if level % 2:
#         water = 1
#     else:
#         water = 2
#
#     d_tree = dq(d_tree)
#
#     while q:
#         pass

# 레벨별로 d_tree가 갈리고,
# def bfs(d_tree,level):
#     q = dq()
#
#     while True:
#         if d_tree.count(0) == N:
#             print(level)
#             return
#
#
#
#
#
#
#
#
# T = int(input())
#
# for tc in range(1,T+1):
#     N = int(input())
#     trees = list(map(int,input().split()))
#     trees.sort() # 작은 것부터
#     max_tree = trees[-1]
#     d_tree = [(max_tree-tree) for tree in trees] # 뒤로 갈 수록 차이 큼
#     # print(d_tree)
#     level = 0
#     water = 0 # 물 뿌리개 용량
#
#     while d_tree.count(0) != 0:
#         d_tree.remove(0)
#
#     # d_tree = dq(d_tree)
#     while d_tree:
#         level += 1
#
#         if level % 2: # 홀수날
#             water = 1
#         else:
#             water = 2 # 짝수날
#
#
#
#         if water == 2: # 짝수날
#             for i in range(len(d_tree)):
#                 if d_tree[i]>=2: # 차이가 2보다 크면
#                     d_tree[i] -= water
#                     d_tree.sort(reverse=True)
#                     break
#
#         else: # 홀수 날일 때
#             for i in range(len(d_tree)):
#                 if d_tree[i]%2: # 값이 홀수면
#                     d_tree[i] -= water
#                     d_tree.sort(reverse=True)
#                     break
#             else: # 다 돌고도 내부에 홀수가 없으면
#                 if len(d_tree) == 1 and d_tree[0] ==2: # 2 하나만 남으면 그냥 냅두는게 이득
#                     continue
#
#                 else:
#                     d_tree[0] -= water
#                     d_tree.sort(reverse=True)
#
#         while d_tree.count(0) !=0:
#             d_tree.remove(0)
#
#
#
#     print(f'#{tc} {level}')
#
#
#






# 마법의 물뿌리개
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))


    def magic():

        day = 1
        target = max(arr)  # 목표 나무의 크기 (가장 큰 나무)
        if all(arr[i] == target for i in range(N)): return 0



        while arr:
            if day % 2 == 0:  # 짝수 날
                water = 2  # 물을 주면 나무가 2만큼 자람
                for i in range(N):
                    tree = arr[i]
                    if tree + water <= target: # 만약 d_tree가 존재한다면(tree가 아직 max보다 작다면)
                        arr[i] += water # 해당 tree에 물 줘서 d_tree를 줄인다
                        break

            else:  # 홀수 날
                water = 1  # 물을 주면 1만큼 자람
                for i in range(N):
                    tree = arr[i]
                    # 남은 길이가 홀수거나 2이상인 경우 물을 줌
                    if (target - tree) % 2: # d_tree[i]가 홀수
                        arr[i] += water
                        break
                else: #짝수가 없으면
                    # 남은 길이가 2 이상이면서 짝수인 경우가 더 있으면 물을 줌
                    if target - tree == 2 and arr.count(target) == N-1:
                        continue
                    else:
                        arr[i] += water

            while arr.count(target):
                arr.remove(target)
            if all(arr[i] == target for i in range(N)): return day
            day += 1



    print(f'#{tc} {magic()}')