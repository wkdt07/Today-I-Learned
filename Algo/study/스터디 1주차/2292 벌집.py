n = int(input())

i = 1
e = 1
k = 0
t = True
while t == True:
    if n <= e: # range로 비교할 필요 없이 e만 변경해서
        print(i)
        t = False

    else:
        k += i
        e = 6*k+1
        i += 1


# n = int(input())
# k = True
# i =1
# s,e = 2,7
# while k == True:
#     if n in range(s,e+1):
#         print(i+1)
#         k = False
#     else:
#         s = e+1
#         e += 6*(i+1)
#         i += 1 시간초과



