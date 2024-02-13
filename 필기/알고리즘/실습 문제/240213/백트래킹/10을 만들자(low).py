N = int(input())
rst = 0
def ten(N,cnt=0,ans = 0):
    # global ans
    global rst
    if cnt == N and ans == 10:
        rst += 1
        # ans -= k
        return
    else:
        if cnt >= N or ans > 10:
            # ans -= k
            return
        else:
            for i in range(1,10):
                # k = i
                ten(N,cnt+1,ans+i)

ten(N)
print(rst)


# while cnt <= N:
#     rst = 0
#
#     for i in range(1,10):
#         rst += i
#         cnt += 1
#         if cnt == 3 and ans == 10:
#             ans += 1
#             break
#
#         else:
#             for
