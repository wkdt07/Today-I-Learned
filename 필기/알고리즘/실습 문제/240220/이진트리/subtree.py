T = int(input())
# 노드 N을 기준으로 그 아래의 서브 트리에 속한 노드의 갯수 구하기

# def pre_order(T): # 전위순회
#     if T:
#         visited()
#         pre_order(left[T])
#         pre_order(right[T])

def subtree(n):
    global cnt
    if n == 0:
        return
    else:
        if right[n]:
            cnt += 1
            subtree(right[n])
        if left[n]:
            cnt += 1
            subtree(left[n])


for t in range(1,T+1):
    E , N = map(int,input().split()) # E: 간선의 갯수, N: 노드의 갯수. 노드 번호는 1번부터 E+1까지
    par = [0] * (E+2)
    left = [0] * (E+2)
    right = [0] * (E+2)
    visited = [0]*(E+2)
    arr = list(map(int,input().split())) # 일단 저장
    cnt = 1
    for i in range(E):
        p,c = arr[i*2],arr[i*2+1]
        par[c] = p # 자식을 인덱스로 하는 부모
        if left[p]:
            right[p] = c
        else:
            left[p] = c
    subtree(N)
    print(f'#{t} {cnt}')


    # print(f'par={par}')
    # print(f'left={left}')
    # print(f'right={right}')
