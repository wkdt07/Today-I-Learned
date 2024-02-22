T = int(input())

for t in range(1,T+1):
    N = input()
    n = float(N)
    tmp = str(2*n)
    lst = []
    while tmp != 1:
        a = tmp[0]
        lst.append(a)
        tmp2 = str((float(tmp)-float(tmp[0]))*2)
        if tmp2[1:] == tmp[1:]:
            break
        if len(lst)>=13:
            break
        tmp = tmp2
    if len(lst)==13:
        print(f'#{t} overflow')
    else:
        rst = ''.join(lst)
        print(f'#{t} {rst}')



