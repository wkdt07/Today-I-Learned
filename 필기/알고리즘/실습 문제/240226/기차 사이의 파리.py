T = int(input())

for t in range(1,T+1):
    D,A,B,F = map(int,input().split())
    v = A+B
    time = D/v
    rst = F*time
    print(f'#{t} {rst:6f}')