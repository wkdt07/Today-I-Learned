# 소인수 분해 했을 떄 연속되는 세트로 묶을 수 있냐/ 이건 곱하기로 연결하는 경우, 이 문제는 합으로 연결

# 소수는 불가능 아니네 7도 소순데 0!+3!으로 가능

def fac(n):
    ans = 1
    if n == 0:
         return ans
    else:
        for i in range(1, n+1):
            ans *= i
    return ans

N = int(input())

# print(pac(20)<1000000000000000000) # False, 최대 20
lst = [fac(i) for i in range(20,-1,-1)]

def check(N):

    if N == 0:
        return 'NO'

    # for i in range(N,-1,-1):
    #     if fac(i)<=N:
    #         max_i = i
    #         break
    # lst = [fac(i) for i in range(max_i,-1,-1)]
    # 시간초과 난다. 최대한 줄이려면 그냥 범위 내 팩토리얼 최대로 받을 수 있는 20으로 잡는게 좋음

    for k in lst:
        if N - k >=0:
            N -= k

    if N == 0:
        return 'YES'

    else: return 'NO'

print(check(N))

'''
시간초과
def check(n):
    lst = [pac(i) for i in range(0,n)]
    lst.sort(reverse = True)
    if n in lst:
        return 'YES'
    for k in range(1,n+1):
        for t in list(itertools.combinations(lst,k)):
            sum_v = sum(t)
            if sum_v == n:
                return 'YES'
            else:
                continue
    return 'NO'

print(check(N))
'''