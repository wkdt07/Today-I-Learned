a = [1,2,100,4,5]

def my_max(lst):
    max_one = lst[0]
    for i in lst:
        if max_one <= i:
            max_one = i
        
        # else:
        #     continue
    
    return max_one

print(my_max(a))
