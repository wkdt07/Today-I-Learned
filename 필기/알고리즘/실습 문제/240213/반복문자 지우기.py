T = int(input())


for t in range(1,T+1):
    words = input()
    stack = [words[0]]
    for w in words[1:]:
        if stack == []:
            stack.append(w)
            continue
        top = stack.pop()
        if w != top:
            stack.append(top)
            stack.append(w)
        else:
            continue
    print(f'{t}',len(stack))