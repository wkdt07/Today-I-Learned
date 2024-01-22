# 아래 함수를 수정하시오.
def find_min_max(lst):
    lst.sort()
    min = lst[0]
    max = lst[len(lst)-1]
    return (min,max)


result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)
