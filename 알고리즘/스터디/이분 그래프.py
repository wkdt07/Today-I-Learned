T = int(input())

for _ in range(T):
    V,E = map(int,input().split()) # V는 정점 수, E는 간선 수
    vst1 = [0] * (V+1) # 사용 했는지
    vst2 = [0] * (V+1)
    vst = [0] *(V+1)

    relation = [[] for _ in range(V+1)]
    for e in range(E):
        s,e = map(int,input().split())
        relation[s].append(e)
        relation[e].append(s)



    start = 1
    while start<=V:
        if not vst[start]:
            vst[start] = 1
            vst1[start] = 1
            for end in relation[start]:
                if not vst[end]:
                    vst2[end] = 1
                    vst[end] = 1
        start+=1

    rst = 'YES'
    def check():
        global rst
        for i in range(1,V):
            if vst1[i]:
                for j in relation[i]:
                    if vst1[j]:
                        rst = 'NO'

            elif vst2[i]:
                for j in relation[i]:
                    if vst2[j]:
                        rst = 'NO'

                # print('YES')
    check()
    print(rst)


    # v = 1
    # while v <= V:
    #     if v not in lst_2 and v not in lst_1:
    #         # vst[v] = 1
    #         lst_1.append(v)
    #         for end in relation[v]:
    #             if end not in lst_1 and end not in lst_2:
    #                 # vst[end] = 1
    #                 lst_2.append(end)
    #     v += 1
    # print(lst_1)
    # print(lst_2)