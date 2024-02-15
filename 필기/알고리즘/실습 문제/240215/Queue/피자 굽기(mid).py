from collections import deque

T = int(input())

for t in range(1,T+1):
    N,M = map(int,input().split())
    c_lst = list(map(int,input().split()))
    c_q = deque()
    last = N
    for i in range(N):
        c_q.append([i,c_lst[i]]) # 인덱스와 값 동시에 처리

    while c_q:
        k = c_q.popleft()
        k[1] //= 2
        if k[1] != 0:
            c_q.append(k)

        else:
            if last == M:
                continue
            else:
                c_q.append([last, c_lst[last] // 2])
                last += 1

    print(f'#{t} {k[0]+1}')