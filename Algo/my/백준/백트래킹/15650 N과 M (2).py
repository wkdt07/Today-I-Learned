N, M = map(int, input().split())

lst =  list(range(1,N+1))

vst = [0] * (N+1)
vst_comb = []
def comb(ans = [],num = 0):
    ans.sort()
    if ans in vst_comb:
        return

    if num == M:
        print(*ans)
        vst_comb.append(ans)
        return

    for i in range(1,N+1):
        if not vst[i]:
            vst[i] = 1
            # ans.append(i)
            comb(ans+[i],num+1)
            vst[i] = 0

comb()