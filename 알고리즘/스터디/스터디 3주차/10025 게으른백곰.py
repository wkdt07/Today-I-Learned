
# N, K = map(int,input().split()) # N:얼음이 있는 지점의 개수 K: 팔의 길이
# ice = [0 for _ in range(1000002)]
# lst = []

N,K = map(int,input().split())
ice = [0 for _ in range(1000002)]
max_idx = 0
for _ in range(N):
    g,idx = map(int,input().split())
    ice[idx] = g
    max_idx = max(max_idx,idx)

arm = 2*K + 1
sum_v = sum(ice[:arm] )
v = sum_v

      # 일단 초기치는 먼저 더해놓는 형식으로 하면 0부터 하는 것보단 나을거다.
for i in range(arm,max_idx+1):
    v +=  ice[i] - ice[i-arm] # 기존 값에서 시작값 빼고 현재값 더하기
    sum_v = max(v,sum_v)

print(sum_v)
    # max_idx = max(idx,max_idx)
    # min_idx = min(idx,min_idx)

# print(min_idx)

# max_v = 0
# for i in range(min_idx,max_idx+1):
#     if i - K <= 0:
#         s = 0
#     else:
#         s = i - K
#
#     if i + K >= 99999:
#         e = 99999
#     else:
#         e = i + K
#     max_v = max(max_v,sum(ice[s:e+1]))
# print(max_v)
