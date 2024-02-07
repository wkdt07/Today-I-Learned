
# pop한거랑 a[0] 같지 않으면?... AABB도 가능
# 강사님 -> 짝이 안 맞는 경우에도 일단 append 한다
T = int(input())

def check(txt):
    stack = []
    n = len(txt)
    if n % 2 != 0: # 갯수가 홀수일 경우는 신경 쓸 이유가 없음
        return 0

    for i in range(n):

        if len(stack) == 0:
            stack.append(txt[i])
            continue

        if stack[-1] == txt[i]:
            stack.pop()
        else:
            stack.append(txt[i])
            continue

    if len(stack) == 0:
        return 1
    else:
        return 0


result = 0
for t in range (1,T+1):
    txt  = input()
    result += check(txt)

print(result)


'''
for t in range(1, T + 1):
    text = input()
    stack = []

    for i in text:
        # 처음에 여는 괄호로 시작
        if i == '{' or i == '(':
            stack.append(i)

        # 닫는 괄호가 나온다 --> 짝이 맞는지 확인 -> 제거 -> pop

        elif stack and i == '}' and stack[-1] == '{':  # if stack? stack에 항이 있냐
            stack.pop()

        elif stack and i == ')' and stack[-1] == '(':
            stack.pop()

        # 닫는 괄호인데 짝이 맞지 않는다. -> 스택에 추가
        elif i == '}' or i == ')':
            stack.apppend(i)

    if stack:  # 스택에 남아있으면
        result = 0

    else:
        result = 1
'''




