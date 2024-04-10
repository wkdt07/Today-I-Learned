
def task():
    global result
    while True:
        for i in range(1,N+1):
            if needs[i] == [0]:
                needs[i].clear()
                for j in range(1,N+1):
                    if i in needs[j]:
                        needs[j].remove(i)
                        times[j] = max(times[j],times[i]+times_ori[j])
                break

        else:
            for k in range(1,N+1):
                if needs[k]:
                    result = -1
                    return
            result = min(result,max(times))
            return

from copy import deepcopy as dc

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    needs_ori = [0]
    times_ori = [0]
    for _ in range(N):
        time,M,*need = map(int,input().split())
        need = list(need)
        if 0 not in need:
            need.append(0)
        needs_ori.append(need)
        times_ori.append(time)

    result = float('inf')

    for coco in range(1,N+1):
        div = times_ori[coco] % 2
        times_ori[coco] = times_ori[coco]//2

        needs = dc(needs_ori)
        times = dc(times_ori)

        task()

        times_ori[coco] *= 2
        times_ori[coco] += div

    print(f'#{tc} {result}')