#연산1 -> +1 , 연산2 -> *2
#A를 K로 만들어야 함
# 최소 연산 횟수 구하기

from collections import deque


A,K = map(int,input().split()) #A는 시작, K는 목적

visited = [0] * (1000001)


def bfs(s,e):
    q = deque()
    q.append((0,s))
    visited[s] = 1
    while q:
        level,ans = q.popleft()
        if ans == e:
            return level
        ans1 = ans*2
        if ans1 <= e:
            if visited[ans1] == 0:
                visited[ans1] = 1
                q.append((level+1,ans1))

        ans2 = ans+1
        if ans2 <= e:
            if visited[ans2] == 0:
                visited[ans2] = 1
                q.append((level+1,ans2))



print(bfs(A,K))






'''
    while q:
        t = q.popleft()
        if t == e:
            print(cnt)
            break

        else:
            a1 = t*2
            a2 = t+1
            if visited[a1]==0:
                cnt += 1
                q.append(a1)
                visited[a1] = 1
            if visited[a2] == 0:
                cnt += 1
                q.append(a2)
                visited[a2] == 1

bfs(A,K)
'''