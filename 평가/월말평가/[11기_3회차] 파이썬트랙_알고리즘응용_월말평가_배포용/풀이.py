# 1

'''
T = int(input())
for t in range(1,T+1):
    N,color = input().split()
    N = int(N)
    if N == 6:
        print(f'{t} {int(color,16):024b}')
    else:
        print(f'#{t} {int(color,2):06x}')
'''

# 2

'''
def f(i,N,c,s):
    global max_c
    global min_v
    
    if i == N:
        if s<= V: # 예산을 초과하지 않으면,
            if max_c>c:
                max_c = c
                min_v = s
            # 최대개수와 같ㄹ으면 더 싸게 만들 수 있는가
            elif max_c == c and min_v>s:
                min_v = s
        elif s>V: # 예산을 초과할 경우
            return
        elif c + (N-i)<max_c # 남은 다리를 다 건설해도 기존 최대 개수에 못 미치면
            return
        else:
            f(i+1,N,c+1,s+cost[i]) # 다리르 건설하는 경우
            f(i+1,N,c+1,s)
'''
