from heapq import heappush, heappop
import sys
q = []
N = int(sys.stdin.readline())
for _ in range(N):
    k = int(sys.stdin.readline())
    if k: # k가 0이 아니면
        heappush(q,k)
    else:
        if q:
            print(heappop(q))
        else:
            print('0')