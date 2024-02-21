# 모든 쓰레기를 다 처리하고, 쓰레기차의 총 이동거리 구하기
'''
1. 쓰레기의 양이 용량에 도달
2. 해당 지점에서 쓰레기차의 용량이 넘을 떄 -> 1,2번 묶을 수 있다
3. 더 이상 쓰레기를 실을 지점이 없을 때
'''

T = int(input())

for _ in range(T):
    W, N = map(int, input().split())
    x = [0] * N
    w = [0] * N
    cnt = 0
    W1 = W # 잔여용량

    for i in range(N):
        x[i], w[i] = map(int, input().split())

    i = 0
    while i < N:
        if W1 == w[i]:
            cnt += 2 * x[i]
            i += 1
            W1 = W # 비우고 와서 잔여용량 리셋

        elif W1 > w[i]:
            W1 -= w[i]
            i += 1

        else:
            cnt += 2 * x[i]
            W1 = W

    if W1 < W:
        cnt += 2 * x[N-1]

    print(cnt)

# for t in range(T):
#     W,N = map(int,input().split()) # W:쓰레기 차 용량, N: 쓰레기가 있는 지점의 갯수
#     x_lst = []
#     w_lst = []
#     for _ in range(N):
#         x_i,w = map(int,input().split()) #x_i : 쓰레기장으로부터의 거리, w: 쓰레기의  양
#         x_lst.append(x_i)
#         w_lst.append(w)
#     max_x = max(x_lst)
#     arr = [0] * (max_x+1)
#     for i in range(len(x_lst)):
#         arr[x_lst[i]] = w_lst[i] #arr[x] = w
#     # print(arr)
#     '''
#     [0,1,2]라면
#     idx=2까지 갔을 때(+2)일 때 한 번 돌아가서 비우고, 이후 다시 2로 돌아와서 쓰레기를 담고, 그 다음 돌아가서 쓰레기를 버린다.
#     '''
#     def dump():
#         w = 0
#         cnt = 0
#         if sum(arr)<W:
#             return 2*(len(arr)-1)
#
#         for i in range(1,len(arr)):
#             w_temp = w
#             if arr[i] != 0:
#                 w_temp += arr[i]
#                 if w_temp < W:
#                     w += arr[i]
#
#                 if w_temp == W:
#                     cnt += 2*i
#                     w = 0
#
#                 if w_temp >W:
#                     cnt += 2*i
#                     w = arr[i]
#         if w != 0:
#             cnt += 2*(len(arr)-1)
#         return cnt
#
#     print(dump())