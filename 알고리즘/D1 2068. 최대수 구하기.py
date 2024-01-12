T=int(input())

for t in range(1,T+1):
    a=list(map(int,input().split()))
    a.sort(reverse=True)

    print(f'#{t} {a[0]}')