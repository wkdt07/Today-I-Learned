def func():
    global result
    while True:
        for i in range(1, N + 1):
            if need[i] == [0]:
                need[i].clear()
                for j in range(1, N + 1):
                    if i in need[j]:
                        need[j].remove(i)
                        time[j] = max(time[j], time_origin[j] + time[i])
                break
        else:  # 끝까지 돌았는데 처리할 수 있는 업무가 없음
            for z in range(1, N + 1):
                if need[z] != []:
                    result = -1
                    return
            result = min(result, max(time))
            return


from copy import deepcopy

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    time = [0] * (N + 1)
    time_origin = [0] * (N + 1)
    need = [0] * (N + 1)
    need_origin = [0] * (N + 1)
    for n in range(1, N + 1):
        t, M, *needs = map(int, input().split())
        if 0 not in needs:
            needs.append(0)
        time[n] = t
        time_origin[n] = t
        need[n] = list(needs)
        need_origin[n] = list(needs)

    result = float("inf")

    # 업무 도와주기
    for n in range(1, N + 1):
        shrink = time[n] // 2
        remain = time[n] % 2
        time[n] = time_origin[n] = shrink
        func()
        time_origin[n] = shrink * 2 + remain
        time = time_origin.copy()
        need = deepcopy(need_origin)

    print(f'#{tc} {result}')