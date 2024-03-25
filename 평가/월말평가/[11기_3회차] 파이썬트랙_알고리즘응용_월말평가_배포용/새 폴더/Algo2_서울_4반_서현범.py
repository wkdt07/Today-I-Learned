T = int(input())

for t in range(1,T+1):
    N,W_max = map(int,input().split()) # 섬의 갯수와 최대예산
    w_lst = list(map(int,input().split())) # 각각의 다리의 가격(총 N개)
    # 단순히 정렬해서 최대 갯수를 구해도 됨
    sum_v =sum(w_lst)
    if sum_v <= W_max:
        print(f'#{t} {N} {sum_v}') # 만약 값의 총합이 예산보다 작으면 그냥 다 더한 값이 답임
        continue

    w_lst.sort() # 가격들 정렬
    sub_w = 0 # 누적합
    cnt = 0 # 인덱스로 사용할 인자이자, 최대 다리 갯수

    while cnt < N:
        temp = w_lst[cnt]
        sub_w += temp
        if sub_w > W_max: # 만약 합이 예산을 넘어가면
            sub_w -= temp # 취소하고
            break # 탈출
        cnt += 1 # 하나 지음

    print(f'#{t} {cnt} {sub_w}')

# 효율적인 방법 -> DP 이용? 어차피 nlogn이냐 n이냐의 차이라서 그닥 큰 의민 없을거 같은데...
# 아니네 차이 많이 나네
# heappop도 import 못 쓰니깐 의미가 없고...
# 유일하게 시간 줄일만한게 sort인데... 흠...
# sort 에서 nlogn 잡아먹고 이후에 최대 n을 더 잡아먹긴 하지만... (최대 nlogn+n)
# 그냥 이진법에 dfs로 처리할까? 근데 그래도 어차피 그 수만큼 더 잡아먹잖아
# 그냥 DP 쓰는게 가장 깔끔하겠다.
# 생각해보니깐 어차피 DP 써도 sort 해야하네.

