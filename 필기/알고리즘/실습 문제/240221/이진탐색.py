def bst(n):  # n은 인덱스(노드 번호)
    global node  # 박아넣을 값

    if n <= N:  # 전체 노드의 수 N보다 n이 작거나 같을 때

        bst(n * 2)  # 왼쪽 자식 노드로 이동

        tree[n] = node  # 현재 노드
        node += 1

        bst(n * 2 + 1)  # 오른쪽 자식 노드로 이동


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    tree = [0 for i in range(N + 1)]
    node = 1
    bst(1)
    print(f'#{t} {tree[1]} {tree[N // 2]}')
# def enq(n):
#     global last
#     last += 1
#     h[last] = n # 일단 넣어놓고
#     c = last # last의 인덱스
#     p = c//2 # c의 부모 인덱스
#     while p >= 1:
#         if c == 2*p : #left일 때
#             if h[p] < h[c]:
#                 h[p],h[c] = h[c],h[p]
#             c = p
#             p = c//2
#         if c == 2*p+1: # right일 때
#             if h[p]>h[c]:
#                 h[p], h[c] = h[c], h[p]
#             c = p
#             p = c // 2

#
# def inorder(idx):
#     global num
#     if idx * 2 not in range(1, N + 1):
#         arr[idx] = num
#         num += 1
#         return
#     inorder(2 * idx) #L
#     arr[idx] = num #V
#     num += 1
#     if idx * 2 + 1 in range(1, N + 1): #R
#         inorder(2 * idx + 1)
#
#
# T = int(input())
# for t in range(1, T + 1):
#     N = int(input())
#     arr = [0] * (N + 1)
#     idx = 1
#     num = 1
#     inorder(1)
#     print(f'#{t} {arr[1]} {arr[N // 2]}')


# preorder(2 * n)
# preorder(2 * n + 1)



# for t in range(1,T+1):
#     N = int(input())
#     h = [0]*(N+1)
#     last = 0
#     for i in range(1,N+1):
#         enq(i)
#     print(h)

