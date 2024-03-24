# 두 정수가 같은 숫자로만 이루어져 있으면 친구
# set 쓰고 sort 하면 되겠는데

# friend가 아닌데 이웃한 숫자에 -1+1하거나 +1-1해서 친구이면 거의 친구. 이 때는 순서를 바꾸면 안된다.
# ex) 2223042와 123은 거의 친구, 137과 470은 아님 why? 맨 앞자리가 0이 되면 안됨

# x,y = map(int,input().split())
import copy

def mp(n,i):
    nmp = copy.deepcopy(n)
    nmp[i] -= 1
    nmp[i+1] += 1
    return nmp

def pm(n,i):
    npm = copy.deepcopy(n)
    npm[i] += 1
    npm[i+1] -= 1
    return npm

def xy():
    for i in range(len(x)-1):
        nmp = mp(x,i)
        npm = pm(x,i)
        if nmp[0] != 0 and set(nmp) == yset:
            return True
        if npm[0] != 0 and set(npm) == yset:
            return True
    return False

def yx():
    for i in range(len(y)-1):
        nmp = mp(y,i)
        npm = pm(y,i)
        if nmp[0] != 0 and set(nmp) == xset:
            return True
        if npm[0] != 0 and set(npm) == xset:
            return True
    return False

try:
    while True:
        xt,yt = map(str,input().split())
        x = list(map(int,xt))
        y = list(map(int,yt))

        xset = set(x) # x의 구성요소
        yset = set(y) # y의 구성요소

        if xset == yset:
            print('friends')
        else:
            if xy() == True or yx() == True:
                print('almost friends')

            else:
                print('nothing')

except:
    pass