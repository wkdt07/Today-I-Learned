T = int(input())

for t in range(1,T+1):
    N = int(input()) # 들어가는 학생 수

    arr = []
    for _ in range(N):
        now,next = map(int,input().split())
        a = [now,next]
        a.sort()
        arr.append(a)
    # now와 next의 구분이 필요 없다. 어차피 경로는 하나로 똑같이 봐서
    arr.sort(key = lambda x:x[0])
    # print(arr)
    # vst = [0] * len(arr)
    # stack = 1
    cnt = 0

    while arr:
        stack = []
        end = 0
        for s,e in arr:

            if e - 1 == s:
                continue

            if s > end:

                end = e
                stack.append([s,e])

        for i in stack:
            arr.remove(i)


        cnt += 1

    print(f'#{t} {cnt}')