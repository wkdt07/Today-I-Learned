sum = 0

sum_lst = []
for i in range(10):
    sum += int(input())
    sum_lst.append(sum)
    if sum >= 100:
        max_index = i
        break
    if i == 9 and sum < 100: # 만약 100이 안 넘는다면?
        max_index = i

if max_index== 0: # 첫 줄에 100 넘어버리면 아래 부분이 런타임 에러
    print(sum_lst[max_index])

elif (sum_lst[max_index]-100)<=(100-sum_lst[max_index-1]):
    print(sum_lst[max_index])


else:
    print(sum_lst[max_index-1])










'''sum = 0

sum_lst = []
for i in range(10):
    sum += int(input())
    sum_lst.append(sum)
    if sum >= 100:
        max_index = i
        break
    else: # 끝까지 sum<100
        max_index = 9

if max_index== 0: # 첫 줄에 100 넘어버리면 아래 부분이 런타임 에러
    print(sum_lst[max_index])

elif max_index == 9:
    print(sum_lst[9])

elif (sum_lst[max_index]-100)<=(100-sum_lst[max_index-1]):
    print(sum_lst[max_index])


elif (sum_lst[max_index]-100)>(100-sum_lst[max_index-1]):
    print(sum_lst[max_index-1])'''


