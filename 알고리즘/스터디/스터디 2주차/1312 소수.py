a,b,n = map(int,input().split())

cnt = 1

x = a%b # x는 나머지, 여기다가 10을 곱한 후 다시 b로 나눈 몫이 소수점 첫째자리

while cnt <= n:
    a = (x*10)//b
    x = (x*10)%b
    cnt += 1

print(a)

# p =f'{a/b}'
#
# lst = p.split('.')
#
# if len(lst[1])>=n+1:
#     print(lst[1][n+1])
#
# else:
#     print(lst[1][-1])

# 순환소수일 경우에는?

# 그냥 나누기로 접근하자

