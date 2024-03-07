data = [
    {
        'name': 'galxy flip',
        'company': 'samsung',
        'is_collapsible': True,
    },
    {
        'name': 'ipad',
        'is_collapsible': False
    },
    {
        'name': 'galxy fold',
        'company': 'samsung',
        'is_collapsible': True
    },
    {
        'name': 'galxy note',
        'company': 'samsung',
        'is_collapsible': False
    },
    {
        'name': 'optimus',
        'is_collapsible': False
    },
]

key_list = ['name', 'company', 'is_collapsible']

# 아래에 코드를 작성하시오.

for dic in data:
    for key in key_list:
        dic.setdefault(key,'unknown')
        a = dic.get(key)
        print(f'{key}은/는 {a}입니다.')
    print() #한 칸씩 띄어쓰기용    

# name은/는 galxy flip입니다.
# company은/는 samsung입니다.
# is_collapsible은/는 True입니다.
 
# name은/는 ipad입니다.
# company은/는 unknown입니다.
# is_collapsible은/는 False입니다.

# name은/는 galxy fold입니다.
# company은/는 samsung입니다.
# is_collapsible은/는 True입니다.

# name은/는 galxy note입니다.
# company은/는 samsung입니다.
# is_collapsible은/는 False입니다.

# name은/는 optimus입니다.
# company은/는 unknown입니다.
# is_collapsible은/는 False입니다.
