a = [1,2,3,4,5]

def my_min(lst):
    # min_one = 0 #이거 0이면 그냥 0으로 튀어나와서 문제인데... 
    min_one = lst[0] #리스트 안에 있는 값을 넣으면 해결
    for i in lst:
        if min_one >= i:
            min_one = i
        else:
            continue


    return min_one

print(my_min(a))

