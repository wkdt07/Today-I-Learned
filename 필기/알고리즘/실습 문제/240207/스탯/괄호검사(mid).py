T = int(input())

def check_1(string):
    stack = []

    try:
        for s in string:
            if s == '{' or s == '(':
                stack.append(s)
            if s == '}':
                k = stack.pop()
                if k == '{':
                    continue

                else:
                    return 0

            if s == ')':
                k = stack.pop()
                if k == '(':
                    continue

                else:
                    return 0
        if len(stack) != 0:
            return 0
        return 1
    except:
        return 0

for t in range(1,T+1):
    string = input()

    result = check_1(string)
    print(f'#{t} {result}')



