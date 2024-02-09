N = int(input())

cls = [list(map(int,input().split())) for _ in range(N)]
cnt_lst = []
for o in range(N):
    cnt = 0

    for i in range(N):
        for j in range(5):
            if (o != i) and cls[i][j] == cls[o][j]:
                cnt += 1
                break # 사람 기준이니깐 + 되면 빠져나가야함

            else:
                continue

    cnt_lst.append(cnt)


max_v = max(cnt_lst)

idx = cnt_lst.index(max_v)+1

print(idx)



# N = int(input())
#
# cls = [list(map(int,input().split())) for _ in range(N)]
#
# def cnt_func(o):
#     cnt = 0
#     for i in range(N):
#         for j in range(5):
#             if (o != i) and cls[i][j] == cls[o][j]:
#                 cnt += 1
#
#             elif len(cls) == 1:
#                 return 1
#
#             else:
#                 continue
#
#     return cnt
#
# cnt_lst = []
#
# for i in range(N):
#     cnt_lst.append(cnt_func(i))
#
# print(cnt_lst)
# max_v = max(cnt_lst)
#
# idx = cnt_lst.index(max_v)+1
#
# print(idx)
#