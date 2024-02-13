n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
e = (n-1,n-1)
s = 0,0
visited = [[0 for _ in range(n)] for _ in range(n)]
dir = [(0,1),(0,-1),(1,0),(-1,0)]

def bt(s,e):
    i = s[0]
    j = s[1]
    ei, ej = e
    visited[i][j] = 1

    for k in dir:
        ni = i + k[0]
        nj = j + k[1]
        if not(0<=ni<n and 0<=nj<n):
            continue

        elif arr[ni][nj] == 1:
            continue

        elif visited[ni][nj] == 1:
            continue

        else:
            s = ni,nj
            bt(s,e)


    if visited[ei][ej] == 1:
        return 1

    else:
        return 0





print(bt(s,e))


# def bt(s,e):
#     i = s[0]
#     j = s[1]
#     if s == e:
#         return 1
#     for k in dir:
#         ni = i + k[0]
#         nj = j + k[1]
#
#         while 0 <= ni < n and 0<= nj < n:
#             if arr[ni][nj] == 1:
#                 break
#
#             else:
#                 s = ni,nj
#                 if s == e:
#                     return 1
#                 bt(s,e)
#     return 0