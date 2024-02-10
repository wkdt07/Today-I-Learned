N = int(input())

arr = [input() for _ in range(N)]

# print(arr)
# par = 0
# for i in range(N):
#     for j in range(N-1):
#         if arr[i][j] == '.' and arr[i][j] == arr[i][j+1]:
#             par += 1
#             break
#         else:
#             continue
# print(par)

col = 0

for j in range(N-1):
    for i in range(N):
        if arr[j][i] == '.' and arr[j+1][i] == arr[j+1][i]:
            col += 1
            break

    # for 순서 변경
print(col)