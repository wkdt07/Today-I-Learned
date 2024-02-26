'''
게임 단계에 따라 3x3에서 8x8 규격의 표적이 나타납니다.
- 가로 한 줄에서 한 개의 표적을 선택할 수 있습니다.
- 세로 한 줄에서 한 개의 표적을 선택할 수 있습니다.-> 가로, 세로 둘 다 기억해야함
- 한 줄에서 2개 이상의 표적을 맞추면 그 단계는 실격입니다. -> 실격하면 안 된다.
- 어떤 단계에는 표적 한 개의 점수가 음수로 나타날 수 있습니다. 이
표적을 맞히면 그 단계는 실격입니다. -> 음수 맞추면 안 된다
'''
'''
T = int(input())

def BackTracking(i = 0, tmp = 0):
    global res
    if i == n: # 모든 가로줄을 탐색한 경우 종료
        # res = max(tmp, res) # 최댓값 갱신
        res.append(tmp)
        return # 이전 노드로 돌아가기 -> cnt -1 , tmp = tmp - arr[cnt][i]

    for j in range(n):
        # 세로 cnt 가로 i 로 설정 # 여기로 도는 경우는 j가 2 미만이면서, i가 3이 아닐 때 , j=2이면 끝남. -> 재귀 함수 하나 끝나는거
        if not visited[j]:  # 가본 적 없는 세로줄
            if arr[i][j] >= 0:
                visited[j] = 1
                BackTracking(i + 1, tmp + arr[i][j])    # 새로운 가로줄에서 다시 탐색
                # return으로 돌아오면
                visited[j] = 0  # 이번 가로줄에서 새로운 선택을 위해 다시 '미방문' 으로 처리
                # 여기서 j = 2라면 해당 재귀 함수가 끝나버린다
                # 그래서 i값이 이전으로 돌아간다.
                # 파이썬 튜터 돌려봐라
                


for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # res = -10 ** 6     # 최댓값 초기화
    res = []
    visited = [0] * n
    BackTracking()

    print(f'#{tc} {res}')
'''
T = int(input())

def BackTracking(cnt = 0, tmp = 0):
    global res
    if cnt == n: # 모든 가로줄을 탐색한 경우 종료
        res = max(tmp, res) # 최댓값 갱신
        return

    for i in range(n):  # 가로 cnt 세로 i 로 설정
        if not visited[i]:  # 가본 적 없는 세로줄
            if arr[cnt][i] >= 0:
                visited[i] = 1
                BackTracking(cnt + 1, tmp + arr[cnt][i])    # 새로운 가로줄에서 다시 탐색
                visited[i] = 0  # 이번 가로줄에서 새로운 선택을 위해 다시 '미방문' 으로 처리

for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    res = -10 ** 6     # 최댓값 초기화
    visited = [0] * n
    BackTracking()

    print(f'#{tc} {res}')

    # https: // www.youtube.com / watch?v = Ar40zcPoKEI
'''
T = int(input())

for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    vst_j= [True]*(N)

    # sum_v = 0
    sum_lst = []




    # while True:
    #     for i in range(N):
    #         if vst_i[i]:
    #             vst_i[i] = False
    #             for j in range(N):
    #                 if vst_j[j]:
    #                     vst_j[j] = False
    #                     sum_v += arr[i][j]
    #     sum_lst.append(sum_v)


    def rating(i=0,sum_v = 0,vst_j = [True]*(N)):
        global sum_lst
        # global sum_v
        # vst_i[i] = False
        if i == N:
            sum_lst.append(sum_v)
            return
        for j in range(N):
            if vst_j[j] and arr[i][j]>=1:
                sum_v += arr[i][j]

                vst_j[j] = False
                rating(i+1,sum_v,vst_j)
                vst_j[j] = True
                # return

    rating()
    rst = max(sum_lst)
    print(f'#{t} {rst}')

            # else:
            #     # vst_i[i] = True
            #     # vst_j[j] = True
            #     return
    #     # for i in range(N):
    #     #     if vst_i[i]:
    #     #         vst_i[i] = False
    #     #         for j in range(N):
    #     #             if vst_j[j] and arr[i][j]>0:
    #     #                 sum_v += arr[i][j]
    #     #                 vst_j[j] = False
    #     #                 rating(sum_v,cnt + 1)
    #     #                 vst_i[i] = True
    #     #                 vst_j[j] = True
    #     #                 return
    #     # return
'''
