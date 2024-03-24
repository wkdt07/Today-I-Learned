# 강의의 순서가 바뀌면 안됨
# 특정 숫자만 넣으면 안됨. i와 j를 넣을거면 그 사이 모든 강의를 다 넣어야 함
from collections import deque as dq


N,M = map(int,input().split()) # N개의 동영상. M개의 블루레이,
vds = list(map(int,input().split())) # 비디오들 길이

sum_vds = sum(vds)
avrg = round(sum_vds/M) # 평균값 구하기
# print(avrg)
vds = dq(vds)
sum_lst = [avrg] * N


i = 0
sum_v = 0
while True:
    if len(sum_lst) == M:
        break

    sum_v += vds[i]

    if sum_v >= avrg:
        sum_lst.append(sum_v)
        sum_v = 0
        i += 1
        continue

    i += 1

print(sum_lst)