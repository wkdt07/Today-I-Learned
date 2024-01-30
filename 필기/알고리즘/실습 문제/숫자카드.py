T = int(input())

for t in range(1,T+1):
    N = int(input())
    string = input()
    # num = int(input())
    num_lst = []
    # while num%10 != 0:
    #     k = num % 10
    #     num_lst.append(k)
    #     num = num//10 이러면 맨 앞 자리가 0일 때는 판단 불가


    for i in string:
        num_lst.append(int(i))

    cnt_lst = [0] * 10

    for num in num_lst:
        for i in range(len(cnt_lst)):
            if num == i:
                cnt_lst[i] += 1


    cnt_lst.reverse()
    max_c = max(cnt_lst)
    max_v = 9 -cnt_lst.index(max_c)
    print(f'#{t} {max_v} {max_c}')



