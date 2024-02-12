n = int(input()) #전구 길이(len(lst))

lst = list(map(int, input().split()))

k = int(input())

def change(a):
    if a == 1:
        a = 0
        return a
    if a == 0 :
        a = 1
        return a
def switch(gen,num):
    if gen == 1:
        idx = num - 1
        while idx < n: # 최대 인덱스 확인
            lst[idx] = change(lst[idx])
            idx += num
        return lst
    i = 1
    if gen == 2:
        idx = num - 1
        while 0<=idx-i and idx+i <=n-1:
            if lst[idx-i] == lst[idx+i]:
                i += 1

            else:
                i -= 1
                for i in range(idx-i,idx+i+1):
                    lst[i] = change(lst[i])
                return lst
        i -= 1
        for i in range(idx - i, idx + i + 1):
            lst[i] = change(lst[i])
        return lst

for _ in range(k):
    gen, num = map(int, input().split())
    switch(gen,num)

# 출력 주의
if n> 20:
    s = 0
    e = 20
    while e<=n:
        print(*lst[s:e])
        s = e
        e += 20
    if e>n:
        print(*lst[s:n+1])

else:
    print(*lst)

