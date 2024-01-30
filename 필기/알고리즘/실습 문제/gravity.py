'''
9
7 4 2 0 0 6 0 7 0
'''

N = int(input()) # 상자가 쌓여있는 가로 길이
arr = list(map(int,input().split())) # 상자 갯수

# arr = input().split()
# print(arr) # ['7', '4', '2', '0', '0', '6', '0', '7', '0']

# 자기 오른쪽에서 자기보다 높은 애들 갯수만큼 낙차 거리가 줄어든다, 맨 윗 상자만 고려하면 됨

# => [7, 5, 4, 0, 0, 2, 0, 1, 0]
#max는 7 (x)

# 근데 리스트 굳이 만들 필요가 없다!

max_v = 0 # 문제에서 나올 수 있는 가장 초기화 값으로 놔라

# 낙차를 구하는 법? 구하고자 하는 상자의 인덱스로 접근(0~N-1)

for i in range(N-1): #i는 낙차 구하는 위치
    count = 0 #오른쪽에 있는 더 낮은 높이의 갯수
    for j in range(i+1,N):#j는 i와 비교하는 위치
        if arr[i] > arr[j]:
            count += 1
    if max_v <count: #최대낙차보다 크면
        max_v = count

print(max_v)

#강의 다시 봐라