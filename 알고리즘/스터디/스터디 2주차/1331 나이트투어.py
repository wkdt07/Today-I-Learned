
'''
나이트 투어
1. 간 곳은 다시 가면 x -> set으로 중복확인
2. 마지막 위치에서 처음 위치로 돌아갈 수 있어야 한다.
3. 다음 칸은 나이트가 갈 수 있는 곳이어야 한다.
'''

# 좀 더 간단한 풀이? 딕셔너리로?

alp_lst = ['A','B','C','D','E','F']

def next(start,end): # 다음 칸으로 갈 수 있는지
    alp = start[0]
    alp_idx = alp_lst.index(alp)
    num = int(start[1:])
    next_lst = []
    if alp_idx -1 >= 0  : # alp 기준
        next_num1 = str(num - 2)
        next_num2 = str(num + 2)
        next_alp = alp_lst[alp_idx-1]
        next1 = next_alp + next_num1
        next2 = next_alp + next_num2
        next_lst.extend((next1,next2))
    if alp_idx -2 >= 0 :
        next_num3 = str(num - 1)
        next_num4 = str(num + 1)
        next_alp = alp_lst[alp_idx-2]
        next3 = next_alp + next_num3
        next4 = next_alp + next_num4
        next_lst.extend((next3,next4))
    if alp_idx + 1 <= 5 :
        next_num5 = str(num - 2)
        next_num6 = str(num + 2)
        next_alp = alp_lst[alp_idx+1]
        next5 = next_alp + next_num5
        next6 = next_alp + next_num6
        next_lst.extend((next5,next6))
    if alp_idx + 2 <= 5:
        next_num7 = str(num-1)
        next_num8 = str(num+1)
        next_alp = alp_lst[alp_idx + 2]
        next7 = next_alp + next_num7
        next8 = next_alp + next_num8
        next_lst.extend((next7,next8))
    if end in next_lst:
        return True
    else:
        return False


def chess(lst):
    # 0 . 무조건 다음으로 갈 수 있어야 함
    for i in range(35):
        s = lst[i]
        e = lst[i+1]
        if not next(s,e):
            return 'Invalid'


    # 1. 간 곳은 다시 가면 x
    if len(set(lst)) != len(lst):
        return 'Invalid'

    #2. 마지막 위치로 돌아갈 수 있어야 한다
    if not next(lst[-1],lst[0]):
        return 'Invalid'

    return 'Valid'

lst = [input() for _ in range(36)]
print(chess(lst))