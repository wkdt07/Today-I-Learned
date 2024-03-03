# T = int(input())
# todo
# 백트래킹이 아니라 bfs로 que에 이전 노드 넣어서
# def mt(s,cnt=0):
#     global min_v
#     i,j = s
#
#     if cnt > min_v:
#         return
#
#     if s == e:
#         min_v = min(cnt,min_v)
#         return
#
#     if s in turner_in: # todo 터널 지나가는 조건 확인
#         ni,nj = turner[s][:2]
#         vst.append((ni,nj))
#         mt((ni,nj),cnt+turner[s][2])
#         vst.remove((ni,nj))
#
#     for d in dir:
#         ni,nj = i+d[0],j+d[1]
#         if 0<=ni<N and 0<=nj<N:
#             if (ni,nj) not in vst:
#                 vst.append((ni,nj))
#                 if mnt[ni][nj] > mnt[i][j]:
#                     tmp = 2*(mnt[ni][nj]-mnt[i][j])
#                 elif mnt[ni][nj] == mnt[i][j]:
#                     tmp = 1
#                 else :
#                     tmp = 0
#                 mt((ni,nj),cnt+tmp)
#                 vst.remove((ni,nj))

from collections import deque as dq

T = int(input())
def bfs(s,e):
    global min_v
    i,j = s
    # vst = []
    q = dq([(i,j)])
    # print(q)
    while q:
        now = q.popleft()
        # print(now)
        i,j = now
        cnt = vst[i][j]

        if now == e:
            min_v = min(cnt,min_v)
            continue

        if vst[i][j] >= min_v:
            continue

        for d in dir:
            ni,nj = i+d[0],j+d[1]
            if 0<=ni<N and 0<= nj <N:

                # 필요 연료 확인
                if mnt[ni][nj] > mnt[i][j]:
                    tmp = 2 * (mnt[ni][nj] - mnt[i][j])

                elif mnt[ni][nj] == mnt[i][j]:
                    tmp = 1

                elif mnt[ni][nj]<mnt[i][j]:
                    tmp = 0

                # vst로 가지치기
                if vst[ni][nj]:#값이 있을 떄

                    if cnt+tmp >= vst[ni][nj]: #만약 현재 값이 기존 값보다 크면
                        continue
                    else: # 더 적은 연료를 찾은 경로를 찾으면
                        vst[ni][nj] = cnt+tmp
                        next = (ni,nj)
                        q.append(next)
                else: # 들른 적 없을 떄
                    vst[ni][nj] = cnt + tmp
                    next = (ni, nj)
                    q.append(next)


        for num in tunnel.keys():
            if (i, j) == tunnel[num][0:2]:
                out_i, out_j = tunnel[num][2:4]
                fuel = tunnel[num][4]

                if vst[out_i][out_j]:
                    if vst[out_i][out_j] > fuel+cnt:
                        vst[out_i][out_j] = fuel+cnt
                        q.append((out_i,out_j))
                    else:
                        continue
                else: # 도달한 적 없으면
                    vst[out_i][out_j] = fuel + cnt
                    q.append((out_i,out_j))
                    continue

                # continue
            elif (i,j) == tunnel[num][2:4]:
                out_i, out_j = tunnel[num][0:2]
                fuel = tunnel[num][4]
                if vst[out_i][out_j]:
                    if vst[out_i][out_j] > fuel + cnt:
                        vst[out_i][out_j] = fuel + cnt
                        q.append((out_i, out_j))
                    else:
                        continue
                else:
                    vst[out_i][out_j] = fuel + cnt
                    q.append((out_i, out_j))

                continue
    # print(vst)



for tc in range(1,T+1):
    N,M = map(int,input().split())
    mnt = [list(map(int,input().split())) for _ in range(N)]
    tunnel = {}


    for num in range(M):
        ai,aj,bi,bj,fuel = map(int,input().split())
        ai -= 1
        aj -= 1
        bi -= 1
        bj -= 1

        tunnel[num] = ai,aj,bi,bj,fuel

# dir을 뒤로도 갈 수 있나?


    dir = [(1,0),(0,1),(-1,0),(0,-1)]

    min_v = float('inf')
    s = (0,0)
    e = (N-1,N-1)
    vst = [[0]*N for _ in range(N)]
    vst[0][0] = 1
    bfs(s,e)

    print(f'#{tc} {min_v-1}')