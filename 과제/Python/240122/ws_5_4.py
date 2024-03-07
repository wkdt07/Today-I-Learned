# 아래 함수를 수정하시오.

## title 안 쓰면?


# def capitalize_words(stri):
#     lst = stri.split()
    
#     lst_cap = [str_i.capitalize() for str_i in lst]
#     result = ' '.join(lst_cap) #sep에 공백 추가하면 리스트 요소 붙일 때 띄어쓰기 가능
#     return result

# result = capitalize_words("hello, world!")
# print(result)




def capitalize_words(stri):
    result = stri.title()
    return result

result = capitalize_words("hello, world!")
print(result)