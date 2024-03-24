n = int(input())


# cnt => 해당 값이 n의 생성자인지 판단할 요소, 하나씩 늘려가며
for cnt in range(1,n+1):
    while cnt%10 != 0:
        cnt += cnt%10

    if cnt == n:
        print(cnt)
        break
    else:
        continue

