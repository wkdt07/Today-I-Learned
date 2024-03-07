# 아래 함수를 수정하시오.
def sort_tuple(a):
    new_tuple = ()
    # new_list = []
    # b = list(a)
    # b.sort()
    # for i in b:
    #     new_list.append(i)
    #     # extend 쓰면 iterable에 들어있는거 싹 다 넣을 수 있음
    # new_tuple = tuple(new_list)
    # return new_tuple
    new_list = []
    new_list.extend(a)
    
    new_list.sort()
    new_tuple = tuple(new_list)
    return new_tuple

    #new_list 안 쓰고 b=list(a), b.sort(), new_tuple = tuple(b) 로 해도 됨


result = sort_tuple((5, 2, 8, 1, 3))
print(result)
