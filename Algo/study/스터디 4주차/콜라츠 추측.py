import sys

while True:
    a,b = map(int, sys.stdin.readline().strip().split())

    if a == 0 and b == 0:
        break
    a_lst = [-100,a] # 어차피 마이너스는 계산상 절대 안 나오고, 무조건 끝나긴 해야해서
    k = a
    while True:
        if k == 1 :
            break

        if k % 2:
            k = 3 * k + 1
            a_lst.append(k)
        else:
            k //= 2
            a_lst.append(k)

    # now_b = b
    b_lst = [-200,b]
    k = b
    while True:
        if k == 1 :
            break

        if k % 2:
            k = 3 * k + 1
            b_lst.append(k)
        else:
            k //= 2
            b_lst.append(k)

    # print(a_lst)
    # print(b_lst)
    #
    # a_len = len(a_lst)
    # b_len = len(b_lst)
    # min_len = min(a_len, b_len)
    # for i in range(-1, -min_len-1, -1): # 역순으로 순회
    for i in range(-1,-10000,-1):
        if a_lst[i] != b_lst[i]:
            break
    print(f'{a} needs {len(a_lst) + i} steps, {b} needs {len(b_lst) +i} steps, they meet at {int(a_lst[i+1])}')
