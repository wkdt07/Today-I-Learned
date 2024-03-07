my_set = {'가', '나', (0, 0)}
my_dict = {
        '가': 1, 
        (0, 0): '튜플도 키값으로 사용가능'
    }

# 아래에 코드를 작성하시오.

for key in my_set:
    print(my_dict.get(key,'None'))

# var = [1,2,3,'a',(0,0,0)] 딕셔너리의 키로 가변 인자는 불가능

var = (1,2,3,'a',(0,0,0)) 

my_dict.setdefault(var,'변수로도 키 설정 가능')

print(my_dict)
