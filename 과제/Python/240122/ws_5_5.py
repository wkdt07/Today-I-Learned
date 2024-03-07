# 아래 함수를 수정하시오.


def even_elements(lst):
    even = []
    lst.sort(reverse = True)
    for i in range(len(lst)): #인덱스로 접근이 불가능함. pop 할 때 인덱스 갯수와 순서도 달라지고, lst.pop(i)해버리면 i가 lst보다 커져서 out of range 되어버림
        a = lst.pop()
        if a % 2 == 0:
            even.append(a)
        # if lst.pop() % 2 == 0:
        #     even.append(lst(pop()))
    result = []
    result.extend(even)
    return result


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)




'''

<잘못된 접근>

for i in range(len(lst)):
    if lst[i] % 2 == 0:
        a = lst.pop(i)
        even.append(a)

result.extend(even)


'''

""" 리스트 컴프리헨션으로 간단하게 가능

def even_lst(lst):
    result = [i for i in lst if i % 2 == 0]
    return result

my_list=[1,2,3,4,5,6,7,8,9,10]
print(even_lst(my_list))    

 """