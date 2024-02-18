# 두 정수가 같은 숫자로만 이루어져 있으면 친구
# set 쓰고 sort 하면 되겠는데

# friend가 아닌데 이웃한 숫자에 -1+1하거나 +1-1해서 친구이면 거의 친구. 이 때는 순서를 바꾸면 안된다.
# ex) 2223042와 123은 거의 친구, 137과 470은 아님 why? 맨 앞자리가 0이 되면 안됨

# x,y = map(int,input().split())
a = {1,2,3}
b = {1,4,5}
print(a-b)
try:
    while True:
        x,y = map(str,input().split())
        xset = set(map(int,x))
        yset = (map(int,y))
        xlst = sorted(list(xset))
        ylst = sorted(list(yset))
        if xlst == ylst:
            print('friends')
        else:
            for

                    print('almost friends')

                else:
                    print('nothing')




except:
    pass