T = int(input())

for t in range(T):
    W,N = map(int,input().split())
    arr = [0] * (N+1)
    for _ in range(N):
        i,w = map(int,input().split())
        arr[i] = w
    print(arr)