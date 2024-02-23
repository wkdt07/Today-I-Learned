# 자신의 팀원? X-1번 패스하고 만난 x번째 학생
# 패스할 때마다 x를 1씩 줄이고 x가 1이면 선택한다.
from collections import deque
q = deque()
N = int(input())
for _ in range(N):
    per,x = map(str,input().split())
    x = int(x)
    lst = [per,x]
    q.append(lst)

# q.rotate(-1)
while len(q) != 1:
    t = q.popleft()
    per = t[0]
    x = t[1]
    q.rotate(-(x-1))
    q.popleft()
print(q[0][0])