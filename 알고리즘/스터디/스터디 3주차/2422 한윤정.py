# N 종류의 아이스크림. 1부터N까지 번호
# 특정 아이스크림끼리 합치면 좆같음. 이걸 피해서
# M은 섞어 먹으면 안 되는 조합의 갯수, N은 아이스크림 종류의 갯수
# 3개 선택할 때,가능한 방법 구하기


N,M = map(int,input().split())

lst = list(range(1,N+1))
f_dic = {}
for i in range(1,N+1):
    f_dic[i] = [0]
# f_lst = []
for _ in range(M):
    a,b = map(int,input().split())
    f_lst = sorted([a,b])
    f_dic[f_lst[0]].append(f_lst[1])

cnt = 0
for i in range(1,N-1):
    for j in range(i+1,N):
        if j in f_dic[i]:
            continue
        for k in range(j+1,N+1):
            if k in f_dic[i] or k in f_dic[j]:
                continue
            cnt += 1
print(cnt)