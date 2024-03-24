nums = list(map(int, input().split()))
nums.sort()
max_v = nums[2]*nums[3]*nums[4]
def multi():
    for i in range(1,max_v+1):
        cnt = 0
        for num in nums:
            if i % num == 0:
                cnt += 1
            if cnt == 3:
                return(i)

print(multi())




'''nums = list(map(int, input().split()))

nums.sort()

max_v = nums[3]*nums[4] #아마 곱해지는 최대 값은 가장 큰 값 두개 곱한 것보단 작을 거다.


def cnt_func():
    for i in range(1, max_v + 1):
        for num1 in nums:
            cnt = 0
            for num2 in nums:
                if (num1 * i) % num2 == 0:
                    cnt += 1
                    if cnt == 3:
                        return(num1*i)

print(cnt_func())'''

'''(num1<=num2) and'''