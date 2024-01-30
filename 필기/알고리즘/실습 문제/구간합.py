T = int(input())

for t in range(1,T+1):
    sum_lst = []
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    # sum_v = 0 sumv 리셋을 여기서 하면 계속 누적됨
    for i in range(0,n-m+1):
        sum_v = 0 #리셋은 여기서(i가 바뀔때마다)
        for k in range(0,m):
            sum_v += arr[i+k]
        sum_lst.append(sum_v)
    result = max(sum_lst)-min(sum_lst)
    print(f'#{t} {result}')