def func():
    global result
    while True:
        for i in range(1, N + 1):
            if need[i] == [0]: # 선행 작업이 없으면
                need[i].clear() # 그냥 지운다, 이제 본격적으로 일 착수
                for j in range(1, N + 1): # 다른 일 확인
                    if i in need[j]:  # 선행작업으로 포함되면
                        need[j].remove(i) # 선행작업 완료 처리 하고
                        time[j] = max(time[j], time_origin[j] + time[i]) # 해당 일을 하면서 걸린 일은
                        # j의 선행 작업이 1번과 2번이고, 1번을 먼저 했을 경우
                        # 걸리는 시간은 1번+j와 2번+j 중 가장 큰 거임
                break
        else:  # 끝까지 돌았는데 처리할 수 있는 업무가 없음
            for z in range(1, N + 1):
                if need[z]: # 선행작업 다 돌았는데도 일이 남아있으면
                    result = -1
                    return
            result = min(result, max(time))
            return


from copy import deepcopy

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    time = [0] * (N + 1)
    time_origin = [0] * (N + 1) # 각 업무당 할당된 시간
    need = [0] * (N + 1)
    need_origin = [0] * (N + 1)
    for n in range(1, N + 1):
        t, M, *needs = map(int, input().split())
        if 0 not in needs:
            needs.append(0)
        time[n] = t
        time_origin[n] = t
        need[n] = list(needs) # 선행 작업
        need_origin[n] = list(needs)

    result = float("inf")

    # 업무 도와주기
    for n in range(1, N + 1):
        shrink = time[n] // 2 # 줄어든 시간
        remain = time[n] % 2 # 나머지
        time[n] = time_origin[n] = shrink # 일단 줄여보고
        func()
        time_origin[n] = shrink * 2 + remain  # 백트래킹
        time = time_origin.copy() # 되돌린거 원상 복구 -> 이럴거면 그냥 time만 건들면 되는거 아닌가?
        need = deepcopy(need_origin)
        # 결국 다 해보기

    print(f'#{tc} {result}')