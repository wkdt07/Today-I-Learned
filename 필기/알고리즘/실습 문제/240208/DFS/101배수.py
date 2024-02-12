
'''
입력
3
22 79 21
'''

'''
출력
22*79-21
22+79*21
'''

N = int(input()) #3 -> len(X)
X = list(map(int, input().split())) #[22,79,21]


def find101(n, x, ans = '', idx = 0, result = 0):
    if idx == 0:
        ans = str(x[0])  # '22'
        result = x[0] # 22 # ans와 result에 초기값 넣기
        find101(n, x, ans, idx+1, result)

    if idx == n:
        if result % 101 == 0 and result != 0:
            print(ans)
        return # 여기서 끝내는게 모든 함수에서 다 끝나는게 아니라 해당 노드를 끝내는 것, 함수가 계속 트리 된다는 걸 생각.

    # 만약 if 문에서 True가 아니면 아래 내용들이 이어진다. idx가 n이 될 때까지
    find101(n, x, ans + '*' + str(x[idx]), idx + 1, result * x[idx]) # 1) 곱하기
    find101(n, x, ans + '+' + str(x[idx]), idx + 1, result + x[idx]) # 2) 더하기
    find101(n, x, ans + '-' + str(x[idx]), idx + 1, result - x[idx]) # 3) 빼기

find101(N, X)