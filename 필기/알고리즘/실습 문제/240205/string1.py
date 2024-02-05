T = int(input())

for t in range(1,T+1):
    str1 = input()
    str2 = input()

    print(f'#{t}',int(str1 in str2))