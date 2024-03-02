# 보너스 점수를 측정하는 bonus라는 변수가 새로 필요
# 근데 틀렸을 때 점수를 받게 하면 마지막까지 다 맞은 친구는 보너스 점수를 못 받음
# 그러니깐 마지막엔 보너스 점수가 몇 점이던간에 일단 더하고 봐야함

T = int(input())

for t in range(1,T+1):
    N,M = map(int,input().split()) # N은 학생 수, M은 문제의 수
    answer = list(map(int,input().split())) #정답
    prob_arr = [list(map(int,input().split())) for _ in range(N)]
    # print(prob_arr)

    score_lst = []

    for k in range(N):
        score = 0
        bonus = 0
        for i in range(M):
            if prob_arr[k][i] == answer[i]:
                score += 1
                score += bonus
                bonus += 1
            else:
                # score += bonus
                bonus = 0
        # score += bonus
        score_lst.append(score)
    rst = max(score_lst) - min(score_lst)
    print(f'#{t} {rst}')

