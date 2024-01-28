# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int,input().split()) for _ in range(N))]

# N,M = map(int,input().split())

# arr1 = [list(map(int,input().split())) for _ in range(N) ]

# arr2 = [list(map(int,input().split())) for _ in range(N) ]

# for n in range(N):
#     for m in range(M):
#         print(arr1[n][m]+arr2[n][m],end=' ')
#     print()

# arr = [list(map(int,input().split())) for i in range(9)]

# # print(arr)

# for n in range(9):
#     lst = arr[n]
#     mx = 0
#     mx_lst = []
#     n_lst = []
#     m_lst = []
#     for m in range(9):
#         if mx <= lst[m]:
#             mx = lst[m]
#             idx_n = n
#             idx_m = m
#             mx_lst.append(mx)
#             n_lst.append(idx_n)
#             m_lst.append(idx_m)
# print(mx_lst)
# print(m_lst)
# print(n_lst)                    


# arr = [list(map(int,input().split())) for i in range(9)]

# lst = []

# for i in range(9):
#     lst.extend(arr[i])

# mx = max(lst)

# idx = lst.index(mx)

# n = idx // 9
# m = idx % 9

# print(mx)
# print(n+1,m+1)

# arr = [list(map(str,input())) for _ in range (5)]

# for i in range(5):
#     for lst in arr:
#         for j in range(len(lst)):
#             print(arr[j][i],end='')



# 2차원 리스트를 입력받는 방법 -> 행, 열이라는 표현 -> matrix[y][x]
# 1. for문 활용
# rows = int(input("행의 개수를 입력하세요"))
# matrix = []

# for i in range(rows):
#     row = list(map(int, input().split()))
#     matrix.append(row)

# for row in matrix:
#     print(row)

# 2. 리스트 컴프리헨션
# matrix = [list(map(int, input().split())) for _ in range(rows)]

# for row in matrix:
#     print(row)

