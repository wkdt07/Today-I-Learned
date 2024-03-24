# 총 3가지 과정으로 이루어진다.

# 마지막 판을 제외한 모든 판을 2번으로 옮긴다. f(n-1)
# 마지막 판을 3으로 보낸다  f(1)
# 2번에 있는 모든 판을 3으로 보낸다 f(n-1)

# 중간지점 : middle, 목적지 : end , 시작점 : start

N = int(input())
cnt = 2**N -1

def hanoi(start,end,n):
    # 종료조건
    if n == 1:
        print(start,end)
        return

    else: # n>=2
        middle = 6-(start+end)
        hanoi(start,middle,n-1) # 위에 있는 판들 전부 middle로
        hanoi(start,end,1) #마지막 판
        hanoi(middle,end,n-1) # middle에 있는 판들 모두 3번으로

print(cnt)
hanoi(1,3,N)
