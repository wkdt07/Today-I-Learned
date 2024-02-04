T=int(input())

a=''

for t in range(1,T+1):
    if T % t == 0:
        a+=str(t)+' '

print(a)
