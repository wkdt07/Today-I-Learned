'''2
7 2
65 66 81 86 65 71 82
8 2
65 65 81 66 65 65 69 69'''

T = int(input())

for t in range(1,T+1):
    N,R = map(int,input().split()) #N: 음식의 갯수, R = 팔의 길이
    arr = list(map(int,input().split()))
    # s = 0 # 초기값 설정
    # e = s + 2*R+1

    rst = 'YES' # 만약 통과하면 결과는 Yes

    for s in range(N):
        stack = []
        e = s+2*R+1
        # if e >= N:
        #     e -= N # 만약 팔의 크기가 2N을 넘어간다면?

        for i in range(s,e):
            while i >= N:
                i -= N

            stack.append(arr[i])
        # print(stack)

        for j in range(len(stack)):
            if stack.count(stack[j])>=3:
                rst = 'NO'

    print(f'#{t} {rst}')




