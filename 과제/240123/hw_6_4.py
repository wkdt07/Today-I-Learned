# 아래 함수를 수정하시오.
def add_item_to_dict(dictionary,a,b):
    new_dict = dictionary.copy()

    # result = new_dict.setdefault(a,b) #이러면 반환값이 추가되는 value 뿐이다 #USA
    new_dict.setdefault(a,b)
    result = new_dict
    return result


my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)
