N = int(input())

cand = ['A','B','C']



def choice(rst='',cnt=0):
    global k

    if len(rst)>=3 and (rst[-1]==rst[-2] and rst[-2]==rst[-3]):
        return

    if cnt == N:
        k += 1
        return

    for c in cand:
        choice(rst + c,cnt+1)

k = 0

choice()

print(k)