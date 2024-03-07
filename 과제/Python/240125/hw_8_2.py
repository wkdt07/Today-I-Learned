# 아래 함수를 수정하시오.
def check_number():
    # num = int(input('숫자를 입력하세요 : ')
    try:
        # num = int(input('숫자를 입력하세요 : ')) #이게 이 안에 있어야 함. 그래야 ValueError 나면 except로 감.
        num = float(input('숫자를 입력하세요 : ')) #float으로 안 하면 1.0 오류.
        if num > 0:    
            print('양수입니다.')
        
        elif num == 0:
            print('0입니다.')

        elif num < 0 :
            print('음수입니다.')
    except ValueError: 
        print('잘못된 입력입니다.')


check_number()
