T=int(input())


def cal(arg):
    date=arg[0:4] + '/' + arg[4:6] + '/' + arg[6:8]
    return date

for t in range(1,T+1):
    arg=input()
    mm=int(arg[4:6])
    dd=int(arg[6:8])
    mm_31=[1, 3, 5, 7, 8, 10, 12]
    mm_30=[4, 6, 9, 11]


    if mm==2:
        if 1<=dd<=28:
            print(cal(arg))
        else:
            print(-1)

    elif mm in mm_31:
        if 1<=dd<=31:
            print(cal(arg))
        else:
            print(-1)

    elif mm in mm_30:
        if 1 <= dd <= 30:
            print(cal(arg))
        else:
            print(-1)

    else:
        print(-1)



