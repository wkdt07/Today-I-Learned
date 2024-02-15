N = int(input())

lst = [500]

for n in range(N):
    a,b = map(int,input().split())

    lst.append(a)
    lst.append(b)
    lst.sort()
    mid = len(lst)//2
    print(lst[mid])