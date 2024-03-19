T = int(input())

for t in range(1,T+1):
    N = int(input())
    ftr = [list(map(int,input().split())) for _ in range(N)]
    vst = [0] *N

    min_v = float('inf')
    def choice(temp =0 ,level=0):
        global min_v
        if level == N:
            min_v = min(min_v,temp)
            return

        if temp >= min_v: # 가지치기
            return

        for j in range(N):
            if not vst[j]:
                vst[j] = 1
                choice(temp+ftr[level][j],level+1)
                vst[j] = 0

    choice()
    print(f'#{t} {min_v}')