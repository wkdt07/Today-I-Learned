


T = int(input())

for t in range(1,T+1):
    arr = [1,2,3,4,5,6,7,8,9,10,11,12]

    n = len(arr)
    subset = []
    for i in range(1 << n):
        s = []
        for j in range(n):
            if i & (1 << j):
                s.append(arr[j])
        subset.append(s)  # 부분집합 모음
    n,k = map(int,input().split())

    count = 0
    for sub in subset:
        if (len(sub) == n) and (sum(sub)==k):
            count += 1

    print(f'#{t} {count}')