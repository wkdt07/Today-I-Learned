N,M = map(int,input().split()) # N은 끊어진 수, M은 브랜드 수

minv = float('inf')
pac_lst = []
sol_lst = []

for _ in range(M):
    pac, sol = map(int, input().split())
    pac_lst.append(pac)
    sol_lst.append(sol)

pac = min(pac_lst) # 굳이 pac과 sol을 같은 브랜드에서 살 필요가 없다
sol = min(sol_lst)
cost = 0
if pac > (sol * 6) :
    cost = sol * N
else:
    a,b =divmod(N,6) #a: 패키지로 사야하는 수, b: 나머지
    cost += a * pac

    if b * sol >= pac :
            cost += pac
    else:
        cost += sol*b

print(cost)
#
# pac,sol = map(int,input().split())

#     minv = min(minv,cost)