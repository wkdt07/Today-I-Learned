N = 9
data_1 = '123456789'
arr_1 = []
# 아래에 코드를 작성하시오.
for i in range(N):
    arr_1.append(data_1[i])

print(arr_1)


M = 15
data_2 = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'
# 아래에 코드를 작성하시오.
arr_2 = list(map(int,data_2.split()))

for data in arr_2:
    if data % 2 != 0:
        print(data)