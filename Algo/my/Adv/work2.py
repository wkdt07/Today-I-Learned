# 코코가 무슨 일을 줄여줘야 하는진 완탐으로 처리한다
# 결국 중요한건 일을 처리하는 함수를 만들어주는것


T = int(input())

def work():
    global result
    while True:
        for i in range(1,N+1):
            if needs[i] == [0]: # 사전 작업이 없다면 +  아직 이 일을 안 했다면
                needs[i].clear() # 그냥 0 지우기, 이게 해당 작업을 처리했다는 증거가 됨
                for j in range(1,N+1):
                    if i in needs[j]:
                        needs[j].remove(i)
                        times[j] = max(times[j], times[i] + times_ori[j]) # 현재까지 걸린 시간 or 사전작업까지 마친 시간

                # 사전 작업이 아닌 일을 만났을 때, 아직 얘는 처리해줄 타이밍이 아님.
                # print(needs)
                break # 사전 작업 다 처리해줬으면 다시 처음부터, 이번에 해준 일 때문에 사전작업이 끝난 일들도 있을 테니깐

        else: #
            for k in range(1,N+1):
                if needs[k] != []:
                    result = -1
                    return

            result = min(result,max(times))
            return

from copy import deepcopy as dc

for tc in range(1,T+1):
    N = int(input())
    needs_ori = [0]
    times_ori = [0]

    for _ in range(N):
        time,M, *need = map(int,input().split())
        need = list(need)
        # print(need)
        if 0 not in need: # 0은 일종의 확인 절차임. 일을 했다는
            need.append(0)

        times_ori.append(time)
        needs_ori.append(need)



    result = float('inf')
    # print(needs)
    for coco in range(1,N+1):
        # sol = times_ori[coco]//2
        div = times_ori[coco]%2
        needs = dc(needs_ori)
        times_ori[coco] = times_ori[coco]//2
        times = dc(times_ori)
    #     print(times)
    #     print(times_ori)
        work()

        times_ori[coco] = times_ori[coco]*2 + div # 이렇게 안 해주면 16줄에서 times에 갱신해줄 때 times_ori[coco]는 줄어들지 않은 채로 들어가버린다.


    print(f'#{tc} {result}')
