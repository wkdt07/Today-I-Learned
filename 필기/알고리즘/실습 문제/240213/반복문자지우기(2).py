'''
T = int(input())

for t in range(1,T+1):
    words = input()
    stack = [words[0]]

    for word in words[1:]:
        if not stack:
            stack.append(word)
            continue
        w = stack.pop()
        if w == word:
            continue
        else:
            stack.append(w)
            stack.append(word)
    # k = ''.join(stack)
    print(f'#{t} {len(stack)}')
'''

T = int(input())

for t in range(1,T+1):
   str_lst = list(input())
   stack = []

   for char in str_lst:
      # 만약 반복 문자라면 pop() ---> stack이 비어있지 않고, char이 마지막 문자와 같다면

      if stack and char == stack[-1]:
         stack.pop()
      else:
         stack.append(char)

   print(f'{t} {len(stack)}')