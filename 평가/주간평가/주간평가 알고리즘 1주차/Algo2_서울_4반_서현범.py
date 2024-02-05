T = int(input())

for t in range(1,T+1):
    N , K = map(int,input().split())
    lotus = list(map(int,input().split()))

    def cnt_lts():
        cnt = 0  # 누적합
        k = 0  # 뛴 횟수
        cur = 0  # 현재 위치
        while 0<=cur<N: # 연꽃 범위를 벗어나지 않을 때까지

            if lotus[cur] >= 0: # 만약 현재 위치에 있는 연꽃 값이 +라면


                if k != 0: #현재 위치는 합산 x
                    cnt += lotus[cur]
                    if k > K:
                        return cnt
                cur += lotus[cur]
                k += 1



            elif lotus[cur] < 0 : # 만약 현재 위치에 있는 연꽃이 - 라면
                while lotus[cur] < 0: # 서 있는 곳의 값이 +가 될 때까지
                    if k != 0:  # 현재 위치는 합산 x
                        cnt += lotus[cur]
                    re_cur = lotus[cur] = lotus[cur]# 이후에 한 번에 도약하기 위해 추가될 값
                    cur += lotus[cur]
                    k += 1
                    if k > K :
                        return(cnt)
                    if lotus[cur] >= 0: # 뒤로 갔을 때 값이 + 라면
                        cnt += lotus[cur]
                        cur += lotus[cur]-re_cur # 도약 거리 추가
                        k += 1
                        if k > K:
                            return(cnt)
                        break


                    else: # 뒤로 갔을 때 값이 -라면
                        k += 1
                        cur += lotus[cur]
                        cnt += lotus[cur]
                        if k > K:
                            return(cnt)
                        continue

        return(cnt)

    print(f'{t} {cnt_lts()}')



