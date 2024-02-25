M,N = map(int,input().split())

# 그냥 N이하의 소수에서 M이하의 소수를 뺀다

def prime_num(M,N):
    arr = [True for i in range(N+1)]
    m = int(N**0.5)
    arr[0],arr[1] = False,False
    for i in range(2,m+1):
        j = 2
        if arr[i]: # 갯수 확 줄여줄 수 있다. 굳이 False인걸 또 건들 필요는 없음
            while i*j<=N:
                arr[i*j] = False
                j += 1

    for i in range(M, N + 1):
        if arr[i]:
            print(i)

prime_num(M,N)
# 출력 초과라는데?

'''
def prime_num(n):
    arr = [True for i in range(n+1)]
    m = int(n**0.5)
    arr[0],arr[1] = False,False
    for i in range(2,m+1):
        j = 2
        while i*j<=n:
            arr[i*j] = False
            j += 1
    return arr

prime_lst= prime_num(N)

for i in range(M,N+1):
    if prime_lst[i]:
        print(i)
'''
