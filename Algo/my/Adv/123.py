direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def dfs(pho, moved, val, previous):
    global arr, jjols
    cy, cx = pho
    py, px = previous
    if moved == 3:
        arr[py][px] = 2
        arr[cy][cx] = val
        return
    for dy, dx in direction:
        met_jjol = False
        for i in range(1, N):
            ny = cy + i * dy
            nx = cx + i * dx
            if ny < 0 or N <= ny or nx < 0 or N <= nx:
                break
            if arr[ny][nx] == 1 and not met_jjol:
                met_jjol = True
                continue
            if met_jjol:
                arr[cy][cx] = 0
                arr[ny][nx] = 2
                if arr[ny][nx] == 1:
                    jjols.add((ny, nx))
                    dfs((ny, nx), moved + 1, 1, (cy, cx))
                    break
                else:
                    dfs((ny, nx), moved + 1, 0, (cy, cx))
    arr[py][px] = 2
    arr[cy][cx] = val


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    jjols = set()
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                dfs((i, j), 0, 0, (0, 0))
    print(f'#{tc} {len(jjols)}')
