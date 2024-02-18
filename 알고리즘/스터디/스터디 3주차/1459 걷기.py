# 집에 가는데 걸리는 최소시간 출력, 가로나 세로로 가거나, 대각선으로 가로질러 가는것
# w는 가로나 세로로 가는 시간, s는 대각선으로 가는 시간
# x,y 는 목표 지점, 현재 위치는 (0,0)
# 대각선은 (+1,+1), 나머지는 (0,+1), (0,-1)0*-
x, y, par_t, cross_t = map(int,input().split())

x_0,y_0 = 0,0
par = 0
cross = 0
dx = x - x_0
dy = y - y_0

if cross_t < 2* par_t:
    if dx>=dy:
        cross += dy
        y_0 += cross
        x_0 += cross
    else:
        cross += dx
        x_0 += cross
        y_0 += cross

    if x_0 == x and y_0 != y:
        dy = abs(y-y_0)
        k = dy % 2

        if dy * cross_t < dy*par_t:
            if not k:
                cross += dy
            else:
                cross += dy-1
                par += 1
        else:
            par += dy
        y_0 = y

    if x_0 != x and y_0 == y:
        dx = abs(x-x_0)
        l = dx % 2
        if dx * cross_t < dx*par_t:
            if not l:
                cross += dx
            else:
                cross += dx-1
                par += 1
        else:
            par += dx
        x_0 = x



else:
    par += abs(x-x_0) + abs(y-y_0)

print(cross*cross_t+par*par_t)



# if x_0 != x:
#     par += abs(x - x_0)
#
# if y_0 != y:
#     par += abs(y - y_0)

