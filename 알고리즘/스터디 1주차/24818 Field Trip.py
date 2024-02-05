
# def check(i_lst):
#     stop = -1
#     for i in range(0,N):
#         for j in range(i,N):
#             if (sum(i_lst[:i]) == sum(i_lst[i:j])) and (sum(i_lst[i:j]) == sum(i_lst[j:N])):
#                 result = i,j
#                 return result
#
#     return stop



N = int(input())

def sub_sum(lst): # 누적합 함수
    sum_lst = []
    sum_v = 0
    for i in range(len(lst)):
        sum_v += lst[i]
        sum_lst.append(sum_v)
    return sum_lst


i_lst = list(map(int, input().split()))

sum_lst = sub_sum(i_lst)
n = len(sum_lst)

if sum_lst[n-1]%3 == 0 and (2*(sum_lst[n-1]//3) in sum_lst):
    i,j = sum_lst.index((sum_lst[n-1]//3))+1,sum_lst.index((sum_lst[n-1]//3)*2)+1
    result = i,j
else:
    result = [-1]

print(*result)





