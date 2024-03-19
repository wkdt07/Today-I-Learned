

T = int(input())

for t in range(1,T+1):
    lst = list(map(int,input().split()))
    N = lst[0] +1
    bats = [0] + lst[1:] + [0] #마지막 정류장엔
    now = 1
    temp = bats[now]
    min_v = float('inf')
    flag = False

    def eat(now,temp = bats[now],cnt = 0):
        global min_v
        if cnt >= min_v:  # 가지치기
            return
        # if temp == 0:
        #     eat(now,bats[now],cnt+1)
        #     return

        for i in range(1,temp+1):
            temp2 = bats[now+i]
            if temp2 >= N-(now+i+1):# 탈출할 수 있으면
                min_v = min(min_v,cnt+1)
                break
            else: # 탈출할 수 없으면
                # eat(now + i, temp - i, cnt)
                eat(now+i,temp2,cnt+1) # 먹고 계속 ㄱ
                # 일단 다 맥이고 생각각
        return

    eat(now)
    print(f'#{t} {min_v}')

