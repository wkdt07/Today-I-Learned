import sys
from itertools import combinations as cb

N , M = map(int,sys.stdin.readline().split())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

c_lst = []
h_lst = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            c_lst.append((i,j))
        if arr[i][j] == 1:
            h_lst.append((i,j))


def c_distance(h,lst):  # 특정 집에서의 치킨 거리를 구함
    min_v = float('inf')
    for c in lst:
        ic, jc = c
        ih, jh = h
        c_d = abs(ic - ih) + abs(jc - jh)
        if c_d < min_v:
            min_v = c_d
    return min_v

min_d = float('inf')

path = list(cb(c_lst,M))


for p in path:
    sum = 0
    for h in h_lst:
        sum += c_distance(h,p)
    if sum < min_d:
        min_d = sum

print(min_d)
# def total_d(level = 0):
#
#     global min_d
#     global path
#
#     if level == M:
#         sum_v = 0
#         for s in h_lst:
#             sum_v += c_distance(s,path)
#             if sum_v > min_d:
#                 return
#
#         if sum_v < min_d:
#             min_d = sum_v
#         return
#
#     for c in c_lst:
#         if c not in path:
#             if path:
#                 if path[0][0]<c[0]:
#                     path.append(c)
#
#                     total_d(level+1)
#                     path.pop()
#             else:
#                 path.append(c)
#                 total_d(level+1)
# if M>=len(c_lst):
#     min_d = 0
#     for s in h_lst:
#         min_d += c_distance(s,c_lst)
#
# else:
#     total_d()

# print(min_d)