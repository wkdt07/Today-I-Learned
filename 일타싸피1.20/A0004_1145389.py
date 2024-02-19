import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = 'SEOUL01_PYTHON'

# 일타싸피 프로그램을 로컬에서 실행할 경우 변경하지 않습니다.
HOST = '127.0.0.1'

# 일타싸피 프로그램과 통신할 때 사용하는 코드값으로 변경하지 않습니다.
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909


# 게임 환경에 대한 상수입니다.
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]

order = 0
balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

sock = socket.socket()
print('Trying to Connect: %s:%d' % (HOST, PORT))
sock.connect((HOST, PORT))
print('Connected: %s:%d' % (HOST, PORT))

send_data = '%d/%s' % (CODE_SEND, NICKNAME)
sock.send(send_data.encode('utf-8'))
print('Ready to play!\n--------------------')


while True:

    # Receive Data
    recv_data = (sock.recv(1024)).decode()
    print('Data Received: %s' % recv_data)

    # Read Game Data
    split_data = recv_data.split('/')
    idx = 0
    try:
        for i in range(NUMBER_OF_BALLS):
            for j in range(2):
                balls[i][j] = float(split_data[idx])
                idx += 1
    except:
        send_data = '%d/%s' % (CODE_REQUEST, NICKNAME)
        print("Received Data has been currupted, Resend Requested.")
        continue

    # Check Signal for Player Order or Close Connection
    if balls[0][0] == SIGNAL_ORDER:
        order = int(balls[0][1])
        print('\n* You will be the %s player. *\n' % ('first' if order == 1 else 'second'))
        continue
    elif balls[0][0] == SIGNAL_CLOSE:
        break

    # Show Balls' Position
    print('====== Arrays ======')
    for i in range(NUMBER_OF_BALLS):
        print('Ball %d: %f, %f' % (i, balls[i][0], balls[i][1]))
    print('====================')

    angle = 0.0
    power = 0.0

    ##############################
    # 이 위는 일타싸피와 통신하여 데이터를 주고 받기 위해 작성된 부분이므로 수정하면 안됩니다.
    #
    # 모든 수신값은 변수, 배열에서 확인할 수 있습니다.
    #   - order: 1인 경우 선공, 2인 경우 후공을 의미
    #   - balls[][]: 일타싸피 정보를 수신해서 각 공의 좌표를 배열로 저장
    #     예) balls[0][0]: 흰 공의 X좌표
    #         balls[0][1]: 흰 공의 Y좌표
    #         balls[1][0]: 1번 공의 X좌표
    #         balls[4][0]: 4번 공의 X좌표
    #         balls[5][0]: 마지막 번호(8번) 공의 X좌표

    # 여기서부터 코드를 작성하세요.
    # 아래에 있는 것은 샘플로 작성된 코드이므로 자유롭게 변경할 수 있습니다.

    def seta(v1,v2): # 두 점 사이 각도 -> 단위벡터 각도
        dot_v = dot(v1,v2)
        cos_v = dot_v/(length(v1)*length(v2))
        rad = math.acos(cos_v)
        return rad
        
      
    
    def length(A,B): # 벡터 길이
        x0,y0 = A
        x1,y1 = B
        return ((x1-x0)**2 + (y1-y0)**2)**(1/2)

    def dot(A,B):   # 내적
        x0,y0 = A
        x1,y1 = B
        return x0*x1+y0*y1

    def parvec(A,B):    #단위벡터 계산
        # x0,y0 = A
        # x1,y1 = B
        vec = B-A
        vec_1 = vec/length(A,B)
        return vec_1
    
    def path(start,end):
        def ball_dim(start,hole): # 칠 수 있는 공 판단
            x0,y0 = start
            x1,y1 = hole
            global ball_o
            for ball in balls[1:]:
                if dot(parvec(start,hole),parvec(start,ball))<=0: # 내적 값이 0보다 작거나 같으면 어차피 수직이거나 둔각이라 그 방향으로는 의미가 없다
                    continue
                else:
                    ball_o.append(ball)
            

        def hall_dim(start,hole): # 들어갈 수 있는 홀인지, 장애물 판단. 
            #각도를 통해서 직사각형 좌표 내에 존재하면 안 됨
            ball_o = ball_dim(start,hole)
            for ball in ball_o:
                seta1 = seta(start,ball) # 1구간 각도
                seta2 = seta(ball,hole) # 2구간 각도
                x0,y0 = start
                x1,y1 = ball
                xh,yh = hole

                while x0!=x1 and y0!=y1:
                    pass
    
                while x1!=xh and y0 != yh:
                    pass

        
    def min_hole(ball):
            length_lst = []
            for hole in HOLES:
                length_v = length(ball,hole)
                length_lst.append(length_v)
            min_length = min(length_lst)
            k = length_lst.index(min_length)
            return HOLES[k]
    
    def ball_dim(start,hole): # 칠 수 있는 공 판단
            x0,y0 = start
            x1,y1 = hole
            global ball_o
            for ball in balls[1:]:
                if dot(parvec(start,hole),parvec(start,ball))<=0: # 내적 값이 0보다 작거나 같으면 어차피 수직이거나 둔각이라 그 방향으로는 의미가 없다
                    continue
                else:
                    ball_o.append(ball)

    ball_d = 5.73
    ball_r = 2.865
    
    # Hole 보정
    HOLES = [[0+ball_r, 0+ball_r], [127, 0+ball_d/3], [254-ball_r, 0+ball_r], [0+ball_r, 127-ball_r], [127, 127-ball_d/3], [254-ball_r, 127-ball_r]]
    # HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]
    ball_o = []  
    
    # for hole in HOLES:
    #     ball_dim(balls[0],hole)
    
    # whiteBall_x = balls[0][0]
    # whiteBall_y = balls[0][1]
    # print(f'white = {whiteBall_x,whiteBall_y}')
        
    # targetBall_x = balls[1][0]
    # targetBall_y = balls[1][1]
    # print(f'target = {targetBall_x,targetBall_y}')


    # whiteBall_x, whiteBall_y: 흰 공의 X, Y좌표를 나타내기 위해 사용한 변수
    whiteBall_x = balls[0][0]
    whiteBall_y = balls[0][1]    

    

    # targetBall_x, targetBall_y: 목적구의 X, Y좌표를 나타내기 위해 사용한 변수
    # target_lst = []
    # for i in [1,3,5]:
        
    #     if balls[i][0] == -1 or balls[i][1] == -1:
    #         continue
    #     else:
    #         target_lst.append(i)
    
    # print(f'target = {target_lst}')
    # whiteBall_x = balls[0][0]
    # whiteBall_y = balls[0][1]
    # while balls[1] != (-1,-1): 
    #     # whiteBall_x = balls[0][0]
    #     # whiteBall_y = balls[0][1]
    #     print(f'white = {whiteBall_x,whiteBall_y}')
    targetBall_x = balls[1][0]
    targetBall_y = balls[1][1]
    if targetBall_x == -1:
        targetBall_x = balls[3][0]
        targetBall_y = balls[3][1]
        # print(f'target = {targetBall_x,targetBall_y}')

    # for ball in ball_o:
    #     targetBall_x,targetBall_y = ball
    
    # width, height: 목적구와 흰 공의 X좌표 간의 거리, Y좌표 간의 거리
        width = abs(targetBall_x - whiteBall_x)
        height = abs(targetBall_y - whiteBall_y)

        # radian: width와 height를 두 변으로 하는 직각삼각형의 각도를 구한 결과
        #   - 1radian = 180 / PI (도)
        #   - 1도 = PI / 180 (radian)
        # angle: 아크탄젠트로 얻은 각도 radian을 degree로 환산한 결과
        radian = math.atan(width / height) if height > 0 else 0
        angle = 180 / math.pi * radian
        
        # todo 이건 공 반지름이 포함 안된거라서 수정 필요
        # todo 타겟 볼을 변경하는 걸로 설정해야할 거 같다
        # 목적구가 흰 공과 상하좌우로 일직선상에 위치했을 때 각도 입력 
        if whiteBall_x == targetBall_x:
            if whiteBall_y < targetBall_y:
                angle = 0
            else:
                angle = 180
        elif whiteBall_y == targetBall_y:
            if whiteBall_x < targetBall_x:
                angle = 90
            else:
                angle = 270

        # 목적구가 흰 공을 중심으로 3사분면에 위치했을 때 각도를 재계산
        if whiteBall_x > targetBall_x and whiteBall_y > targetBall_y:
            radian = math.atan(width / height)
            angle = (180 / math.pi * radian) + 180
        
        # 목적구가 흰 공을 중심으로 4사분면에 위치했을 때 각도를 재계산
        elif whiteBall_x < targetBall_x and whiteBall_y > targetBall_y:
            radian = math.atan(height / width)
            angle = (180 / math.pi * radian) + 90

        print(f'angle = {angle}')    
        # distance: 두 점(좌표) 사이의 거리를 계산

        distance = math.sqrt(width**2 + height**2)

        # power: 거리 distance에 따른 힘의 세기를 계산
        power = distance * 0.5

        print(f'd and p = {distance,power}')
        print()
        targetBall_x = balls[1][0]
        targetBall_y = balls[1][1]
            
    


        # 구하는건 angle과 power


        # 주어진 데이터(공의 좌표)를 활용하여 두 개의 값을 최종 결정하고 나면,
        # 나머지 코드에서 일타싸피로 값을 보내 자동으로 플레이를 진행하게 합니다.
        #   - angle: 흰 공을 때려서 보낼 방향(각도)
        #   - power: 흰 공을 때릴 힘의 세기
        # 
        # 이 때 주의할 점은 power는 100을 초과할 수 없으며,
        # power = 0인 경우 힘이 제로(0)이므로 아무런 반응이 나타나지 않습니다.
        #
        # 아래는 일타싸피와 통신하는 나머지 부분이므로 수정하면 안됩니다.
        ##############################

        merged_data = '%f/%f/' % (angle, power)
        sock.send(merged_data.encode('utf-8'))
        print('Data Sent: %s' % merged_data)
    targetBall_x = balls[3][0]
    targetBall_y = balls[3][1]
    width = abs(targetBall_x - whiteBall_x)
    height = abs(targetBall_y - whiteBall_y)

    # radian: width와 height를 두 변으로 하는 직각삼각형의 각도를 구한 결과
    #   - 1radian = 180 / PI (도)
    #   - 1도 = PI / 180 (radian)
    # angle: 아크탄젠트로 얻은 각도 radian을 degree로 환산한 결과
    radian = math.atan(width / height) if height > 0 else 0
    angle = 180 / math.pi * radian
    
    # todo 이건 공 반지름이 포함 안된거라서 수정 필요
    # todo 타겟 볼을 변경하는 걸로 설정해야할 거 같다
    # 목적구가 흰 공과 상하좌우로 일직선상에 위치했을 때 각도 입력 
    if whiteBall_x == targetBall_x:
        if whiteBall_y < targetBall_y:
            angle = 0
        else:
            angle = 180
    elif whiteBall_y == targetBall_y:
        if whiteBall_x < targetBall_x:
            angle = 90
        else:
            angle = 270

    # 목적구가 흰 공을 중심으로 3사분면에 위치했을 때 각도를 재계산
    if whiteBall_x > targetBall_x and whiteBall_y > targetBall_y:
        radian = math.atan(width / height)
        angle = (180 / math.pi * radian) + 180
    
    # 목적구가 흰 공을 중심으로 4사분면에 위치했을 때 각도를 재계산
    elif whiteBall_x < targetBall_x and whiteBall_y > targetBall_y:
        radian = math.atan(height / width)
        angle = (180 / math.pi * radian) + 90

    print(f'angle = {angle}')    
    # distance: 두 점(좌표) 사이의 거리를 계산

    distance = math.sqrt(width**2 + height**2)

    # power: 거리 distance에 따른 힘의 세기를 계산
    power = distance * 0.5

    print(f'd and p = {distance,power}')
    print()
    targetBall_x = balls[1][0]
    targetBall_y = balls[1][1]
        



    # 구하는건 angle과 power


    # 주어진 데이터(공의 좌표)를 활용하여 두 개의 값을 최종 결정하고 나면,
    # 나머지 코드에서 일타싸피로 값을 보내 자동으로 플레이를 진행하게 합니다.
    #   - angle: 흰 공을 때려서 보낼 방향(각도)
    #   - power: 흰 공을 때릴 힘의 세기
    # 
    # 이 때 주의할 점은 power는 100을 초과할 수 없으며,
    # power = 0인 경우 힘이 제로(0)이므로 아무런 반응이 나타나지 않습니다.
    #
    # 아래는 일타싸피와 통신하는 나머지 부분이므로 수정하면 안됩니다.
    ##############################

    merged_data = '%f/%f/' % (angle, power)
    sock.send(merged_data.encode('utf-8'))
    print('Data Sent: %s' % merged_data)
   # ====================================================================         
    # else:
    #     for i in target_lst:
    #         whiteBall_x = balls[0][0]
    #         whiteBall_y = balls[0][1]
    #         print(f'white = {whiteBall_x,whiteBall_y}')
            
    #         white = balls[0]

    #         target = balls[i] #좌표

    #         hole = min_hole(target) #좌표

    #         vec_ht = [target[0]-hole[0],target[1]-hole[1]]
    #         vec_wt = parvec(white,target)
    #         end = tuple(target) - ball_d * tuple(vec_wt)



    #         targetBall_x = balls[i][0]
    #         targetBall_y = balls[i][1]
    #         print(f'target = {target}')

    #         end_x = end[0]
    #         end_y = end[1]
    #         print(f'end = {end}')
    #     # for ball in ball_o:
    #     #     targetBall_x,targetBall_y = ball
        
    #     # width, height: 목적구와 흰 공의 X좌표 간의 거리, Y좌표 간의 거리
    #         width = abs(end_x - whiteBall_x)
    #         height = abs(end_y - whiteBall_y)

    #         # radian: width와 height를 두 변으로 하는 직각삼각형의 각도를 구한 결과
    #         #   - 1radian = 180 / PI (도)
    #         #   - 1도 = PI / 180 (radian)
    #         # angle: 아크탄젠트로 얻은 각도 radian을 degree로 환산한 결과
    #         radian = math.atan(width / height) if height > 0 else 0
    #         angle = 180 / math.pi * radian
            
    #         # todo 이건 공 반지름이 포함 안된거라서 수정 필요
    #         # todo 타겟 볼을 변경하는 걸로 설정해야할 거 같다
    #         # 목적구가 흰 공과 상하좌우로 일직선상에 위치했을 때 각도 입력 
    #         if whiteBall_x == end_x:
    #             if whiteBall_y < end_y:
    #                 angle = 0
    #             else:
    #                 angle = 180
    #         elif whiteBall_y == end_y:
    #             if whiteBall_x < end_x:
    #                 angle = 90
    #             else:
    #                 angle = 270

    #         # 목적구가 흰 공을 중심으로 3사분면에 위치했을 때 각도를 재계산
    #         if whiteBall_x > end_x and whiteBall_y > end_y:
    #             radian = math.atan(width / height)
    #             angle = (180 / math.pi * radian) + 180
            
    #         # 목적구가 흰 공을 중심으로 4사분면에 위치했을 때 각도를 재계산
    #         elif whiteBall_x < end_x and whiteBall_y > end_y:
    #             radian = math.atan(height / width)
    #             angle = (180 / math.pi * radian) + 90
    #         # else:
    #         #     radian = math.atan(height/width)
    #         #     angle = (180/math.pi*radian)
    #         print(f'angle = {angle}')    
    #         # distance: 두 점(좌표) 사이의 거리를 계산

    #         distance = math.sqrt(width**2 + height**2)

    #         # power: 거리 distance에 따른 힘의 세기를 계산
    #         power = distance * 0.5

    #         print(f'd and p = {distance,power}')
    #         print()
            
    


    #     # 구하는건 angle과 power


    #     # 주어진 데이터(공의 좌표)를 활용하여 두 개의 값을 최종 결정하고 나면,
    #     # 나머지 코드에서 일타싸피로 값을 보내 자동으로 플레이를 진행하게 합니다.
    #     #   - angle: 흰 공을 때려서 보낼 방향(각도)
    #     #   - power: 흰 공을 때릴 힘의 세기
    #     # 
    #     # 이 때 주의할 점은 power는 100을 초과할 수 없으며,
    #     # power = 0인 경우 힘이 제로(0)이므로 아무런 반응이 나타나지 않습니다.
    #     #
    #     # 아래는 일타싸피와 통신하는 나머지 부분이므로 수정하면 안됩니다.
    #     ##############################

    #         merged_data = '%f/%f/' % (angle, power)
    #         sock.send(merged_data.encode('utf-8'))
    #         print('Data Sent: %s' % merged_data)

print(balls[0][0],balls[0],[1])
sock.close()
print('Connection Closed.\n--------------------')



# def seta(A,B): # 두 점 사이 각도 -> 단위벡터 각도
    #     x,y = parvec(A,B)
    #     vec = parvec(A,B)
    #     if x>=0 and y>= 0: # 1사분면

    #         result = math.atan(y/x)
    #         result = math.degrees(result)
    #         return result

    #     if x<0 and y>= 0: # 2사분면
    #         result = math.atan(y/x)
    #         result = math.degrees(result)
    #         return result

    #     if x<0 and y< 0: # 3사분면
    #         result = math.atan(y/x)
    #         result = math.degrees(result)
    #         return result

    #     if x>=0 and y < 0: # 4사분면
    #         result = math.atan(y/x)
    #         result = math.degrees(result)
    #         return result
