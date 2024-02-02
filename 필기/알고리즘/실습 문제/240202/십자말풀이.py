## 작년 im 기출

# 연속한 1의 갯수를 세기

# N = 7
# K = 3
# arr = [0,1,0,1,1,1,0]
# cnt = 0
# ans = 0
#
# for i in range(N):
#     # if arr[i]:
#     #     cnt+=1
#     # elif arr[i]==0 or i == N-1: # 이러면 마지막 인덱스에 들어간 값이 1일 때 적용이 안 되고 위에서 끊기
#     if arr[i] == 0:
#         if cnt == K:
#             ans += 1
#         cnt = 0
#     else: # arr[i] == 1
#         cnt += 1
#         if (i == N - 1 and cnt == K):
#             ans += 1
#=======================================================

# T = int(input())
# for t in range(1,T+1):
#     N,K = map(int,input().split())
#     arr = [list(map(int,input().split())) + [0] for _ in range(N)]+[[0]*(N+1)]  # 우측이랑 하단에 0 추가
#     N += 1 #0인 행 추가했으니깐
#
#     # 가로, 세로로 연속한 1의 개수가 K인 경우의 수
#     ans = 0
#     for i in range(N):
#         cnt = 0 #i 행에서 연속한 1의 갯수
#         for j in range(N):
#             if arr [i][j]:
#                 cnt+=1
#             else: #arr [i][j] == 0 이면
#                 if cnt == K:
#                     ans+=1
#                 cnt = 0
#
#     for j in range(N):# 열 기준
#         cnt = 0  # j 열에서 연속한 1의 갯수
#         for i in range(N):
#             if arr[i][j]:
#                 cnt += 1
#             else:  # arr [i][j] == 0 이면
#                 if cnt == K:
#                     ans += 1
#                 cnt = 0
#
#     print(f'{t} {ans}')

# =====================================================================

T = int(input())

for t in range(1,T+1):
    N,K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = 0

    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
                if (j == N-1 and arr[i][j] == 1) and cnt == K:
                    ans+=1

            if arr[i][j] == 0 :
                if cnt == K:
                    ans += 1
                cnt = 0

    for j in range(N):
        cnt = 0
        for i in range(N):
            if arr[i][j] == 1:
                cnt += 1
                if (i == N-1 and arr[i][j] == 1) and cnt == K:
                    ans += 1

            if arr[i][j] == 0:
                if cnt == K:
                    ans += 1
                cnt = 0

    print(f'#{t} {ans}')