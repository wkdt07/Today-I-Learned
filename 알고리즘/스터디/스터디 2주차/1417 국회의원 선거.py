N = int(input())

lst = [0]*(N+1)
for n in range(1,N+1):
    lst[n] = int(input())

fst = lst[1]
max_v = max(lst)
cnt = 0
while max_v != fst:
    idx = lst.index(max_v)
    lst[idx] -= 1
    lst[1] += 1
    # lst[1]이 max일 때 끝내야 한다. 만약 밑에 재지정이 없으면 lst가 동률일 때 lst[idx] = lst[1]이 되어버림
    fst = lst[1]
    max_v = max(lst)
    cnt+=1


k = lst.count(fst)

if k>1:
    cnt += 1

print(cnt)


