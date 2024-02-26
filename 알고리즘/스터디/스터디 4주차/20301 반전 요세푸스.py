# # (-1)**i 사용
# N,K,M = map(int,input().split())
# lst = [i for i in range(1,N+1)]
# vst = [0] * (N+1)
# result = []
# cnt = 0
# i = K - 1
# while cnt != N:
#     if cnt % M==0 and cnt !=0:
#         lst.reverse()
#     if not vst[i]:
#         print(lst[i])
#         vst[i] = 1
#         cnt += 1
#         # 인덱스 변경해야함
#         i += K
#         if K > N:
#             K -= N
#
#     else:
#         i += 1
from collections import deque as dq

N,K,M = map(int,input().split())

lst = []

q = dq(range(1,N+1))

i = 1
cnt = 0
while q:
    if (cnt//M)%2 == 0:
        q.rotate(-1*i*(K-1))
        t = q.popleft()
        lst.append(t)
        cnt += 1
    else:
        q.rotate(K)
        t = q.popleft()
        lst.append(t)
        cnt += 1

for i in lst:
    print(i)
# from collections import deque as dq
#
# N,K,M = map(int,input().split())
#
# lst = []
#
# q = dq(range(1,N+1))
#
# i = 1
# cnt = 0
# while q:
#     q.rotate(-1*i*(K-1))
#     t = q.popleft()
#     lst.append(t)
#     cnt += 1
#     if cnt == M:
#         q.reverse()
#         cnt -= M
#
# for i in range(N):
#     print(lst[i])
