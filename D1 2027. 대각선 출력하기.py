

for i in range(0,5):
    for j in range(0,5):
        a = []
        if i==j:
            a.append('#')
        else:
            a.append('+')
    print(a)