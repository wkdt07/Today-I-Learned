string = input()
stack = []

for s in string:
    if s not in '+-':
        stack.append(s)

    else:
        a = int(stack.pop())
        b = int(stack.pop())
        if s == '+':
            rst = b+a
            stack.append(rst)
        else:
            rst = b-a
            stack.append(rst)

result = stack.pop()
print(result)