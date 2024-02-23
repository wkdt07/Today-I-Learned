T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    M = bin(M)[2:]
    print(M)
    rst = 'ON'
    for i in range(N):
        if not(M & (1<<N)):
            rst = 'OFF'
            break

