T = int(input())

def color(arr,i_s,j_s,i_f,j_f):
    for i in range(i_s,i_f+1):
        for j in range(j_s,j_f+1):
            if 0 <= i < 10 and 0 <= j < 10:
                arr[i][j] += 1
    return arr

for t in range(1,T+1):
    N = int(input())
    arr = list([0] * 10 for _ in range(10))
    # print(*arr)
    trial = [list(map(int,input().split())) for _ in range(N)]
    # print(*trial)
    for n in range(N):
        i_s,j_s = trial[n][0],trial[n][1]
        i_f,j_f = trial[n][2],trial[n][3]
        arr = color(arr,i_s,j_s,i_f,j_f)

    count = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j]==2:
                count += 1

    print(f'#{t} {count}')