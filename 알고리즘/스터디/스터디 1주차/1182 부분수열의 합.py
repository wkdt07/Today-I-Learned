import itertools

N,S = map(int,input().split())
nums = list(map(int,input().split()))

cnt = 0
for i in range(1,N+1):
    combs = list(itertools.combinations(nums,i))
    for comb in combs:
        if sum(comb) == S:
            cnt += 1
print(cnt)