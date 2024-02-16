# 자물쇠 N개를 해제
# D : 2배 , S : -1,단 0000 이면 9999 , L : rotate(-1) , R: rotate(1)
# 최소한의 동작으로 해제 번호를 맞추기
from collections import deque



# 숫자로 받아야 함

def Double(lst):
    N = cg(lst)
    N = (N*2)%10000
    N = str(N)
    if len(N) != 4:
        while len(N) != 4:
            N = '0'+N

    lst2 = []
    lst2.extend(N)
    return lst2

# 무조건 리스트로 받도록

def Subtract(lst):
    N = cg(lst)
    lst2 = []
    if N == 0:
        N = '9999'
        lst2.extend(N)
        return lst2
    else:
        N -= 1
        N = str(N)
        if len(N) != 4:
            while len(N) != 4:
                N = '0' + N

        lst2 = []
        lst2.extend(N)
        return lst2

def Left(N_lst):
    q = deque(N_lst)
    q.rotate(-1)
    return list(q)

def Right(N_lst):
    q = deque(N_lst)
    q.rotate(1)
    return list(q)



def cg(A):
    v = int(A[0]) * 1000 + int(A[1]) * 100 + int(A[2]) * 10 + int(A[3]) * 1
    return v



def dslr(A,B,ans =''):
    q = deque([])
    q.append([ans,A])
    v = cg(A)
    vst[v] = 1
    while q:
        ans,t = q.popleft()
        if t == B:
            break
        else:
            t1 = Double(t)
            v1 = cg(t1)
            ans1 = ans + 'D'
            if not vst[v1]:
                q.append([ans1,t1])
                vst[v1] =1
            t2 = Subtract(t)
            v2 = cg(t2)
            ans2 = ans + 'S'
            if not vst[v2]:
                q.append([ans2,t2])
                vst[v2] = 1
            t3 = Left(t)
            v3 = cg(t3)
            ans3 = ans + 'L'
            if not vst[v3]:
                q.append([ans3,t3])
                vst[v3] = 1
            t4 = Right(t)
            v4 = cg(t4)
            ans4 = ans + 'R'
            if not vst[v4]:
                q.append([ans4,t4])
                vst[v4] = 1
    return ans


N = int(input())
for _ in range(N):
    vst = [0] * 10000
    a, b = map(str, input().split())
    if len(a) != 4:
        while len(a) != 4:
            a = '0' + a
    if len(b) != 4:
        while len(b) != 4:
            b = '0' + b
    A, B = list(map(str, a)), list(map(str, b))

    print(dslr(A, B))






#     q = deque(['D','S','L','R'])
#     if A == B:
#         return ans
#     for d in q:
#         if d == 'D':
#             A = Double(A)
#             q.append('D')
#             ans += 'D'
#             dslr(A, B, ans)
#
#         if d == 'S':
#             A = Subtract(A)
#             q.append('S')
#             ans += 'S'
#             dslr(A, B, ans)
#
#         if d == 'L':
#             A = Left(A)
#             q.append('L')
#             ans += 'L'
#             dslr(A, B, ans)
#
#
#         if d == 'R':
#             A = Right(A)
#             q.append('R')
#             ans += 'R'
#             dslr(A, B, ans)



# q = deque([])
# def dslr(A,B,ans=''):
#     global q
#     q.extend(['D','S','L','R'])
#      # 이러면 dslr만 계속 반복함
#     if A == B:
#         return ans
#
#     t = q.popleft()
#     if t == 'D':
#         A = Double(A)
#         q.append('D')
#         ans += 'D'
#         dslr(A,B,ans)
#
#     if t == 'S':
#         A = Subtract(A)
#         q.append('S')
#         ans += 'S'
#         dslr(A, B, ans)
#
#     if t == 'L':
#         A = Left(A)
#         q.append('L')
#         ans += 'L'
#         dslr(A, B, ans)
#
#     if t == 'R':
#         A = Right(A)
#         q.append('R')
#         ans += 'R'
#         dslr(A, B, ans)




'''
def dslr(A,B,ans=''):
    if A == B:
        return ans
    # 끊기는 타이밍을 알아야 함
    dslr(Double(int(a)),B,ans + 'D')
    dslr(Subtract(int(a)), B, ans + 'S')
    dslr(Left(A),B,ans + 'L')
    dslr(Right(A),B,ans + 'R')

# print(A,B)
'''
