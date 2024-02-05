N = int(input())

arr = []

for i in range(N):
    arr_lst = list(map(int,input().split()))
    arr.append(arr_lst)

K = int(input())
lst = []
for y in range(N):
    for x in range(N):
        sumv = 0
        for k in range(1,K+1):
            dir = [(-1,-1),(-1,1),(1,-1),(1,1)]
            for dx,dy in dir:
                ny = k*dy+y
                nx = k*dx+x
                if 0 <= nx < N and 0 <= ny < N:
                    sumv += arr[ny][nx]
            lst.append(sumv)

print(max(lst))




# # dir = [(-1,-1), (1,1), (1,-1), (-1,1)]
# x = [-1,1,0]
# y = [-1,1,0]
#
#
#
# lst = []
#

# for i,j in range(N): #이런 식도 되나? 안됨.
# for i in range(N):
#     for j in range(N):
#         sumv = 0
#         for dx in x:
#             for dy in y:
#                 for k in range(1,K+1):
#                     try:
#                         sumv += arr[i+k*dx][i+k*dy]
#                     except:
#                         pass
#         lst.append(sumv)
#
# print(max(lst))


