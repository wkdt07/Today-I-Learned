# # 아래 함수를 수정하시오.
def reverse_string(my_str):
    my_list = list(my_str)
    my_list.reverse()
    reverse_str = ''.join(my_list)
    # 리스트를 다시 str로 만들려면 str() 함수로 불가능
    return reverse_str

result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH



