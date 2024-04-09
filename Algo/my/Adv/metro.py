# vst와 choice
# choice는 실제로 뽑힌 수, 이건 4개만 뽑힌다
# vst는 양 옆 포함. 어차피 하나가 뽑히면 양 옆은 절대 못 뽑는다
# 교차는 신경쓸거 없음. 4개를 뽑은 다음에 연결하면 됨.
# 이 때 4개를 교차 없이 연결하는 경우는 2개. 이걸 하드코딩


T = int(input())

def bt():
    global max_v

    # 4개를 다 뽑았을 떄
    if len(choice) == 4:
        choice.sort()
        f1= (nums[choice[0]]+nums[choice[1]])**2 + (nums[choice[2]]+nums[choice[3]])**2
        f2 = (nums[choice[0]]+nums[choice[3]])**2 + (nums[choice[1]]+nums[choice[2]])**2
        max_v = max(f1,f2,max_v)
        return

    # 4개 뽑기 전 백트래킹

    for i in range(N):
        if i not in vst:
            choice.append(i)
            vst.append(i)
            vst.append((i-1)%N) # 왼쪽에 있는 애
            vst.append((i+1)%N)

            bt()

            # 백트래킹 하면서 흔적 지우기
            choice.remove(i)
            vst.remove(i)
            vst.remove((i-1)%N)
            vst.remove((i+1)%N)




for tc in range(1,T+1):
    N = int(input())
    nums = list(map(int,input().split()))

    vst= []
    choice = []
    max_v = -float('inf')
    bt()

    print(f'#{tc} {max_v}')

