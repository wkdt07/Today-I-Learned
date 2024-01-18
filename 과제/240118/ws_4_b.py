food_list = [
    {
        '종류': '한식',
        '이름': '잡채'
    },
    {
        '종류': '채소',
        '이름': '토마토'
    },
    {
        '종류': '중식',
        '이름': '자장면'
    },
]


for food in food_list:
    if food['이름'] == '토마토':
        food['종류'] = '과일'
        print(f"{food['이름']} 은/는 {food['종류']}이다.")
    
    elif food['이름'] == '자장면':
        print('자장면엔 고춧가루지')
        print(f"{food['이름']} 은/는 {food['종류']}이다.")
    
    else: 
        print(f"{food['이름']} 은/는 {food['종류']}이다.")

print(food_list)