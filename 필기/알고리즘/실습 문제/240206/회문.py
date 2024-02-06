T = int(input())
def pali(N,M,arr):
    for i in range(N):
        # 각 행에서 가능한 시작 위치, M길이의 회문을 찾기 위해서 N-M의 위치까지만 고려
        for j in range(N-M+1):
            # 가로회문  ---> 시작 j에서 길이가 M 만큼의 부분 문자열
            h = arr[i][j:j+M]
            #세로회문   ---> k행의 i열 문자열 가져오기
            v = [arr[k][i]for k in range(j,j+M)]

            if h == h[::-1]:
                return h

            if v == v[::-1]:
                return v
    return ''

for t in range(1,T+1):
    N , M = map(int,input().split())

    arr = [list(map(int,input().split())) for _ in range(N)]

    result = pali(N,M,arr)
    string = ''.join(result)

    print(f'#{t} {string}')


# def pali(arr,N,M):
#     n = M//2
#
#
#     for i in range(N):
#         a=arr[i]
#         b = a[::-1]
#         for k in range(N-M+1):
#             if a[k:M+k+1] == b[k:]
#
# #
#     for j in range(N):
#         b = []
#         for i in range(N):
#             b.append(arr[i][j])
#
#         for k in range(N - M+1):
#             if b[k:n + k] == b[n + k: 2*n+k][::-1]:
#                 return b
#             else:
#                 continue
#     return ''

 # for j in range(N):
#         for i in range(N - M + 1):
#             # n = M // 2  # 판독 정중앙
#             if arr[i:i + n+1][j] == arr[i + n+1:i + M][j]:
#                 return arr[i:M+1][j]
#             else:
#                 continue

