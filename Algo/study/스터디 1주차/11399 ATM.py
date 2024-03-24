
# 메모리 초과 - itertools
# import itertools

def sum_cnt(lst): # 누적합 함수
    sum_v = 0
    result = 0
    for i in lst:
        sum_v += i
        result += sum_v
    return result


N = int(input())

P_lst = list(map(int,input().split()))

# p_per = list(itertools.permutations(P_lst, N))

P_lst.sort()

min_v = sum_cnt(P_lst)
print(min_v)



