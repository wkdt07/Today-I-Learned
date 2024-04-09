T = int(input())

for tc in range(1,T+1):
    N = int(input())

    trees = list(map(int,input().split()))

    max_tree = max(trees)
    d_trees = []
    for tree in trees:
        d = max_tree - tree
        d_trees.append(d)

    i = 0
    while d_trees.count(0) != 0:
        d_trees.remove(0)
    # water = 0

    cnt = 0
    while d_trees:
        cnt += 1
        if cnt % 2: # 홀수
            water = 1
        else:
            water = 2

        if water