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
        d_trees.sort(reverse = True)

        if cnt % 2: # 홀수
            water = 1
        else:
            water = 2
        flag = False

        if water % 2: # 홀수 일 때
            for i in range(len(d_trees)):
                if d_trees[i]%2:
                    flag = True
                    d_trees[i] -= water
                    break
            if not flag:
                # 다 돌았는데 홀수가 없다면
                if d_trees[0] == 2 and len(d_trees) == 1: # 가장 큰 값이 2이면
                    # 그리고 나무가 하나만 남았으면.
                    # 나무가 2개 이상 남으면 오히려 2 2, 1 2, 1 0, 0 0 이랑 2 2, 2 0, 2 0, 0 0, 똑같음
                    # 3개일 때도 해보면 2 2 2, 2 1, 2, 0 으로 4일인데/ 2 2 2, 2 2, 2 2, 2, 2, 0으로 더 오래 걸림
                    continue
                else:
                    d_trees[0] -= water

        else: # 짝수 일 때

            for i in range(len(d_trees)):
                if d_trees[i] >= 2:
                    d_trees[i] -= water
                    break

        while d_trees.count(0):
            d_trees.remove(0)

    print(f'#{tc} {cnt}')