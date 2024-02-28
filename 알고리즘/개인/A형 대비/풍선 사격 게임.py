# from copy import deepcopy

def shot(sum_v=0,level = 0):
    global ans_lst
    if level == N-1:
        idx = vst[1:N+1].index(0)
        temp = balloons[idx-1]
        ans_lst.append(sum_v+temp)
        return

    for i in range(1,N+1):
        if not vst[i]:
            #
            vst[i] = 1
            #왼쪽
            l = 1
            while i-l: # todo 인덱스 확인
                if vst[i-l]: #이미 터진 애면
                    l += 1
                else:break

            left_shot = balloons[i-l]
            r = 1
            while i+r <= N:
                if vst[i+r]:
                    r+=1
                else:break

            right_shot = balloons[i+r]

            if left_shot and right_shot: # 둘 다 0이 아니면
                tmp = left_shot*right_shot
            else:
                tmp = left_shot+right_shot
            shot(sum_v + tmp,level+1)
            vst[i] = 0


# if i == 0:
            #     sum_v += lst_same[i+1]
            # elif i == len(lst_same)-1:
            #     sum_v += lst_same[i-1]
            # else:
            #     sum_v += lst_same[i-1]*lst_same[i+1]


T = int(input())

for t in range(1,T+1):
    ans_lst = []
    N = int(input()) # 풍선의 갯수
    vst = [0]*(N+2) #인덱스 저장할거임
    balloons = list(map(int,input().split()))
    balloons.append(0)
    balloons = [0] +balloons
    print(balloons)
    print(vst)
    # lst_same = balloons.dc
    shot()
    print(len(ans_lst))
    # rst = max(ans_lst)
    # print(f'#{t} {rst}')
