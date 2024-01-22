# 아래 함수를 수정하시오.
def remove_duplicates(lst):
    new_lst = []
    for i in lst:
        if lst.count(i)>1:
            lst.remove(i)
        
    new_lst = lst
    return new_lst


result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)





# L = [1,2,2,3,4,5]

# # for i in L:
# #     if L.count(i)>1:
# #         L.remove(i)
# #         new_list = L


# # print(new_list)
# new_list = []

# # new_list.append(L.pop())
# print(new_list)


# for i in L:
    
#     if L.count(i)==1:
#         new_list.append(L.pop(i))

#     elif L.count(i)>1:
#         new_list.append(L.pop(i))
    
# print(new_list)
  