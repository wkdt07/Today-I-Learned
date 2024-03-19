N = int(input()) # 노드의 갯수

dic = {

}
for _ in range(N):
    root,left,right = input().split()
    dic[root]=[left,right]

rst1 = ''
rst2 = ''
rst3 = ''

def preorder(root): # 전위순회. VLR  LRV
    global rst1
    rst1 += root
    left = dic[root][0]
    right = dic[root][1]

    # print(root, end='')
    # print()
    if left != '.': # 왼쪽이 None이 될 때까지는 계속 함수 재귀 => 왼쪽 끝까지 간다
        preorder(left)
    # else: return
    # print(root, end='')
    # print()
    if right != '.': # 오른쪽이 None이 될 떄까지는 계속 함수 재귀 => 오른쪽 끝까지 간다
        # rst3 += right
        preorder(right)
    # print(root, end='') # 이 프린트의 위치에 따라 전위, 중위, 후위가 결정됨
    # else:return    # print(rst)

def inorder(root):
    global rst2
    left = dic[root][0]
    right = dic[root][1]

    # print(root, end='')
    # print()
    if left != '.': # 왼쪽이 None이 될 때까지는 계속 함수 재귀 => 왼쪽 끝까지 간다
        inorder(left)
    # else: return
    print(root, end='')
    # print()
    if right != '.': # 오른쪽이 None이 될 떄까지는 계속 함수 재귀 => 오른쪽 끝까지 간다
        # rst3 += right
        inorder(right)

def postorder(root):
    # global rst2
    left = dic[root][0]
    right = dic[root][1]


    if left != '.': # 왼쪽이 None이 될 때까지는 계속 함수 재귀 => 왼쪽 끝까지 간다
        postorder(left)

    if right != '.': # 오른쪽이 None이 될 떄까지는 계속 함수 재귀 => 오른쪽 끝까지 간다
        postorder(right)
    print(root, end='')
preorder('A')
print(rst1)
inorder('A')
print()
postorder('A')

# def preorder(root): # 전위순회. VLR  LRV
#     # global rst
#     # rst += root
#     left = dic[root][0]
#     right = dic[root][1]
#     print(root, end='')
#     # print()
#     if left != '.': # 왼쪽이 None이 될 때까지는 계속 함수 재귀 => 왼쪽 끝까지 간다
#         preorder(left)
#     # else: return
#     # print(root, end='')
#     # print()
#     if right != '.': # 오른쪽이 None이 될 떄까지는 계속 함수 재귀 => 오른쪽 끝까지 간다
#         preorder(right)
#     # print(root, end='') # 이 프린트의 위치에 따라 전위, 중위, 후위가 결정됨
#     # else:return    # print(rst)
#
# def inorder(root): # 전위순회. VLR  LRV
#     # global rst
#     # rst += root
#     left = dic[root][0]
#     right = dic[root][1]
#     # print()
#     if left != '.': # 왼쪽이 None이 될 때까지는 계속 함수 재귀 => 왼쪽 끝까지 간다
#         preorder(left)
#     # else: return
#     print(root, end='')
#     # print()
#     if right != '.': # 오른쪽이 None이 될 떄까지는 계속 함수 재귀 => 오른쪽 끝까지 간다
#         preorder(right)
#     # print(root, end='') # 이 프린트의 위치에 따라 전위, 중위, 후위가 결정됨
#     # else:return    # print(rst)
#
#
# def lastorder(root):  # 전위순회. VLR  LRV
#     # global rst
#     # rst += root
#     left = dic[root][0]
#     right = dic[root][1]
#
#     # print()
#     if left != '.':  # 왼쪽이 None이 될 때까지는 계속 함수 재귀 => 왼쪽 끝까지 간다
#         preorder(left)
#     # else: return
#     # print(root, end='')
#     # print()
#     if right != '.':  # 오른쪽이 None이 될 떄까지는 계속 함수 재귀 => 오른쪽 끝까지 간다
#         preorder(right)
#     print(root, end='') # 이 프린트의 위치에 따라 전위, 중위, 후위가 결정됨
#     # else:return    # print(rst)
#
# preorder('A')
# print()
# inorder('A')
# print()
# lastorder('A')
