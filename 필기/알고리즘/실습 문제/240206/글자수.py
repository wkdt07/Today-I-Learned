T = int(input())

for t in range(1,T+1):
    # str1 = list(map(str,input()))
    # str2 = list(map(str,input())) 어차피 str도 따로따로 순회 가능

    str1 = input()
    str2 = input()

    cnt_lst = []
    for s in str1:
        num = str2.count(s)
        cnt_lst.append(num) # 그냥 변수 할당 안 해도 됨

    cnt = max(cnt_lst)

    print(f'#{t} {cnt}')

