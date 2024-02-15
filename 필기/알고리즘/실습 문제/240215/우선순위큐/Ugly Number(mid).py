from heapq import heappop as hp
from heapq import heappush as ps
'''
N = int(input())

t = list(map(int,input().split()))
# a = [[i,v] for i,v in enumerate(lst)]

h = [1]

ugly = [1]
while len(ugly) <= max(t):
    cur = hp(h)
    a = cur * 2
    b = cur * 3
    c = cur * 5
    if a not in ugly:
        ps(ugly,a)
    if b not in ugly:
        ps(ugly,b)
    if c not in ugly:
        ps(ugly,c)

    ps(h,a)
    ps(h,b)
    ps(h,c)

ugly.sort()

for i in t:
    print(ugly[i-1],end=' ')

'''

N = int(input())

K = list(map(int,input().split()))

ugly = []
heap = [1]  #최초 힙 1
ps(heap,2)
ps(heap,3)
ps(heap,5)

while len(ugly) < max(K):
    n = hp(heap) # 힙에서 최소값 가져오기

    if n not in ugly: # 중복 피하기
        ugly.append(n)
        ps(heap,n*2)
        ps(heap,n*3)
        ps(heap,n*5)

for i in K:
    print(ugly[i-1],end = ' ')






