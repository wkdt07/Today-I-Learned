import copy

N = int(input())

resv=[]
max_e = 0
for n in range(N):
    s,e = map(int,input().split())
    resv.append((s,e))
    if e >= max_e:
        max_e = e

cnt_lst = []
for a in range(N-1):
    f = resv[a]
    time = [0] * (e+1)
    sf, ef = f
    for i in range(sf, ef):
        time[i] = 1
        cnt = 1
    time_r = copy.deepcopy(time)
    for b in range(a,N):
        snd = resv[b]
        s2,e2 = snd
        for j in range(s2, e2):
            time_r[j] += 1
        if time_r.count(2) == 0:
            cnt += 1
        else:
            time_r = copy.deepcopy(time)
            continue
    cnt_lst.append(cnt)

print(max(cnt_lst))







