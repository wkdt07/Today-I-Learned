# BFS?
from collections import deque
q = deque()
N = int(input())
# visited = [0] * (10**6 +1)
visited = [0] * (N+1)
q.append((0,N))
while q:
    level,ans = q.popleft()
    if ans == 1:
        print(level)
        break
    if ans % 3 == 0:
        ans1 = ans//3
        if ans1 >= 1:
            if visited[ans1] ==0:
                visited[ans1] =1
                q.append((level+1,ans1))

    if ans % 2 == 0:
        ans2 = ans//2
        if ans2 >= 1:
            if visited[ans2]==0:
                visited[ans2]=1
                q.append((level+1,ans2))


    ans3 = ans-1
    if ans3>= 1:
        if visited[ans3] ==0:
            visited[ans3] =1
            q.append((level+1,ans3))




