
# 재귀 호출을 나눠서
n = int(input())

cnt = 0
def col(n):
    global cnt
    if n ==1:
        return cnt

    if n %2 == 0:
        n //= 2
        cnt+=1
        return col(n)
    else:
        n = 3*n + 1
        cnt += 1
        return col(n)

print(col(n))