##<prob.1>

def min_cost(cost_list):

    min_cost = cost_list[0]
    for cost in cost_list[1:]: #굳이 0번부터 할 필요 없음
        if cost <= min_cost:
            min_cost = cost #갱신
    return min_cost

# 이 문제는 sort 써도 됨


## <prob.2>

def average_cost(cost_list):
    cost_count = 0.0
    cost_around = 0.0

    for cost in cost_list:
        cost_count += cost
        cost_around += 1.0
    
    return cost_count/cost_around


## <prob.3>

def check_user_id(user_data):
    list_id = list(user['user_id'])
    count = 0

    for id in list_id:
        count += 1
        if count <4 or count >= 16:
            return False
        else:
            return True
        


## <prob.7>

'''
# SHB

def tidy_up_company(email_list):
    dic = {}    
    for i in range(0,len(email_list)):
        count = 0
        for j in range(len(email_list)):
            if email_list[i] == email_list[j]:
                count+=1
        dic.setdefault(email_list[i],count)
    return dic
'''   


def tidy_up_company(email_list):
    result = {}
    for email in email_list:
        if result.get(email):
            result[email] += 1
        
        else:
            result[email] = 1
    return result


email_list1 = ['Koogle', 'Koogle', 'Maver']
print(tidy_up_company(email_list1))   # {'Koogle': 2, 'Maver': 1}

email_list2 = [
    'Koogle', 'Koogle', 'JCloud', 'Koogle', 'GaKao', 
    'School', 'Koogle', 'Maver', 'GaKao', 'Maver', 
    'Koogle', 'GaKao', 'School', 'GaKao', 'JCloud', 
    'School', 'GaKao', 'GaKao', 'Maver', 'Koogle'
]
print(tidy_up_company(email_list2))



### <prob.9>

'''
# SHB

def dec_to_bin(n):
    i = n // 2
    j = n % 2
    
    if n == 0:
        return '0'
    if n == 1:
        return '1'

    if i == 0:          
        return str(j)+str(i)
    else:     
        return dec_to_bin(i)+str(j)

'''

def dec_to_bin(n):

    if n<=1:
        return str(n)
    
    else:
        return dec_to_bin(n // 2)+str(n%2)
    

### <prob. 10>
    

'''
# SHB

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

이거보다 3~4배 어렵게 방향배열 나오는게  IM
'''
def is_position_safe(N, M, current):
    # dir = [(-1,0),(1,0),(0,-1),(0,1)] #방향 첫 번째 방법 튜플로

    d_row = [-1,1,0,0] # 행방향
    d_col = [0,0,-1,1] #열방향 # 2번째, 리스트로
    row,col = current
    
    if (0 <= row+d_row[M] < N) and (0 <= col+d_col[M] < N):
        return True
    else:
        return False


## <prob .11>
    
def get_final_position(N, matrix, move_list):
    d_row = [-1,1,0,0] 
    d_col = [0,0,-1,1]
    row = 0
    col = 0
    
    #1은 현재 위치. 이걸 찾아야 함
    for r in range(N):
        for c in range(N):
            if matrix[r][c] == 1:
                row = r
                col = c
                break #찾으면 브레이크, 반복문 탈출
    
    #움직이기 시작
    for move in move_list:
        row += d_row[move]
        col += d_col[move]

        #범위가 '하나라도' 넘어가면 None -> or
        if row <=0 or row >= N or col<0 or col>=N:
            return None

    return [row,col]    