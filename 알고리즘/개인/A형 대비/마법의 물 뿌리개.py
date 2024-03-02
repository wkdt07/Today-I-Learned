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
def bfs(d_tree,level):
    q = dq()
    
    while True:
        if d_tree.count(0) == N:
            print(level)
            return








T = int(input())

for tc in range(1,T+1):
    N = int(input())
    trees = list(map(int,input().split()))
    trees.sort() # 큰 것부터
    max_tree = trees[-1]
    d_tree = [(max_tree-tree) for tree in trees] # 뒤로 갈 수록 차이 큼
    # print(d_tree)
    level = 0
    water = 0 # 물 뿌리개 용량

    # d_tree = dq(d_tree)
    while d_tree.count(0) != N:
        level += 1

        if level % 2:
            water = 1
        else:
            water = 2



        if water == 2:
            for i in range(len(d_tree)):
                if d_tree[i] and not d_tree[i]%2:
                    d_tree[i] -= water
                    d_tree.sort(reverse = True)
                    break
                else:
                    continue

        else:
            for i in range(len(d_tree)):
                if d_tree[i] and d_tree[i]%2:
                    d_tree[i] -= water
                    d_tree.sort(reverse = True)
                    break
                else:
                    continue


    print(f'#{tc} {level}')