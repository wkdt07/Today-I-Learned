# n = int(input())
#
# cnt = 0
# i = 0
# while True:
#     if '666' in str(i):
#         cnt += 1
#         if cnt == n:
#             print(i)
#             break
#         i += 1
#     else:
#         i += 1
# 592ms


n = int(input())

cnt = 0
i = 666 # 이러면 아주 조금 더 빠름
while True:
    if '666' in str(i):
        cnt += 1
        if cnt == n:
            print(i)
            break
        i += 1
    else:
        i += 1

# 580ms