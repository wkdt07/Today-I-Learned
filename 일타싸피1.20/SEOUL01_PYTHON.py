import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = 'A0004_1144946'


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
    
    # 전략
    # 먼저 타겟볼이 2개 이상 있을 때 order에 따라 목적구가 들어갔을 때(목적구가 -1이 되었을 때) 목적구를 바꿈
    # 그리고 목적구가 흰 공을 중심으로 1, 2사분면에 있을 때 각도들 추가
    # stage 4까지는 고정적으로 깰 수 있도록 power 및 angle 세부 조정
    # 흰공의 x값이나 y값이 목적구와 같을 때 각도를 조금 바꾸어 스테이지 6에서 계속 똑같은 각도로 치지 않게끔 바꿈
    # 시뮬레이션 통해 점수 획득


    def dot(A,B):   # 내적
        x0,y0 = A
        x1,y1 = B
        return x0*x1+y0*y1
    
    #shb
    ball_d = 5.73
    ball_r = 2.865
    HOLES = [[0+ball_r, 0+ball_r], [127, 0+ball_d/3], [254-ball_r, 0+ball_r], [0+ball_r, 127-ball_r], [127, 127-ball_d/3], [254-ball_r, 127-ball_r]]

    # whiteBall_x, whiteBall_y: 흰 공의 X, Y좌표를 나타내기 위해 사용한 변수
    whiteBall_x = balls[0][0]
    whiteBall_y = balls[0][1]

    def cross(A,B): # 벡터 외적
        x0,y0 = A
        x1,y1 = B
        return (x0*y1 - y0*x1)
    def length(A,B): # 벡터 길이
        x0,y0 = A
        x1,y1 = B
        return ((x1-x0)**2 + (y1-y0)**2)**(1/2)
    
    def path(white,target,HOLES):
        wx,wy = white
        tx,ty = target
        # global target_lst
        for hole in HOLES:
            hx,hy =hole
            vec_wt = (tx-wx,ty-wy)
            len_wt = length(vec_wt)
            vec_1_wt = vec_wt/len_wt
            vec_ht = (hx-tx,hy-ty)
            len_ht = length(vec_ht)
            vec_1_ht = vec_ht/len_ht

            if dot(vec_wt,vec_ht) <= 0:
                continue
            cnt = 0
            for e_ball in (enemy_ball + my_ball):
                if abs(cross(e_ball,hole)) < ball_d:
                    cnt += 1
            if cnt < 1:
                target_lst.append(target)
        
        return target_lst
            # for e_ball in (enemy_ball + my_ball):
            #     ex,ey = e_ball
            #     htx1 , hty1 = vec_1_ht
            #     wtx1, wty1 =vec_1_wt
            #     norm_ht = -hty1,htx1
            #     norm_wt = -wty1,wtx1
            #     for i in range(-ball_r,ball_r):
            #         if ex in (wx+i*









    visited = [False,False]
    white = whiteBall_x,whiteBall_y

    # targetBall_x, targetBall_y: 목적구의 X, Y좌표를 나타내기 위해 사용한 변수
    if order == 1:
        my_ball = [balls[1],balls[3]]
        enemy_ball = [balls[2],balls[4],balls[5]]
        target_lst = []
        for idx,ball in enumerate(my_ball):
            if ball[0] == -1 and ball[1] == -1:
                visited[idx] = True
            if visited.count(True) == 2:
                my_ball.append(balls[5])
        
        for ball in my_ball:
            target_lst = []
            if path(white,ball,HOLES):
                targetBall_x,targetBall_y = target_lst[0]
            else:
                targetBall_x,targetBall_y = 64,64
                break
                

        

        # targetBall_x = balls[1][0]
        # targetBall_y = balls[1][1]
        # if targetBall_x == -1:
        #     targetBall_x = balls[3][0]
        #     targetBall_y = balls[3][1]
        #     if targetBall_x == -1:
        #         targetBall_x = balls[5][0]
        #         targetBall_y = balls[5][1]

    if order == 2:
        # my_ball = [balls[2],balls[4],balls[5]]
        enemy_ball = [balls[1],balls[3],balls[5]]
        my_ball = [balls[2],balls[4]]
        target_lst = []
        for idx,ball in enumerate(my_ball):
            if ball[0] == -1 and ball[1] == -1:
                visited[idx] = True
        if visited.count(True) == 2:
            my_ball.append(balls[5])
        
        for ball in my_ball:
            target_lst = []
            if path(white,ball,HOLES):
                targetBall_x,targetBall_y = target_lst[0]  
            else:
                targetBall_x,targetBall_y = 64,64
                break
                
        
    
    
    


    # width, height: 목적구와 흰 공의 X좌표 간의 거리, Y좌표 간의 거리
    width = abs(targetBall_x - whiteBall_x)
    height = abs(targetBall_y - whiteBall_y)

    # radian: width와 height를 두 변으로 하는 직각삼각형의 각도를 구한 결과
    #   - 1radian = 180 / PI (도)
    #   - 1도 = PI / 180 (radian)
    # angle: 아크탄젠트로 얻은 각도 radian을 degree로 환산한 결과
    radian = math.atan(width / height) if height > 0 else 0
    angle = 180 / math.pi * radian
    
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

    # 목적구가 흰 공을 중심으로 1사분면에 위치했을 때 각도를 재계산
    elif whiteBall_x < targetBall_x and whiteBall_y < targetBall_y:
        radian = math.atan(width / height)
        angle = (180 / math.pi * radian)
    # 목적구가 흰 공을 중심으로 2사분면에 위치했을 때 각도를 재계산
    elif whiteBall_x > targetBall_x and whiteBall_y < targetBall_y:
        radian = math.atan(height / width)
        angle = (180 / math.pi * radian) + 270
        
    elif whiteBall_y == targetBall_y:
        radian = math.atan(height / width)
        angle = (180 / math.pi * radian) + 92
        
    else:
        radian = math.atan(width / height)
        angle = (180 / math.pi * radian) + 181
    # distance: 두 점(좌표) 사이의 거리를 계산
    distance = math.sqrt(width**2 + height**2)

    # power: 거리 distance에 따른 힘의 세기를 계산
    power = distance * 0.55







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

sock.close()
print('Connection Closed.\n--------------------')