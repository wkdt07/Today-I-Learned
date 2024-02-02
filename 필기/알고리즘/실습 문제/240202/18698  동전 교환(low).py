m = int(input())

cnt = 0
while m != 0:
    if m // 500 != 0:
        cnt += m //500
        m = m% 500

    elif m // 100 != 0:
        cnt += m //100
        m = m% 100

    elif m // 50 != 0:
        cnt += m //50
        m = m% 50

    elif m // 10 != 0:
        cnt += m //10
        m = m% 10

print(cnt)