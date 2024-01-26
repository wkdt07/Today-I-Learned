def my_len(lst):
    count = 0
    for i in lst:
        count += 1
    
    return count

def my_sort(lst):
    for i in range(1, my_len(lst)):
        for j in range(my_len(lst)-1):
            if lst[i]>=lst[j]:
                pass
            elif lst[i]<lst[j]:
                lst[i],lst[j] = lst[j],lst[i]
    return lst

a = [100,-42,5,7,23,999,-999]
b = ['c','d','a','o','t']

print(my_sort(a))
print(my_sort(b))
        
