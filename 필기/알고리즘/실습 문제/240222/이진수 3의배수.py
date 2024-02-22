N,K = map(int,input().split())
# lst = [1]*K + [0]*(N-K)
lst = [1,2,3]
def pac(n):
    if n == 0 or n == 1:
        return 1
    return n*pac(n-1)
vst = [0] * len(lst)
vst_lst = []
cb_lst = []
cbset = []
def cb(lst,i=0):
    global cb_lst
    global cbset
    global vst

    while len(cbset) != pac(len(lst)):
        if len(cb_lst) == N and cb_lst not in vst_lst:
            cbset.append(cb_lst)
            vst_lst.append(cb_lst)
            vst = [0] * N
            return
        for i in range(N):
            if not vst[i]:
                cb_lst.append(lst[i])
                vst[i] = 1
            else:
                continue
            cb(lst,i)

cb(lst,vst)
print(cbset)