import sys

N,M = map(int,sys.stdin.readline().rstrip().split())

pok = {}
for i in range(1,N+1):
    name = sys.stdin.readline().rstrip()
    pok[i] = name
    pok[name] = i

for _ in range(M):
    q = sys.stdin.readline().rstrip()
    if q.isdigit():
        r = int(q)
        print(pok[r])
    else:
        print(pok[q])



'''
시간초과 -> sys 안 쓴거
N,M = map(int,input().split())
pok = {}
for i in range(1,N+1):
    name = input()
    pok[i] = name
    pok[name] = i

for _ in range(M):
    q = input()
    if q.isdigit():
        r = int(q)
        print(pok[r])
    else:
        print(pok[q])
'''
'''
시간초과
pok = [0] + [input() for _ in range(N)]

num_lst = [str(i) for i in range(1,N+1)]

for _ in range(M):
    q = input()
    if q in num_lst:
        q = int(q)
        print(pok[q])
    else:
        print(pok.index(q))
'''

'''
시간초과
pok = {} # 1: 포켓몬
for i in range(N):
    pok.setdefault(i+1,input())

pok2 = {} # 포켓몬:1
for key in pok:
    pok2[pok[key]] = key

num_lst = [str(i) for i in range(1,N+1)]

for _ in range(M):
    q = input()
    if q in num_lst:
        q = int(q)
        print(pok[q])
    else:
        print(pok2[q])
'''