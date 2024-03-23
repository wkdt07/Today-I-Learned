import sys
input = sys.stdin.readline
from heapq import heappush, heappop
T = int(input())

for _ in range(T):
    K = int(input()) # 연산의 수
    # I n -> n을 Q에 삽입
    # D 1 -> Q에서 최댓값을 삭제
    # D -1 -> Q에서 최솟값을 삭제
    # 제거 과정에서 동일 값이 있을 경우, 하나만 삭제됨
    # Q가 비어있는데 D가 적용되면 무시 가능s
    # q를 2개 만들어서 교집합만 비교?
    q_min = []
    q_max = []
    for k in range(K):
        a = input()
        calc = a[0]
        n = int(a[2:])
        if calc == 'I':
            heappush(q_min,n)
            heappush(q_max,-n)
        elif calc == 'D':
            if n == 1 and q_max: # 최대값 제거
                heappop(q_max)
            elif n == -1 and q_min:
                heappop(q_min)

        for i in range(len(q_max)):
            q_max[i] = q_max[i]*(-1)

        q_max = set(q_max)
        q_min = set(q_min)
        q = q_max & q_min # 근데 이러면 q에 같은 값이 들어있으면 확인할 수가 없는데...
        if q:
            print(max(q), min(q))
        else:
            print('EMPTY')


