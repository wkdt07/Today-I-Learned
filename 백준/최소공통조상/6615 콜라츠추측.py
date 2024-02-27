import sys

while True:
    a,b = map(int, sys.stdin.readline().strip().split())

    now_a = a
    now_b = b
    if now_a == 0 and now_b == 0:
        break
    a_lst = [-1,a] # 어차피 마이너스는 계산상 절대 안 나오고, 무조건 끝나긴 해야해서
    while True:
        if now_a == 1 :
            break

        if now_a % 2:
            now_a = 3 * now_a + 1
            a_lst.append(now_a)
        else:
            now_a //= 2
            a_lst.append(now_a)

    # now_b = b
    b_lst = [-2,b]
    while True:
        if now_b == 1 :
            break

        if now_b % 2:
            temp = 3 * now_b + 1
            b_lst.append(now_b)
        else:
            now_b //= 2
            b_lst.append(now_b)

    # print(a_lst)
    # print(b_lst)
    #
    a_len = len(a_lst)
    b_len = len(b_lst)
    min_len = min(a_len, b_len)
    for i in range(-1, -min_len-1, -1): # 역순으로 순회
        if a_lst[i] != b_lst[i]:
            t = -i
            break
    print(f'{a} needs {a_len - t} steps, {b} needs {b_len - t} steps, they meet at {a_lst[-t+1]}')



# import sys
#
#
# vst = [0] * (100000)
#
# depth_A = 0
# depth_B = 0
# def dfs1(a,depth=0):
#     global depth_A
#     global c
#     if a == 1 or a == 0:
#         return
#
#     if not a%2:
#         a_n = a//2
#         if not vst[a_n]:
#             # parent[a_n] = a
#             vst[a_n] = 1
#             dfs1(a_n,depth+1)
#         else:
#             depth_A = depth
#             c = a
#             return
#     else:
#         a_n = 3 * a + 1
#         if not vst[a_n]:
#             # parent[a_n] = a
#             vst[a_n] = 1
#             dfs1(a_n, depth + 1)
#         else:
#             depth_A = depth
#             c = a
#             return
# def dfs2(b,depth=0):
#     global depth_B
#     global c
#
#     if b == 1 or b == 0:
#         return
#
#     if not b % 2:
#         b_n = b // 2
#         if not vst[b_n]:
#             # parent[a_n] = a
#             vst[b_n] = 1
#             dfs1(b_n, depth + 1)
#         else:
#             depth_B = depth
#             c = b_n
#             return
#     else:
#         b_n = 3*b+1
#         if not vst[b_n]:
#             # parent[a_n] = a
#             vst[b_n] = 1
#             dfs1(b_n, depth + 1)
#         else:
#             depth_B = depth
#             c = b_n
#             return
#
# a,b = map(int,sys.stdin.readline().split())
#
# depth_A = 0
# depth_B = 0
#
# print(f"{a} needs {depth_A} steps, {b} needs {depth_B} steps, they meet at {c}")
# # def dfs(p,depth = 0):
# #     global cnt
# #     global d_A
# #     global d_B
# #     if cnt == 2:
# #         return
# #     if p == A:
# #         d_A = depth
# #         cnt += 1
# #     if p == B:
# #         d_B = depth
# #         cnt += 1
# #
# #     if (p-1)//3 == (p-1)/3:
# #         c1 = (p-1)//3
# #         if not vst[c1]:
# #             vst[c1] = 1
# #             parent[c1] = p
# #             depth_lst[c1] = depth
# #             dfs(c1,depth + 1)
#
# #     c2 = p*2
# #     if not vst[c2]:
# #         parent[c2] = p
# #         depth_lst[c2] = depth
# #         vst[c2] = 1
# #         dfs(c2,depth + 1)
# #
# #
# # dfs(1,0)
# #
# # print(d_A,d_B)