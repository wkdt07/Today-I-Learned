import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    N,S = input().split()
    n = int(N)
    ans = ''

    for s in S:
        ans += s*n
    print(ans)
