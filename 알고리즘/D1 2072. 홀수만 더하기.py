T=int(input())

for t in range(1,T+1):
    a=list(map(int,input().split()))
    print(a)
    for i in a:
        if i % 2 == 0:
            a.remove(i)
    print(a)
    total = sum(a)
    print(f'#{t} {total}')


# for t in range(1,T+1):
#     a=list(map(int,input().split()))
#     b=[]
#     for i in a:
#         if i % 2 != 0:
#             b.append(i)
#     print(b)
#     total = sum(b)
#     print(f'#{t} {total}')

# 두번째 commit