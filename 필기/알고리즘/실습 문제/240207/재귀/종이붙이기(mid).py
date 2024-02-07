T = int(input())

def func(N):
    n = N//10
    if n == 1 :
        return 1
    elif n == 2 :
        return 3

    else:
        return func(N-10)+2*func(N-20)



for t in range(1,T+1):
    N = int(input())
    result = func(N)

    print(f'#{t} {result}')
