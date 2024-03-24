import sys
sys.stdin = open("./input.txt","r")

N , K = map(int, input().split())

temp_lst = list(map(int, input().split()))
sum_lst = []
for i in range(N-K+1):
    sum_v = 0
    for k in range(K):
        sum_v += temp_lst[i+k] # 인덱스 설정 조금 헤맸음
    sum_lst.append(sum_v)


print(max(sum_lst))