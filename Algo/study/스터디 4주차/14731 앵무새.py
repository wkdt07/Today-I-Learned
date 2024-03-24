
### 그냥 popleft만 써서 서로 비교하면 더 간단할거같은데

from collections import deque

N = int(input())
words = []
cnt = 0
for n in range(N):
    lst = deque(input().split())
    words.append(lst)
    cnt += len(lst)
L = deque(input().split())
L_len = len(L)


# print(words)
# print(L)
# system = [[(-1,-1)] for _ in range(N)] # 긱 문장의 구성요소 판단 여부를 넣을 스택

# print(system)

system = [[-1] for _ in range(N)]

def check():
    if cnt != len(L):
        print('Impossible')
        return
    while L:
        t = L.popleft()
        for i in range(N):
            k = True
            if t in words[i]: # a,b,c 어느 리스트에 속해있는지 어떻게 판단하게?
                idx = words[i].index(t)
                if system[i]: # 이미 선객이 존재할 때
                     # 이전 인덱스
                    idx_old = system[i].pop()
                    # idx_old = a[0]
                    if idx<idx_old:
                        print('Impossible')
                        return
                    else:
                        # system[i].append([idx,t])
                        system[i].append(idx)
                        words[i].remove(t)
                        k = False
                        break
                break # i가 바뀌는거.
        # 다 돌았는데 없다면?
        if k: #  다 돌았는데도 k가 바뀌지 않고 True라면
            print('Impossible')
            return
    # finish_v = 0
    # for i in range(N):
    #     if len(words[i]):
    #         finish_v = 1
    #         break
    #     else:
    #         continue


    print('Possible')
    return



# print(bool(lst))
check()