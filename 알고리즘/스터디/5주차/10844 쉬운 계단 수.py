# 마지막 자리가 9면 경우의 수가 8 하나밖에 안 나온다.
# 이전 자리가 0이라도 다음 경우의 수는 1 하나밖에 없다.
# 0갯수랑 9 갯수만큼 경우의수에서 마이너스
N = int(input())
if N == 1:
    print(9)

elif N == 2:
    print(17)

else:
    