import itertools

N , M = map(int, input().split())
nums = list(map(int, input().split()))


nums_comb = list(itertools.combinations(nums,3))

sum_lst = []

for comb in nums_comb:
    if sum(comb) <= M:
        sum_lst.append(sum(comb))

print(max(sum_lst))