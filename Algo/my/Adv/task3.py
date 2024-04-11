T = int(input())

def task():
    global min_v
    while True:
        for i in range(1,N+1):
            if needs[i] == [0]:
                needs[i].clear()
                # for j in range(N):
                for j in range(1,N+1):
                    # print(needs)
                    if i in needs[j]:
                        needs[j].remove(i)
                        times[j] = max(times[j],times[i] + times_ori[j])

                break

    # 선행작업 끝났다면
        else:
            for x in range(1,N+1):
                if needs[x] != []:
                    min_v = -1
                    return
            min_v = min(min_v,max(times))
            return



from copy import deepcopy as dc
for tc in range(1,T+1):
    N = int(input())
    times_ori = [0]
    needs_ori = [0]
    for i in range(N):
        time,M,*need = map(int,input().split())
        need = list(need)
        if 0 not in need:
            need.append(0)
        needs_ori.append(need)
        times_ori.append(time)
    min_v = float('inf')
    # print(needs_ori)
    # print(times_ori)
    for coco in range(1,N+1):
        if min_v == -1:
            break
        # times = dc(times_ori)
        needs = dc(needs_ori)
        # print(needs)
        div = times_ori[coco]%2
        times_ori[coco] = times_ori[coco] // 2
        times = dc(times_ori)
        task()
        times_ori[coco] = times_ori[coco]*2 +div
    print(f'#{tc} {min_v}')
