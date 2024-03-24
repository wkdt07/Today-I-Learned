import sys

input = sys.stdin.readline
from heapq import heappush, heappop, heapify

T = int(input())

for _ in range(T):
    K = int(input())  # 연산의 수
    # I n -> n을 Q에 삽입
    # D 1 -> Q에서 최댓값을 삭제
    # D -1 -> Q에서 최솟값을 삭제
    # 제거 과정에서 동일 값이 있을 경우, 하나만 삭제됨
    # Q가 비어있는데 D가 적용되면 무시 가능s
    # q를 2개 만들어서 교집합만 비교?
    q_min = []
    q_max = []
    vst = {}
    for k in range(K):
        # vst = []
        a = input().split()
        calc = a[0]

        n = a[1]
        if calc == 'I':
            n = int(n)
            heappush(q_min, n)
            heappush(q_max, -1 * n)
            if vst.get(n) != None:
                vst[n] = vst[n] + 1
            else:
                vst.setdefault(n,1)
                # vst[n] = vst[n] + 1
        elif calc == 'D':
            if n == '1' and q_max:  # 최대값 제거
                # if t_min:
                #     q_max.remove(-1 * t_min)
                #     heapify(q_max)
                #     t_min = None

                # q_min.remove(t_max_rev) # todo 시간 초과 난다면 여기서
                while q_max:
                    t_max = heappop(q_max)
                    t_max_rev = -1 * t_max
                    if vst.get(t_max_rev):
                        vst[t_max_rev] -= 1
                        break
                    else: continue

            elif n == '-1' and q_min:
                # if t_max:
                #     q_min.remove(-1*t_max)
                #     heapify(q_min)
                #     t_max = None
                while q_min:
                    t_min = heappop(q_min)  # 여기서 뺴준걸 위에서도 빼줘야 한다.
                    # t_min_rev = -1 * t_min
                    # q_max.remove(t_min_rev) # todo 시간 초과 난다면 여기서
                    if vst.get(t_min):
                        vst[t_min] -= 1
                        break
                    else:
                        continue
    # todo 디버그로 어떤 상황인지 확인
    #    if t_max:
    #        q_min.remove(-1 * t_max)
    #        heapify(q_min)
    #    if t_min:
    #        q_max.remove(-1 * t_min)
    #        heapify(q_max)

    # todo 특히 이거
    # print(q_max)
    # print(q_min)
    INF = int(1e7)
    max_v = INF
    min_v = INF


    while q_max:
        mx = -heappop(q_max)
        if vst.get(mx):
            max_v = mx
            break
    while q_min:
        nx = heappop(q_min)
        if vst.get(nx):
            min_v = nx
            break

    if max_v == INF and min_v == INF:
        print('EMPTY')
    else:
        print(max_v, min_v)


    # if q_max or q_min:
    #     max_v = -1 * heappop(q_max)
    #     min_v = heappop(q_min)
    #     print(max_v, min_v)
    # else:
    #     print('EMPTY')
    # print(vst)
    # for i in range(len(q_max)):
    #     q_max[i] = q_max[i] * (-1)
    #
    # # print(q_min)
    # # print(q_max)
    # q_max = set(q_max)
    # q_min = set(q_min)
    # q = q_max & q_min  # 근데 이러면 q에 같은 값이 들어있으면 확인할 수가 없는데...
    # q = list(q)
    # q = sorted(q_min)
    # if q:
    #     print(q[-1], q[0])
    # else:
    #     print('EMPTY')


