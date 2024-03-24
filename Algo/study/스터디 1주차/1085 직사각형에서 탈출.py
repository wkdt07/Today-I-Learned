x,y,w,h = map(int,input().split())

lst = []
dxp,dxm,dyp,dym = (w-x),(x),(h-y),(y)
lst.extend([dxp,dxm,dyp,dym])

print(min(lst))
