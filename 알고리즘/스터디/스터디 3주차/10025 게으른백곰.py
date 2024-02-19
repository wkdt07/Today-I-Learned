N,K = map(int,input().split())
ice = [0 for _ in range(1000002)]
# max_idx = 0
# min_idx = float('inf')
for _ in range(N):
    g,idx = map(int,input().split())
    ice[idx] = g

result = 0
arm = 2*K + 1

if arm > 1000002:
    result = sum(ice)
else:
    for i in range(0,1000002-arm):
        v = sum(ice[i:i+arm+1])
        result =  max(result,v)

print(result)
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
