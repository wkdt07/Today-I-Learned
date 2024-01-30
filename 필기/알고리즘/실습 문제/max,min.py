T =int(input())

for t in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    print(f'#{t} {max(lst)-min(lst)}')