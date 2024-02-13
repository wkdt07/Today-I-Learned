n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]
dir = [(-1,0),(1,0),(0,-1),(0,1)]
used = [[0 for _ in range(n)] for _ in range(n)] # 각 칸의 방문 여부 체크

def red(dy,dx):
   if dy == n - 1 and dx == n-1: # 목적지 도착 시
      return 1

   for d in dir:
      ny,nx = dy + d[0], dx + d[1]

      if not(0<=ny<n and 0<=nx<n): # 1.맵의 범위 벗어났을 때
         continue

      if arr[ny][nx] == 1: # 2.장애물 만났을 때
         continue

      if used[ny][nx] == 1: # 3. 이미 방문한칸일 때 다른 방향 탐색 -> 가지치기
         continue

      used[ny][nx] = 1 # 현재 칸 방문 표시

      ret = red(ny,nx) #다음 칸 할당

      if ret == 1: #결국엔 목적지 도착해서 1을 return 받았을 때
         return 1 # 부모 노드에도 쭉 1을 올려라

      used[ny][nx] = 0 #백트래킹, 가지치기 : 이 경로가 해결책이 아니라면, 방문표시 되돌리기... 이건 왜???

   return 0 # 만약 for문, 재귀까지 다 돌았는데도 목적지에 도착하지 않았다면 0을 return 해라

used[0][0] = 1 # 시작점 방문

print(red(0,0))


'''shb

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
e = (n-1,n-1)
s = 0,0
visited = [[0 for _ in range(n)] for _ in range(n)]
dir = [(0,1),(0,-1),(1,0),(-1,0)]

def bt(s,e):
    i = s[0]
    j = s[1]
    ei, ej = e
    visited[i][j] = 1

    for k in dir:
        ni = i + k[0]
        nj = j + k[1]
        if not(0<=ni<n and 0<=nj<n):
            continue

        elif arr[ni][nj] == 1:
            continue

        elif visited[ni][nj] == 1:
            continue

        else:
            s = ni,nj
            bt(s,e)


    if visited[ei][ej] == 1:
        return 1

    else:
        return 0





print(bt(s,e))


# def bt(s,e):
#     i = s[0]
#     j = s[1]
#     if s == e:
#         return 1
#     for k in dir:
#         ni = i + k[0]
#         nj = j + k[1]
#
#         while 0 <= ni < n and 0<= nj < n:
#             if arr[ni][nj] == 1:
#                 break
#
#             else:
#                 s = ni,nj
#                 if s == e:
#                     return 1
#                 bt(s,e)
#     return 0
'''