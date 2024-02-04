import sys

A = int(input())

# deg = [6*i for i in range(61) ] # 각 분당(인덱스랑 같음) 분침이 이루는 각도 위치
# # print(deg_lst)
#
# h_move = 0 #이걸 넣는 이유? h의 위치는 deg[h_move]...아닌데? [6,12,18,24,30]
# m_same_deg = [] # 시침이 움직였을 때 분침의 각도 위치
# for m in range(60):
#     m_deg = deg[m]
#     if m %12 == 0:
#         h_move += 1
#         print(deg[h_move])
#         m_same_deg.append(m_deg)
# print(m_same_deg)
#
'''
차라리 각 시간대별로 접근해볼까?

{ 1: [0,6,9,12...] 2:[15,18,...]} 이런 식으로 
# 한 시간에 15도씩
근데 차이를 구하는건데?

'''


m = 0 # 분
h = 0 # 시간
h_deg = 0
dif_lst = []
while h<=12:
    m_deg = m * 6
    if m != 0 and m % 12 ==0:
        h_deg += 1

    if m!=0 and m % 60 ==0:
        m = 0

    dif = abs(m_deg - h_deg)
    if dif > 180:
        dif -= 180

    if h_deg>=15 and h_deg % 15 == 0:
        h+=1
    dif_lst.append(dif)
    m += 1
dif_set = set(dif_lst)
print(len(dif_set))

# 이러면 0부터 180까지 다 나온다.