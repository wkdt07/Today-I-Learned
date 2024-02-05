# T = int(input())

# for t in range(1,T+1):
#     N= int(input())
#     arr = list(map(int,input().split()))
#     max_one = 0
#     for i in range(N-1):
#         count = 0
#         for j in range(i+1,N):
#             if arr[i] > arr[j]:
#                 count += 1
#         if max_one < count:
#             max_one = count
#     print(f'#{t} {max_one}')



'''
def gravity(T):
    for _ in range(1, T+1):
        N = int(input()) 
        arr = list(map(int, input().split()))
        max_v = 0  
        for i in range(N-1): 
            cnt = 0
            for j in range(i+1, N): 
                if arr[i] > arr[j]:
                    cnt += 1
                if max_v < cnt:
                    max_v = cnt
        print(f'#{_} {max_v}')
 
T = int(input())
 
gravity(T)

이런 식으로 하면 전역 변수 안 꼬이네...아예 T가 함수 밖에서 정의되는구나!
'''


T = int(input())

def gravity(boxes):
    max_v = 0
    for idx, box in enumerate(boxes): # 인덱스와 요소를 쌍으로 저장하는 메서드
        fall = 0
        for next in range(idx+1,N):
            if box > boxes[next]:
                fall += 1
        max_v =max(max_v,fall)
    return max_v

for tc in range(1,T+1):
    N = int(input())
    boxes = list(map(int,input().split()))
    result = gravity(boxes) #함수 호출에 breaking point
    print(f'#{tc} {result}')