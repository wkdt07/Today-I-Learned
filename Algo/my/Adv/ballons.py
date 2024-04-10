# 만약 무작위로 모두 돌리고 싶으면?
# DFS

T = int(input())

def shot(ans = 0,level = 0):
    global max_v

    if level == N-1:
        idx = vst.index(0)
        ans += ballons[idx]
        max_v = max(ans,max_v)
        return
    # now = i
    for now in range(N):
        if not vst[now]:
            left = now - 1
            right = now + 1
            while left >= 0:
                if vst[left]:
                    left -= 1

                else:
                    break

            while right <= N-1:
                if vst[right]:
                    right += 1
                else:
                    break
            if left == -1:
                # ans += tmp[left]
                tmp_v = ballons[right]
            elif right == N:
                # # ans += tmp[right]
                # # vst.append(now)
                # shot(ans + tmp[right])
                # vst.remove(now)
                tmp_v = ballons[left]
            else:
                # ans += tmp[left] * tmp[right]
                # vst.append(now)
                # shot(ans + tmp[left]*tmp[right])
                # vst.remove(now)
                tmp_v = ballons[right]*ballons[left]
            vst[now] = 1
            shot(ans + tmp_v,level+1)
            vst[now] = 0

from copy import deepcopy as dc
for tc in range(1,T+1):
    N = int(input())
    ballons = list(map(int,input().split()))
    max_v = -float('inf')
    # tmp = dc(ballons)
    vst = [0]*N
    shot()
    print(f'#{tc} {max_v}')