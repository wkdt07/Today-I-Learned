# N = int(input()) # 탑의 갯수
#
# tops = [[0],[i for i in range(N,0,-1)],[],[]] #tops[0]는 그냥 인덱스 맞추기 용
#
#
#
# '''
# 한 번에 한 개의 원판만을 다른 탑으로 옮길 수 있다.
# 쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.
# '''
#
# print(2**N-1)

n,m = map(int,input().split())


lst= list(map(int,input().split()))

low = 0
high = low+1

cnt = 0
while low <= n-2:
    if lst[low] + lst[high] == m:
        cnt += 1
    low += 1
    high = low + 1

print(cnt)
