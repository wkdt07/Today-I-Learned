# (-1)**i 사용
N,K,M = map(int,input().split())
lst = [i for i in range(1,N+1)]
vst = [0] * (N+1)
result = []
cnt = 0
i = K - 1
while cnt != N:
    if cnt % M==0 and cnt !=0:
        lst.reverse()
    if not vst[i]:
        print(lst[i])
        vst[i] = 1
        cnt += 1
        # 인덱스 변경해야함
        i += K
        if K > N:
            K -= N

    else:
        i += 1



