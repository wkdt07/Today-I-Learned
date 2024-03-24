#K = K-(K&(K+1)) -> (K&(K+1))는 K의 가장 아래쪽 1을 반환함.K가 0이 되려면 1의 갯수만큼 연산하면 됨.


input()
print(input().count('1'))



## 51점
# N = int(input())
#
# K = int(input(),2)
#
# cnt = 0
# while K:
#     K = K - ( K & (~K+1) )
#     cnt += 1
#
# print(cnt)

