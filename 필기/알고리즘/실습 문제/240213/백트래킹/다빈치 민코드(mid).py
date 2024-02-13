N,M = map(int,input().split())

nums = sorted(list(map(int,input().split())))

result = []
min_v = float('inf')
def cod(nums,cnt=0, rst = 1,stack = []):
    global min_v
    global result
    if len(set(stack)) == 3:
        # if stack in result:
        #     stack.pop()
        #     cnt -= 1
        #     pass
        # if rst>min_v:
        #     stack.pop()
        #     pass
        if rst < min_v:
            min_v = rst
            cnt = 0
            if result == []:
                result.append(stack)
                pass
            else:
                result.pop()
                result.append(stack)
            stack = []

    for num in nums:
        if num in stack:
            continue
        else:
            stack.append(num)
            cod(nums,cnt+1,rst*num,stack)

a = cod(nums)

print(result)