# 스도쿠

arr = [list(map(int,input().split())) for _ in range(9)]

target_lst = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            target_lst.append((i,j))

# 행 검사
# 열 검사
# 3*3 검사 -> 해당 좌표 확인


