def change(n):
    arr = [100,50,10]
    cnt = [0]*len(arr)
    dic = {}
    for i in range(len(arr)):
        if n // arr[i] != 0:
            cnt[i] = (n//arr[i])
            n = n % arr[i]
        dic.setdefault(arr[i], cnt[i]) #이거 위치에서 해맸음
    return dic

print(change(380))


