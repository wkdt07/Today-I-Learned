# BFS로 최단 레벨 구하기
# 우선순위 큐 사용

from heapq import heappush as push
from heapq import heappop

s,e = map(int,input().split()) # N:현재위치, K:목표지점


vst = [0] * 100001

def bfs(s,e):
    level = 0 # 방문 표시를 위해 혹시 몰라서 더해둠
    q = [[level,s]]

    vst[s] = 0
    while q:
        t = heappop(q)
        now = t[1]
        level = t[0]
        # print(t)
        vst[now] = 1
        if now == e:
            print(level)
            return

        if now*2 in range(100001) and not vst[now*2]: # 이게 level을 최대한 줄일 수 있어서 q에 우선 넣어야함
            # vst[now*2] = 1
            push(q,[level,now*2])
            # print(q)

        if now + 1 in range(100001) and not vst[now+1]:
            # vst[now+1] = 1
            push(q,[level+1,now+1])

        if now-1 in range(100001) and not vst[now-1]:
            # vst[now-1] = 1
            push(q,[level+1,now-1])

bfs(s,e)
# print(bfs(s,e))


# from heapq import heappop, heappush
# n, k = map(int, input().split())  # 나, 동생
# visit = [0] * 100001 # 방문 기록
# visit[n] = 0
# q = [(0, n)]
# # tip : 우선순위 큐에 iterable 을 넣으면 가장 앞의 value를 기준으로 우선순위가 정렬됨
#
# while q:
#     time, position = heappop(q)
#     if position == k:
#         print(time)
#         break
# 		# 범위 안에 있고, 방문 안했으면 큐에 시간과 같이 넣고 방문처리
#     for i in [2 * position, position + 1, position - 1]:
#         if i in range(100001):
#             if i and i == 2 * position and not visit[i]:
#                 heappush(q, (time, i))
#                 visit[position] = 1
#             else:
#                 if not visit[i]:
#                     heappush(q, (time + 1, i))
#                     visit[i] = 1
