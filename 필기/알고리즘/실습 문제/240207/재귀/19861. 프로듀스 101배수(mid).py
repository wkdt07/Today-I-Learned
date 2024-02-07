N = int(input())
X = list(map(int, input().split()))


def find101(n, x, ans = '', idx = 0, res = 0):
    if idx == 0:
        ans = str(x[0])
        res = x[0]
        pr = x[0]
        find101(n, x, ans, idx+1, res)

    if idx == n:
        if res % 101 == 0 and res != 0:
            print(ans)
        return

    find101(n, x, ans + '*' + str(x[idx]), idx + 1, res * x[idx])
    find101(n, x, ans + '+' + str(x[idx]), idx + 1, res + x[idx])
    find101(n, x, ans + '-' + str(x[idx]), idx + 1, res - x[idx])

find101(N, X)







# import itertools

# N = int(input())
#
# nums = list(map(int,input().split()))
# i = 0
# def(nums,i):
#     if



# temp = []
# a = ['*','+','-']
# eval_lst = list(itertools.product(a,repeat=N-1))
# print(eval_lst)


temp = []
# def func(nums):
#     k = nums.pop()
#
#     result = nums[0]
#
#     if nums == []:
#         return temp
#
#     if (result * k) % 101 == 0:
#         temp.append(f'*{k}')
#
#     elif (result + k) % 101 == 0:
#         temp.append(f'+{k}')
#
#     elif (result - k) % 101 == 0:
#         temp.append(f'-{k}')
#
#     result = func(nums)
# print(func(nums))





#     '''        a = nums.pop()
#         #num=0도 생각
#         if (result * a) % 101 == 0:
#             temp.append(f'*{a}')
#             return(func(result))
#         else:
#             result *= a
#
#         if (result + a) % 101 == 0:
#             temp.append(f'+{a}')
#             return(func(result))
#         else:
#             result += a
#
#         if (result - a) % 101 == 0:
#             temp.append(f'-{a}')
#             return(func(result))
#         else:
#             result -= a
#
#
#
#     return temp
#
# print(func(nums))'''