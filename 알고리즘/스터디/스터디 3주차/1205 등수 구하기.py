N,new,P = map(int,input().split()) # N은 기존 점수 개수, new는 새로운 점수, P는 랭킹 한계
lst = list(map(int,input().split()))
lst.append(new)

lst.sort(reverse=True)

rank = lst.index(new)

# rank로 넣으면 동점자가 같은 점수일 때가 적용이 안 됨

rank += lst.count(new)

if rank > P:
    print(-1)

else:
    print(rank)