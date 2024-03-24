# T = int(input())
#
# for t in range(T):
#     k = int(input())
#     n = int(input())# k는 층, n은 호수
#     start = [i for i in range(n+1)]
#     for _ in range(k):
#         for j in range(1,n+1):
#             start[j] += start[j-1]
#     print(start[-1])
#
#
def dp():
    apart = [[0 for _ in range(15)] for _ in range(n+1)]
    for i in range(k+1): # 층수
        for j in range(n+1): # 호수
            if i == 0: # 층
                apart[i][j] = j
            else:
                for m in range(j+1):
                    apart[i][j] += apart[i-1][m]
    # l = len(apart)
    print(apart[k][n])
    # for i in range(l):
    #     print(*apart[i])
    # # print(apart)

T = int(input())
for tc in range(1, T+1):
    k = int(input())
    n = int(input())
    dp()