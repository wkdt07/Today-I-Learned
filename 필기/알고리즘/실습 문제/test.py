# N, K = map(int, input().split())
# lst = list(int(input()) for _ in range(N))

# s, e = 0, max(lst)

# while s <= e:
#     mid = (s + e) // 2
#     cnt = 0
#     for l in lst:  # 현재 mid 길이로 츄러스를 잘라 만들 수 있는 츄러스의 개수 총합
#         cnt += l // mid

#     if cnt >= K:
#         s = mid+1

#     else:
#         e = mid-1

# print(e)

for i in range(5):
    n = 0b1<<i
    print(bin(n),int(n))