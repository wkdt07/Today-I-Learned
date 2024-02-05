############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.

def is_position_safe(N, M, current):
    arr = []
    for i in range(N):
        for j in range(N):
            arr.append([i,j])

    dp =[[0,-1],[0,1],[-1,0],[1,0]]
    dM = dp[M]
    current_lst = list(current)
    idx = arr.index(current_lst)
    a = True
    for i in range(2):

        if (arr[idx][i] + dM[i]<0):  
            a = False
            break
        elif  (arr[idx][i] + dM[i]>=(N-1)):
            a=False
            break
    return a

            

    # 여기에 코드를 작성하여 함수를 완성합니다.
    



# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(is_position_safe(3, 1, (0, 0))) # True
print(is_position_safe(3, 0, (0, 0))) # False
#####################################################
