# N,K = map(int,input().split())
# lst = []
# for _ in range(N):
#     n = int(input())
#     lst.append(n)
#
# max_v = max(lst)
# a = max_v
# g_lst = []
#
# while a <= max_v:
#     trial_lst = []
#     for n in lst:
#         trial = n//a
#         trial_lst.append(trial)
#         if sum(trial_lst) == K:
#             g_lst.append(a)
#     a += 1
# # print(g_lst)
# print(max(g_lst))


# N,K = map(int,input().split())
# lst = []
# for _ in range(N):
#     n = int(input())
#     lst.append(n)
#
# # print(lst)
#
# sum_v = 0
# max_v = max(lst)
# a = 1
# g_lst = []
#
# while a <= max_v:
#     trial_lst = []
#     for n in lst:
#         trial = n//a
#         trial_lst.append(trial)
#         if sum(trial_lst) == K:
#             g_lst.append(a)
#     a += 1
# # print(g_lst)
# print(max(g_lst))
# # 1 87 92 상황에선 불가능(1이 나와야 함)

N, K = map(int, input().split())
lst = list(int(input()) for _ in range(N))

s, e = 0, max(lst)

while s <= e:
    mid = (s + e) // 2
    cnt = 0
    for l in lst:  # 현재 mid 길이로 츄러스를 잘라 만들 수 있는 츄러스의 개수 총합
        cnt += l // mid

    if cnt >= K: # cnt가 K 보다 크면 더 큰 놈으로 잘라여 된다
        s = mid + 1

    else: # cnt가 K보다 작으면 더 작은 놈으로 잘라야 한다
        e = mid - 1

print(e)