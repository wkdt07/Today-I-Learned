N,L = map(int,input().split())

lst = list(map(int,input().split()))

lst.sort()

cnt = 0
i = 0
j= 1
while j < N:
    s = lst[i]
    e = lst[j]
    if j == N-1:
        if e-s <=L:
            cnt += 1
        else:
            cnt += 2
        break

    if (e-s)+1 < L:
        j+=1

    elif (e-s)+1 > L:
        cnt += 1
        i = j
        j += 1

    elif e -s +1 == L:
        cnt += 1
        i = j+L-1
        j += L

print(cnt)


# N,L = map(int,input().split())
#
# hole = list(map(int,input().split()))
#
# lst = [0]*(max(hole)+L)
#
# for i in hole:
#     lst[hole] = 1
#
# for i in range(len(lst)):
#     if lst[i] == 0:
#         continue
#
#     else: #lst[i] ==1
#         for j in range(i,i+L):
#             if lst[j] == 1:
#
