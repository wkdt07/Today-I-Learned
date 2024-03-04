# N개의 퀸을 공격할 수 없게 놓기
# 상하좌우 대각선 모든 방향에 끝까지 움직일 수 있음

dir = [(-1,1),(-1,-1)]
N = int(input())
vst = [[0]*N for _ in range(N)]
cnt = 0
# def dfs(j,i=0):
#     global cnt
#
#     if i == N-1:
#         cnt += 1
#         return
#
#     for d in dir: # 우선 방향에 퀸이 존재하는지 확인
#         p = 1
#         while True:
#             ni,nj = i+p*d[0],j+p*d[1]
#             if not(0<=ni<N and 0<=nj<N):
#                 break
#             if vst[ni][nj] == 1:
#                 return
#             p+=1
#
#         vst[i][j] = 1
#         dfs(j,i+1)
#         vst[i][j] = 0
# for j in range(N):
#     dfs(j)

print(cnt)