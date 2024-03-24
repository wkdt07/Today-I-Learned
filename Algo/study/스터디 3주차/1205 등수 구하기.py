N,new,P = map(int,input().split()) # N은 기존 점수 개수, new는 새로운 점수, P는 랭킹 한계
# 시발 설마 N = 0일 때 때문에 그러나...EOF error
# 그러네 시발 ㅋㅋㅋㅋㅋㅋㅋ
if N ==0:
    print(1)
else:
    lst = list(map(int,input().split()))

    lst.append(new)

    lst.sort(reverse=True)
    # 이러면 만약 유일한 번호여도 +1이 되어버린다. 상관없네. 어차피 인덱스니깐 +1 해야됨
    # 동점자도 다 다른 번호로 나온다

    if lst.count(new) + lst.index(new) > P:
        print(-1)

    else:
        print(lst.index(new)+1) # 인덱스니깐