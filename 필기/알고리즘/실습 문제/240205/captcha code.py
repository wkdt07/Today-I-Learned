T = int(input())

for t in range(1,T+1):
    N,K = map(int,input().split())
    cap = list(map(int,input().split()))
    pas = list(map(int,input().split()))
    n = K

    first = pas[0]
    stop = True
    while stop == True:

        for cd in cap:
            first = pas[0]
            if first not in cap:
                print(f'#{t}', 0)
                stop = False
                break
            if cd == first:
                idx = cap.index(cd)
                cap = cap[idx+1:N]
                pas.remove(cd)

                if len(pas)==0:
                    print(f'#{t}', 1)
                    stop = False
                    break



