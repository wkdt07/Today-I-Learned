T = int(input())

for t in range(1,T+1):
    N,M = map(int,input().split()) # N은 인원 수, M은 신청서 갯수
    # rat = [[] for _ in range(N)]
    # 대표자를 찾아서 max값만 구하면 됨, 대표자의 max가 그룹의 갯수..? 아님
    # 그냥 순회하는게 빠를 듯 어차피 100개밖에 안되고

    rep = [_ for _ in range(N+1)]
    cand = list(map(int,input().split()))

    def find_set(x) :
        if rep[x] == x:
            return x

        rep[x] = find_set(rep[x])
        return rep[x]

    def union(x,y):
        x = find_set(x)
        y = find_set(y)
        if x>y:
            rep[x] = y
        elif x<y:
            rep[y] = x

    for i in range(0,len(cand),2):
        union(cand[i],cand[i+1])

    cnt = 0
    vst = []
    for i in range(1,len(rep)):
        if i == rep[i]:
            cnt += 1
    # cnt = 0
    # vst = []
    # for r in rep[1:]:
    #     if r not in vst:
    #         cnt += 1
    #         vst.append(r)
    '''
    1
    4 3
    1 2 3 4 2 4
    '''
    for r in rep[1:]:
        find_set(r)

    print(rep)
    print(f'#{t} {cnt}')



