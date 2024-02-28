# arr = ['A','B','C']
#
# def get_sub(tar):
#     for i in range(n):
#         if tar & 0x1: # 마지막 비트가 1이면
#             print(arr[i],end='')
#         tar >>= 1
#
# n = 3
#
# for tar in range(1<<n): # = range(0,8)
#     print(bin(tar))
#     print('{',end = '')
#     get_sub(tar)
#     print('}')

path = []
N = 3
def dice(level=0,start=1):
    if level == N:
        print(path)
        return

    for i in range(start,7):
        path.append(i)
        dice(level+1,i) # start를 i 그대로
        path.pop()

dice()