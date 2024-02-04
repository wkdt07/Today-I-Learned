a='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
b=list(range(1,27))

d={}
for i in range(26):
    d[a[i]]=b[i]
a=list(input())
# print(a)
for j in a:
    print(d[j],end=' ')


# a=[1,2,3,4]
#
# for i in a:
#     print(i, end=' ')