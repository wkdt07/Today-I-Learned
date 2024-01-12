test=int(input())

for i in range(1,test+1):
    a=input()
    
    t=[]
    for k in range(1,len(a)):
        if a[:k] == a[k:2*k]:
            length=k
            t.append(length)
    print(t[0])

