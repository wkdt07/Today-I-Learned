try:
    while True:
        n = int(input())
        ans = '1'*len(str(n))
        while int(ans)%n != 0 :
            ans += '1'
        print(len(ans))
except:
    pass