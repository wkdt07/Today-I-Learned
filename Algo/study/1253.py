# now 아래쪽으로 두 수 골라서 합 찾기
# 투 포인터 알고리즘
# 정렬 후, 만약 start+end가 now보다 작으면 start 올리기, 아니면 end 낮추기

# 추가) '정수' 이기 때문에 -3 0 3 과 같이 양 옆을 더했을 때 가운데가 되는 좆같은 케이스가 존재할 수 있음
import sys
input = sys.stdin.readline

N = int(input())

lst = list(map(int,input().split()))
lst.sort()
def two_point():
    global ans
    if N <= 2:
        ans = 0
        return ans
    # if N == 3:
    #     if lst[0] + lst[1] == lst[2]:
    #         ans = 1
    #         return ans
    now = 0
    ans = 0
    start = 0
    end = N-1 # 마지막 거
    while now < N: # 마지막 자리에 닿으면 끝
        # if lst[start] + lst[start+1] > lst[now]: # 가장 작은 값이 now보다 크면 의미가 없음
        #     now += 1
        #     start = 0
        #     end = now - 1
        #     continue
        # if lst[end] + lst[end-1] < lst[now]: # 가장 큰 값이 now보다 작으면 의미가 없음
        #     now += 1
        #     start = 0
        #     end = now - 1
        #     continue
        if start == end:
            now += 1
            start = 0
            end = N-1
            continue
        now_num = lst[now]
        if lst[start]+lst[end] == now_num:
            if start != now and end != now:
                ans += 1
                now += 1
                start = 0
                end = N-1
                # 만약 합이 같고, 그 합을 이루는 요소들이 now가 아니라면 => 정답 += 1하고 리셋
            elif start == now:
                start = now+1
                continue
            else:
                end = now - 1
                continue

            # ans += 1
            # now += 1
            # start = 0
            # end = now - 1
            # continue
        elif lst[start]+lst[end] < now_num: # 두 합이 현재보다 작으면 -> start를 늘려야 한다.
            start += 1
            continue
        else: # 두 합이 현재보다 크면 -> end를 줄여야 한다.
            end -= 1
            continue

    return ans

ans = two_point()

print(ans)