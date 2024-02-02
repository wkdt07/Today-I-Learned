# 방향배열 문제

#
# T = int(input())
#
# for t in range(1,T+1):
#     N,M = map(int,input().split())
#     arr = [list(map(int,input().split())) for _ in range(N)]
#
#     di = [0,0,-1,1]
#     dj = [1,-1,0,0]
#
#     max_v = 0 # 최대 꽃가루 합계
#     for i in range(N):
#         for j in range(M):
#             cnt = arr[i][j] # 터트린 풍선의 꽃가루 수
#             for k in range(4): #주변 풍선의 인덱스 ni,nj
#                 ni = i +di[k]
#                 nj = j + dj[k]
#                 if 0 <= ni <N and 0 <= nj < M:
#                     cnt += arr[ni][nj]
#
#             # 꽃가루를 최대값과 비교
#             if max_v < cnt:
#                 max_v = cnt
#
#     print(f'#{t} {max_v}')
#

# 만약 특정 값에서만 멈추고 싶으면 브레이크포인트에 condition에 i==8 아니면 max_v ==8 이런 식으로


T = int(input())

for t in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    di = [0,0,1,-1]
    dj = [1,-1,0,0]


    lst = []
    for i in range(N):
        for j in range(M):
            cnt = arr[i][j]
            K = arr[i][j]
            for n in range(4):
                ni = i + di[n]
                nj = j + dj[n]
                if 0<=ni<N and 0<=nj<M:
                    cnt+=arr[ni][nj]
            lst.append(cnt)
    max_v = max(lst)

    print(f'#{t} {max_v}')