t = list(input().split('.'))

cnt = 1

for i in range(1,3):

    #월
    if i == 1 and len(t[i]) == 1:
        if t[i] == 'X':
            cnt += 9
    if i ==1 and len(t[i]) ==2:
        if t[i][1] == 'X' :
            cnt += 2

    # 일
    if 'X' not in t[1]:
        if i == 2 and len(t[i]) == 1:
            if t[i] == 'X':
                cnt += 9

        if i == 2 and len(t[i]) == 2:
            if t[i][1] == 'X':
                if t[i][0] == 'X':
                    if t[i][0] in range(0, 2):
                        cnt += 31

                else:
                    cnt += 9

            if t[i][0] == 'X' and t[i][1] != 'X':
                if t[i][1] in range(2):
                    cnt += 3
                else:
                    cnt += 2


    else:
        if i == 2 and len(t[i])==1:
            if t[i] == 'X':
                cnt *= 9

        if i == 2 and len(t[i])==2:
            if t[i][1] == 'X':
                if t[i][0] == 'X':
                    if t[i][0] in range(0,2):
                        cnt *= 31

                else:
                    cnt *= 9

            if t[i][0] =='X' and t[i][1] != 'X':
                if t[i][1] in range(2):
                    cnt *= 3
                else:
                    cnt *= 2

print(cnt)

