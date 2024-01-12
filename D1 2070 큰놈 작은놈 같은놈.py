T=int(input())

for t in range(1,T+1):
    a=list(map(int,input().split()))
    if a[0] < a[1]:
           print(f'#{t} <')

    elif a[0] > a[1]:
           print(f'#{t} >')

    elif a[0]==a[1]:
          print(f'#{t} =')