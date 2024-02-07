# nums = list(map(int,input()))
# def my_sum(n):
#     if n > 0:
#         a = nums[n]
#         return a+my_sum(n-1)
#     else:
#         return nums[0]
#
#
# n = len(nums)-1
#
# result = my_sum(n)
#
# print(result)
#


nums = list(input())


def my_sum(nums):
    n = len(nums)
    if n > 1:
        a = nums[0]
        return int(a) + my_sum(nums[1:])
    else:
        return int(nums[0])


result = my_sum(nums)

print(result)
'''
nums = input()

def my_sum(n):
    if n == 0:
        return int(nums[0])
    if n > 0:
        a = int(nums[n])
        return a+my_sum(n-1)

n = len(nums)-1

result = my_sum(n)

print(result)
'''