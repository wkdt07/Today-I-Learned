# 소인수 분해 했을 떄 연속되는 세트로 묶을 수 있냐/ 이건 곱하기로 연결하는 경우, 이 문제는 합으로 연결

# 소수는 불가능 아니네 7도 소순데 0!+3!으로 가능

import itertools
def pac(n):
    ans = 1
    if n == 0:
         return ans
    else:
        for i in range(1, n+1):
            ans *= i
    return ans

N = int(input())



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
