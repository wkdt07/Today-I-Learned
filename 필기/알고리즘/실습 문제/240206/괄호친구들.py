nums = list(map(str,input()))

# for i in range(len(nums)):
#     if nums[i] == '[' or nums[i] == ']':
#         cnt_p.append(i)
#     elif nums[i] == '{' or nums [i] == '}':
#         cnt_m.append(i)
result = 0
for num in nums:
    if num == '[':
        i = nums.index('[')
        j = nums.index(']')
        a =''.join(nums[i+1:j])
        result += int(a)
        nums.remove('[')
        nums.remove(']')

    if num == '{':
        i = nums.index('{')
        j = nums.index('}')
        a = ''.join(nums[i + 1:j])
        result *= int(a)
        nums.remove('{')
        nums.remove('}')

print(result)