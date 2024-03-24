# 강의의 순서가 바뀌면 안됨
# 특정 숫자만 넣으면 안됨. i와 j를 넣을거면 그 사이 모든 강의를 다 넣어야 함

'''이분탐색에서 가장 중요한건 '무엇을 탐색하고, 그 시작과 끝을 뭘로 하냐' '''

# 특정 조건을 만족하는 값을 찾는 최적화 문제 -> 이진 탐색으로 변형할 수 있음
# https://www.youtube.com/watch?v=94RC-DsGMLo - 이진 탐색 관련 강의

N,M = map(int,input().split()) #N : 강의 갯수 M : 필요한 블루레이 갯수

vds = list(map(int,input().split()))

s,e = max(vds),sum(vds) # 모든 강의가 하나의 블루레이에 들어갈 수는 있어야 한다는 조건 때문에 최솟값은 vds의 최대, 끝값은 한 블루레이에 들어갈 수 있는 총 합



while s<=e:
    mid = (s + e) // 2  # 초기 mid 값

    cnt = 1

    sum_v = 0 # 각 블루레이의 합

    for i in range(N):
        sum_v += vds[i]
        if sum_v > mid: # 블루레이 값이 넘어가면
            cnt += 1 # 블루레이 하나 추가
            sum_v = vds[i] # 블루레이 내용물 초기화

        # if cnt > M:break  가지치기 될 줄 알았는데 오히려 시간 더 걸리네 ㅎㅎ;;
        # sum_v += vds[i] # 얘가 이 밑에 있어야 함. why? 위에 있으면 해당 vds[i]값이 증발하는 꼴임

    if cnt >M: # 블루레이 갯수 모자르다 -> 용량 늘려야 함

        s = mid+1

    elif cnt<= M: # 블루레이 갯수 넘친다 -> 용량 줄여야 함
        e = mid - 1
        rst = mid

    # else:
    #     break

    # cnt == M이라도 더 최적화 할 수도 있음

print(rst)




# from collections import deque as dq
#
#
# N,M = map(int,input().split()) # N개의 동영상. M개의 블루레이,
# vds = list(map(int,input().split())) # 비디오들 길이
#
# sum_vds = sum(vds)
# avrg = round(sum_vds/M) # 평균값 구하기
# # print(avrg)
# vds = dq(vds)
# sum_lst = [avrg] * N
#
#
# i = 0
# sum_v = 0
# while True:
#     if len(sum_lst) == M:
#         break
#
#     sum_v += vds[i]
#
#     if sum_v >= avrg:
#         sum_lst.append(sum_v)
#         sum_v = 0
#         i += 1
#         continue
#
#     i += 1
#
# print(sum_lst)