T = int(input())

for t in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    lst.sort()
    mid_idx = len(lst)//2
    # print(mid_idx)
    # print(lst[mid_idx])

    lst_small = lst[:mid_idx]
    lst_small.sort()
    # print(len(lst_small))
    lst_big = lst[mid_idx:]
    # print(len(lst_big))
    lst_big.sort(reverse=True)
    arr = []
    i = 0
    while i < mid_idx:
        arr.append(lst_big[i])

        arr.append(lst_small[i])

        i += 1
    if len(lst) %2 !=0:
        arr.append(lst[mid_idx])

    print(f'#{t}',*arr[:10])

# T = int(input())
#
# for t in range(1, T + 1):
#     N = int(input())
#     nums = list(map(int, input().split()))
#     result = []
#
#     while len(nums) > 0:
#         # max_v = max(nums) 만약 max 못 쓰게 하면?
#
#         max_v = float('-inf')  # 음의 무한대. 계속 max값 초기화, 만약 문제 조건에 max_v에 대한 조건이 없으면 이렇게 써라
#         for i in range(len(nums)):
#             if nums[i] > max_v:
#                 max_v = nums[i]
#
#         nums.remove(max_v)
#         result.append(max_v)
#
#         min_v = min(nums)
#         nums.remove(min_v)
#         result.append(min_v)
#
#         print(result)
#         # print(f'#{t}', *result[:10])  # 언패킹 연산자로 출력