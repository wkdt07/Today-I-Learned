T = int(input())

# def bt(sum_v = 0):
#     global min_v
#     if sum_v >= target:
#         min_v = min(sum_v-target,min_v)
#         return
#     if not min_v:
#         return
#     for i in range(N):
#         # if h > min_v:
#         #     return
#         if not vst[i] :
#             h = heights[i]
#             vst[i] = 1
#             bt(sum_v+h)
#             vst[i] = 0
''' 제한시간 초과가 많이 날 수 밖에 없다. 노드가 20개면 20!이 경우의수임
이럴거면 차라리 이진트리로 '뽑았냐' '안뽑았냐' 가 더 적절 '''

def bt(cnt=0,sum_v = 0):
    global min_v
    if sum_v >= target:
        min_v = min(sum_v - target,min_v)
    if cnt == N:
        return

    # 뽑
    bt(cnt+1,sum_v+heights[cnt])

    # 안뽑
    bt(cnt+1,sum_v)
for t in range(1,T+1):
    N,target = map(int,input().split())
    heights = list(map(int,input().split()))
    min_v = float('inf')
    vst = [0] * N
    bt()
    print(f'#{t} {min_v}')
