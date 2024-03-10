# N개의 퀸을 공격할 수 없게 놓기
# 상하좌우 대각선 모든 방향에 끝까지 움직일 수 있음

# dir = [(-1,1),(-1,-1)]
N = int(input())
vst = [0]*N
vst_cross1 = [0]*(2*N)
vst_cross2 = [0]*(2*N)
cnt = 0
def qn(level = 0):
    global cnt
    if level == N: #
        cnt += 1
        return

    for i in range(N):
        if not (vst[i] or vst_cross1[level+i] or vst_cross2[i-level]):
            vst[i] = 1
            j = i + level
            k = i - level
            vst_cross1[j], vst_cross2[k] = 1,1
            qn(level+1)
            vst[i] = 0
            vst_cross1[j] = 0
            vst_cross2[k] = 0

qn()

print(cnt)

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

# print(cnt)