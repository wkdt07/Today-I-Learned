'''
좋은 구간
1. A와 B가 양의 정수이고 A<B이다.
2. A<=x<=B를 만족하는 정수 x가 집합S에 속하지 않는다.
3. 구간은 n을 포함해야 한다.
'''

L = int(input())

#L = 1일 때는?
S = list(map(int, input().split()))
S.sort()

n = int(input())

s_lst = []
e_lst = []

for i in S:
    if i <= n:
        s_lst.append(i)

    if i>=n:
        e_lst.append(i)

if s_lst == []:
    s_lst.append(0)

# if e_lst == []:
#     e_lst.append(n+1)   'False'
# 어차피 이러면 답이 무한이 됨

s_max = max(s_lst)
e_max = min(e_lst)
cnt = 0
for s in range(s_max+1,n+1):
    for e in range(n,e_max):
        if s<e:
            cnt += 1

print(cnt)

# s_lst.append(n)
# e_lst.append(n)
#
# e_lst.sort()
# e_lst = [n]
# s_max = s_lst[-2]
# #만약 리스트가 n 혼자면?
# e_max = e_lst[1]
# print(e_max)
# if s_max != n:
#     s_max += 1
#
# if e_max != n:
#     e_max -= 1



