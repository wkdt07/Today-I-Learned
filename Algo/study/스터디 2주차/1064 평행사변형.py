from math import sqrt as sq

import itertools

xa,ya,xb,yb,xc,yc = map(int,input().split())
x_lst = [xa,xb,xc]
y_lst = [ya,yb,yc]
def check():
    # 평행사변형을 만들 수 없는 경우
    # 기울기 접근
    # 나누기는 사실상 곱하기로 접근해도 상관 없음

    if (ya-yb)*(xc-xa)== (yc-ya)*(xa-xb) and (ya-yb)*(xb-xc)==(yb-yc)*(xa-xb):
        return -1.0

    # 구하는건 좌표가 아닌 길이

    d1 = sq((xa - xb) ** 2 + (ya - yb) ** 2)
    d2 = sq((xa - xc) ** 2 + (ya - yc) ** 2)
    d3 = sq((xb - xc) ** 2 + (yb - yc) ** 2)

    d_lst = [d1,d2,d3]
    combs = list(itertools.combinations(d_lst,2))

    min_v = float('inf')
    max_v = 0
    for comb in combs:
        min_v = min(min_v,2*sum(comb))
        max_v = max(max_v,2*sum(comb))

    result = max_v - min_v
    return result

print(check())