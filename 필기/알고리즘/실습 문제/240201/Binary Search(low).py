n = int(input())

lst = list(map(int,input().split()))

k = int(input())

f_lst = list(map(int,input().split()))

c_lst = []
for f in f_lst:
    if f in lst:
        c_lst.append('O')
    else:
        c_lst.append('X')
#
st = ''.join(c_lst)
print(st)
# ['o','x',]
# print(c_lst)

# for c in c_lst:
#     print(c,end='') 이렇게 해도 됨