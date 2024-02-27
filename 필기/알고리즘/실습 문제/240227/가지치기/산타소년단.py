N = int(input())

members = ['b','t','k','r']

vst = {'b':0,
       't':0,
       'k':0,
       'r':0
       }

def bts(cnt=1):
    global rst
    if cnt == N:
        rst += 1
        return

    for mb in members:
        if not vst[mb]:
            vst[mb] = 1
            bts(cnt+1)
            vst[mb] = 0

rst = 0

bts()

rst *= (N)

print(rst)