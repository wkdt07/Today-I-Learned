from heapq import heappop, heappush
n = int(input())
lst = []
for _ in range(n):
    inv = list(map(int,input().split()))
    if inv[0] == 0:
        if lst:
            print(-heappop(lst))
        else:
            print(-1)

    else:
        for i in range(1,len(inv)):
            heappush(lst,-inv[i])



'''
n = int(input())
lst = []
for _ in range(n):
    inv = input()
    if inv == '0': #inv = 0
        if lst:
            print(lst.pop())
        else:
            print(-1)

    else:
        inv = list(map(int,inv.split()))
        lst.extend(inv[1:])
        lst.sort()
'''

