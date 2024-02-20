# 홀수 노드의 경우 완전이진트리라는 가정 하에 무조건 오른쪽 노드
# 그럼 이제 노드를 어떻게 분배할지가 문제
# LVR 탐색으로 차례대로 넣는다

T = int(input())

for t in range(1,T+1):
    N = int(input())
    if N%2 == 0:
        k = N//2
    else:
        k = N//2 + 1

    par = [0] * (N+1)
    left = [0] *(k+1)
    right = [0] *k


