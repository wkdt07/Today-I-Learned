T = int(input())

for t in range(1,T+1):
    N = int(input()) # 전선 갯수
    A = []
    B = []
    for _ in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    cnt = 0
    for i in range(N-1):
        for j in range(i+1,N):
            if (A[i]<=A[j] and B[i]>=B[j]) or (A[i]>=A[j] and B[i]<=B[j]): #같은거 포함?
                cnt += 1

    print(f'#{t} {cnt}')