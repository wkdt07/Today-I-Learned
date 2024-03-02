# 4개의 케이스 중 어디에 속해있는지
'''
1. 겹친 영역이 존재
2. 겹친 선이 존재
3. 겹친 점이 존재
4. 해당 없음

x1,y1  x2,y2 로 만들어지는 사각형임

x1<x2로 확정이지만 y는 확정난게 없음
'''

#
# T = int(input())
#
# for tc in range(1,T+1):
#     x1_1,y1_1,x2_1,y2_1 = map(int,input().split())
#     x1_2,y1_2,x2_2,y2_2 = map(int,input().split())
#
#
#     max_x = max(x2_1,x2_2)
#
#     y1_max = max(y1_1,y2_1)
#
#     y1_min = min(y1_1,y2_1)
#
#     y2_max = max(y1_2,y2_2)
#
#     y2_min = min(y1_2,y2_2)
#
#     max_y = max(y1_max,y2_max)
#
#     cnt_square = [[0] * (1001) for _ in range(1001)]
#
#     cnt_lst = [0] * 5
#
#     for i in range(x1_1,x2_1+1):
#         for j in range(y1_min,y1_max+1):
#
#             if j == y1_min or j == y1_max or i == x1_1 or i == x2_1:
#                 cnt_square[i][j] += 1
#             cnt_square[i][j] += 1
#             cnt_lst[cnt_square[i][j]] += 1
#
#
#     for i in range(x2_1,x2_2+1):
#         for j in range(y2_min,y2_max+1):
#             if j == y2_min or j == y2_max or i == x2_2 or i == x1_2:
#                 cnt_square[i][j] += 1
#             cnt_square[i][j] += 1
#             # cnt_lst[cnt_square[i][j]] += 1
#     for i in range(0,1001):
#         for j in range(0,1001):
#             # cnt_square[i][j] += 1
#             if cnt_square[i][j]:
#                 cnt_lst[cnt_square[i][j]] += 1
#
#     print(cnt_lst)
    # if cnt_lst[4] == 1:
    #     print(3)
    #
    # if cnt_lst[4]>1 and cnt_lst[3]

T = int(input())

for t in range(1,T+1):
    arr = [[0]*1001 for _ in range(1001)]
    cnt = [0] * 5 # 4가지 경우

    for _ in range(2): # 두 개의 사각형
        x1,y1,x2,y2 = map(int,input().split())

        for i in range(y1,y2+1): # 사각형 테두리 또는 사각형의 내부
            for j in range(x1,x2+1):
                if i == y1 or i == y2 or j == x1 or j == x2: # 테두리의 경ㅇ
                    arr[j][i] += 1
                arr[j][i] += 1
                cnt[arr[j][i]] += 1 # 각 영역의 카운트 업데이트
    print(cnt)
    # 1: 하나의 영역 2: 하나의 선 3: 선과 영역이 겹치는 부분 # 4: 선끼리 겹치는 부분
    if cnt[4] == 1: # 3번 상태 (겹치는 영역 없고, 겹치는 선 없음) 점만 겹침
        ans = 3
    elif cnt[4] > 1 and cnt[3] > 0: # 1번 상태.
        ans = 1
    elif cnt[4] > 1: # 2번 상태, 선이 겹침
        ans = 2
    else: # 아예 겹치는 영역이 없음
        ans = 4

    print(f'{t} {ans}')
