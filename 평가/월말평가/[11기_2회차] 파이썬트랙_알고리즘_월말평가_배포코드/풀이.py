'''
# 1
T = int(input())

for t in range(1,T+1):
    N,M = map(int,input().split()) # N: 돌의 갯수, M: 작업 수
    arr = list(map(int,input().split()))

    for _ in range(M): # 작업 반복
        i,j,w = map(int,input().split()) #i 기준위치 j 개수 w 작업
        i -= 1 # 순서 -> 인덱스 반환

        if w == 1:
            for p in range(i,i+j):
                if p < N:
                    arr[p] = (arr[p]+1)%2 #0,1을 반전
                
        elif w == 2:
            for p in range(i,i+j):
                if p < N:
                    arr[p] = arr[i]
        
        elif w == 3:
            for p in range(1,j+1):
                if 0 <= i - p and i+p < N:
                    if arr[i-p] == arr[i+p]: # 같으면 뒤집기
                        arr[i-p] = (arr[i-p] +1 ) % 2
                        arr[i+p] = arr[i-p]
    
    print(f'#{t}',*arr)
'''

# 2

def func(i,k,s):
    global max_v
    if i == k:
        if max_v < s:
            max_v = s
    else:
        for j in range(i,k):
            p[i],p[j] = p[j],p[i]
            if target[i][p[i]] > 0 : # 실격이 되는 표적을 제외
                func(i+1,k,s+target[i][p[i]])
            p[i],p[j] = p[j][i]

T = int(input())

for t in range(1,T+1):
    N = int(input())
    target = [list(map(int,input().split()))]
    p = [i for i in range(N)]
    max_v = 0
    func(0,N,0)
    print(f'#{t} {max_v}')
    
                    