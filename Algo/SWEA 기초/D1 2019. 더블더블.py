T=int(input())

a=1
a_list=[1]
for i in range(T):
    a*=2
    a_list.append(a)

# for j in a_list:
#     print(j, end=' ')

print(*a_list)