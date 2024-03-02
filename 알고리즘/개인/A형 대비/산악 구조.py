T = int(input())
# todo
# 백트래킹이 아니라 bfs로 que에 이전 노드 넣어서
def mt(s,cnt=0):
    global min_v
    i,j = s

    if cnt > min_v:
        return

    if s == e:
        min_v = min(cnt,min_v)
        return

    if s in turner_in: # todo 터널 지나가는 조건 확인
        ni,nj = turner[s][:2]
        vst.append((ni,nj))
        mt((ni,nj),cnt+turner[s][2])
        vst.remove((ni,nj))

    for d in dir:
        ni,nj = i+d[0],j+d[1]
        if 0<=ni<N and 0<=nj<N:
            if (ni,nj) not in vst:
                vst.append((ni,nj))
                if mnt[ni][nj] > mnt[i][j]:
                    tmp = 2*(mnt[ni][nj]-mnt[i][j])
                elif mnt[ni][nj] == mnt[i][j]:
                    tmp = 1
                else :
                    tmp = 0
                mt((ni,nj),cnt+tmp)
                vst.remove((ni,nj))

for tc in range(1,T+1):
    N,M = map(int,input().split())
    mnt = [list(map(int,input().split())) for _ in range(N)]
    turner = {}
    for _ in range(M):
        ai,aj,bi,bj,fuel = map(int,input().split())
        ai -= 1
        aj -= 1
        bi -= 1
        bj -= 1

        turner[(ai,aj)] = (bi,bj,fuel)
        turner[(bi,bj)] = (ai,aj,fuel)
# dir을 뒤로도 갈 수 있나?

    turner_in = list(turner.keys())
    # print(turner)
    # print(turner_in)
    cnt_lst = []
    dir = [(1,0),(0,1)]

    min_v = float('inf')
    s = (0,0)
    e = (N-1,N-1)

    vst = [s]

    mt(s)

    print(f'#{tc} {min_v}')