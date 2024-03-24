# -*- coding:utf-8 -*-

# 내가 만약 첫 번째 스티커를 뜯는다면, 가능한 경우의 수는 2개
# 대각선을 뜯느냐, 해당 렬을 한 번 건너띄고 다음 렬, 다른 행의 스티커를 뜯느냐.
# 이진트리? 아니면 무조건 적용 가능?

#a_0(첫번째 선택을 0행으로 잡냐) a_1(첫번쨰 선택을 1행으로 잡냐) 비교

T = int(input())

for t in range(T):
    N = int(input())

    stickers = [list(map(int, input().split())) for _ in range(2)]

    def take(i):
        j = 0
        temp = 0  # 처음에 뜯는다는 보장이 없다.
        # 현재와 다음 대각선이 다음과 다음의 대각선보다 크면 뜯는다
        # temp = stickers[i][j]
        while j<N:
            if j == N-1: # 만약 뜯은게 N-1이 된다면
                # temp += stickers[i][j]
                return temp
            if j == N-2: # 만약 지금 뜯은게 N-2라면
                temp += stickers[(i+1)%2][j+1]
                return temp
            if stickers[(i+1)%2][j+1]+stickers[i][j+2]> stickers[(i+1)%2][j+2]:
                temp += stickers[(i+1)%2][j+1]+stickers[i][j+2]
                j += 2 # 지금 여기까지 뜯었다
            else: # 같을 땐 어떡하냐?
                temp += stickers[(i+1)%2][j+2]
                j += 2 # 지금 여기까지 뜯었다
                i = (i+1)%2
        return temp

    max_v = max(take(0),take(1))

    print(max_v)