# 아래 함수를 수정하시오.
def difference_sets(s1,s2):
    result = s1.difference(s2)
    return result


result = difference_sets({1, 2, 3}, {3, 4, 5})
print(result)
