# BFS?
from collections import deque
q = deque()
N = int(input())

q.append(N)
cnt = 0
while q:
    cnt += 1
    t = q.popleft()
    if t == 1:
        print(cnt)
        break
    if t % 3 == 0:
        q.append(t%3)

    if t % 2 == 0:
        q.append(t%2)

    q.append(t-1)

