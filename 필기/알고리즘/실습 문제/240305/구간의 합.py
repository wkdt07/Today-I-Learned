N,target = map(int,input().split())

lst = list(map(int,input().split()))

sum_v = 0

low = 0
high = 0

cnt = 0
while True:
    if sum_v >= target or high == N:
        sum_v -= lst[low]
        low += 1

    elif sum_v<target:
        sum_v += lst[high] # 실질적으로 값을 더하는건 high
        high += 1
# 어차피 우연에 의해 sum_v가 완전히 target과 같아졌다 해도 이 밑에서 한 번 세주는거라 첫 번째 if문에 sum_v>=target이라도 상관이 없음
    if sum_v == target:
        cnt += 1

    if low == N:
        break

print(cnt)





