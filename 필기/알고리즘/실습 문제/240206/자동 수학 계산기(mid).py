


# while (word[idx] != '+') or  (word[idx] != '-') or (idx != len(nums)):

nums = input()

result = 0

s,e = 0,1

while e != len(nums)-1:

    if e == len(nums)-2:
        e += 1
        if nums[s-1] == '+':
            result += int(nums[s:e])
        if nums[s-1] == '-':
            result -= int(nums[s:e])
    if nums[e] == '+':
        result += int(nums[s:e])
        s = e
        e += 1
    if nums[e] == '-':
        result -= int(nums[s:e])
        s = e
        e += 1
    e+=1
print(result)










# for num in nums:
#     if num == '+' or num == '-':
#         idx = nums.index(num)
#         result = int(nums[:idx])
#         break






'''
for i in range(len(nums)-1):
    temp = ''
    idx = i+1
    
    
    s,e = 0,0
    if nums[0] == 
    if nums[0] == '-':
   
    if nums[idx] == '+':
        while (idx != len(nums)-1)and (nums[idx+1]!='+') and (nums[idx+1]!='-'):
            temp += nums[idx+1]
            idx+=1
        result += int(temp)

    if nums[idx] == '-':
        while (nums[idx+1]!='+') and (nums[idx+1]!='-') and (idx != len(nums)-1):
            temp += nums[idx+1]
            idx += 1
        result -= int(temp)

print(result)
'''






'''
nums_temp = []
for num in nums:
    nums_temp.append(num)

result = 0
cnt = []
for num in nums_temp:
    if num == '+' or num == '-':
        cnt.append(nums.index(num))
        nums_temp.remove(num)

result = int(nums[:cnt[0]])

for num in nums:
    if num == '+' or num == '-':
        idx = nums.index(num)
        for i in range(idx+1,len(nums)):
            if nums[i] == '+' or nums[i] == '-':
                idx_e = i

        if num == '+':
            result += int(nums[idx+1:idx_e])

        if num == '-':
            result -= int(nums[idx + 1:idx_e])

'''

















#
#
# for i in range(len(cnt)-1):
#
#     if i == len(cnt)-1:
#         if nums[cnt[i]] == '+':
#             result += int(nums[cnt[i] + 1:len(nums)+1])
#
#         if nums[cnt[i]] == '-':
#             result -= int(nums[cnt[i] + 1:len(nums)+1])
#
#
#     if nums[cnt[i]] == '+':
#         result += int(nums[cnt[i]+1:cnt[i+1]])
#
#     if nums[cnt[i]] == '-':
#         result -= int(nums[cnt[i]+1:cnt[i+1]])
#
#
#
# print(result)