from collections import deque

T = int(input())

for t in range(1,T+1):
    N,M = map(int,input().split())
    lst = list(map(int,input().split()))
    lst = deque(lst)
    for _ in range(M):
        lst.append(lst.popleft())

    print(f'#{t} {lst[0]}')