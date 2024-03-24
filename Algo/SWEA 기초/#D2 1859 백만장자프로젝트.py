T=int(input())

for t in range(1,T+1):
    n=int(input())
    price=list(map(int,input().split(' ')))
    a=price[::-1]
    max_one=0
    benefit=0
    for m in a:
        if max_one<m:
            max_one=m
            t=a.index(max_one)
            benefit+=m-sum(a[:t])
            #갱신 안 될때 더하는걸로 다시 생각
    print(benefit)

    
    
