############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 리스트 메서드 .count()를 사용하지 않습니다.
def find_solo(number_list):
    dic = tidy_up_company(number_list)
    for key in dic:
        if dic[key] == 1:
            return key

    # 여기에 코드를 작성하여 함수를 완성합니다.
    
def tidy_up_company(email_list):
    dic = {}    
    for i in range(0,len(email_list)):
        count = 0
        for j in range(len(email_list)):
            if email_list[i] == email_list[j]:
                count+=1
        dic.setdefault(email_list[i],count)
    return dic


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
number_list1 = [64, 27, 71, 27, 64]
print(find_solo(number_list1))  # 71
number_list2 = [4, 14, 60, 14, 49, 49, 78, 60, 78]
print(find_solo(number_list2))  # 4
#####################################################
