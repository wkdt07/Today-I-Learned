'''
T = int(input())

for t in range(1,T+1):
    arr = [1,2,3,4,5,6,7,8,9,10,11,12]

    n = len(arr)
    subset = []
    for i in range(1 << n):
        s = []
        for j in range(n):
            if i & (1 << j):
                s.append(arr[j])
        subset.append(s)  # 부분집합 모음
    n,k = map(int,input().split())

    count = 0
    for sub in subset:
        if (len(sub) == n) and (sum(sub)==k):
            count += 1

    print(f'#{t} {count}')
    '''

# import itertools
# T = int(input())
# A = list(range(1,13))
#
# for t in range(1,T+1):
#     N,K = map(int,input().split())
#     combs = itertools.combinations(A,N)
#     cnt = 0
#     for comb in combs:
#         if sum(comb)==K:
#            cnt+=1
#
#     print(f'#{t} {cnt}')


arr = list(map(int,input().split()))
arr.sort

i =0
N= len(arr)
K = 3
combs = []
while i<=N:
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            chosen = arr[i],arr[j],arr[k]
            combs.append(chosen)
    i+= 1

cnt_run = 0
cnt_triple = 0

for comb in combs:
    if comb[0]==comb[1]==comb[2]:
        cnt_triple += 1
    if (comb[2]-comb[1] == 1) and (comb[1]-comb[0] == 1):
        cnt_run += 1

if cnt_run >= 1 and cnt_triple >= 1:
    print(True)

else:
    print(False)