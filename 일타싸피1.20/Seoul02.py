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


    import math

##############################
# 이 위는 일타싸피와 통신하여 데이터를 주고 받기 위해 작성된 부분이므로 수정하면 안됩니다.
#
# 모든 수신값은 gameData에 들어갑니다.
#   - gameData.order: 1인 경우 선공, 2인 경우 후공을 의미
#   - gameData.balls[][]: 일타싸피 정보를 수신해서 각 공의 좌표를 배열로 저장
#     예) gameData.balls[0][0]: 흰 공의 X좌표
#         gameData.balls[0][1]: 흰 공의 Y좌표
#         gameData.balls[1][0]: 1번 공의 X좌표
#         gameData.balls[4][0]: 4번 공의 X좌표
#         gameData.balls[5][0]: 마지막 번호(8번) 공의 X좌표

# 여기서부터 코드를 작성하세요.
# 아래에 있는 것은 샘플로 작성된 코드이므로 자유롭게 변경할 수 있습니다.

# Vector 구현
    class Vector:
        def __init__(self, x, y):
            self.x = float(x)
            self.y = float(y)

        def __repr__(self):
            return f'{self.x:.10f}, {self.y:.10f}'

        @property
        def _comp(self):
            return (self.x, self.y)

        def __add__(self, other):
            return Vector(*(i + j for i, j in zip(self._comp, other._comp)))

        @property
        def norm(self):
            return sum(i * i for i in self._comp) ** (1 / 2)

        def dot(self, other):
            return sum(i * j for i, j in zip(self._comp, other._comp))

        def cross(self, other):
            return (self.x * other.y - self.y * other.x)

        def __neg__(self):
            return Vector(*(-i for i in self._comp))

        def __sub__(self, other):
            return self + (-other)

        def __mul__(self, other):
            if isinstance(other, Vector):
                return self.cross(other)
            return Vector(*(other * i for i in self._comp))

        def __rmul__(self, other):
            if isinstance(other, Vector):
                return self.cross(other)
            else:
                return self.__mul__(other)

        def __truediv__(self, other):
            return Vector(*(i / other for i in self._comp))


    # x 부터 y까지 가는 경로 계산하는 함수
    def path_find(x: Vector, y: Vector):
        def path_check(path: Vector, start, end):
            checkvec = end - start
            checkvec = checkvec / checkvec.norm
            cnt = 0
            for ball in objball + enemyball + [myball] + Myholes:
                checkball = ball - start
                if checkvec.dot(checkball) < 0:
                    continue
                if abs(checkvec.cross(checkball)) < 1.5 * Ball_r:
                    cnt += 1
                # print(cnt)
            print(start, end, cnt)
            if cnt > 2:
                return False
            return True

        path = y - x
        if path_check(path, x, y):
            return path
        return None


    Ball_stack = []
    Ball_r = 5.73 / 2
    Ball_R = 5.73
    W = 254
    H = 127
    # 일부러 홀의 위치를 보이기보다 약간 안쪽으로 잡아당겨줌
    # HOLES = [[0+Ball_r/4, 0+Ball_r/4], [127, 0+Ball_r/3], [254-Ball_r/4, 0+Ball_r/4], [0+Ball_r/4, 127-Ball_r/4], [127, 127-Ball_r/3], [254-Ball_r/4, 127-Ball_r/4]]

    const = 0.3
    k = Ball_r * const
    print(k)
    HOLES = [[0 + k, 0 + k], [127, 0 + k / 2], [254 - k, 0 + k], [0 + k, 127 - k], [127, 127 - k / 2], [254 - k, 127 - k]]
    Myholes = []
    for hole in HOLES:
        Myholes.append(Vector(*hole))
        # 홀 위치를 더 추가해서 정확도를 올리려했으나 실패?
        # for _ in range(20):
        #     seta = _*2*math.pi/20
        #     addvector = Vector(math.cos(seta),math.sin(seta))*Ball_r/10
        #     addvector = addvector/(2)
        #     Myholes.append(Vector(*hole) + addvector)

    # for

    # 내공
    myball = Vector(*gameData.balls[0])
    # 목적구
    objball = []
    # 상대구
    enemyball = []

    print(myball)
    # 공을 정리함 -> 목적구 2개가 안넣어졌으면 8볼은 상대목적구로 봄
    flag1 = False
    flag2 = False
    if gameData.order == 1:
        for idx, ball in enumerate(gameData.balls[1:]):
            # 목적구 2개가 다 끝났으면 True
            if ball == [-1.0, -1.0]:
                if idx == 0:
                    flag1 = True
                if idx == 2:
                    flag2 = True
                continue
            else:
                if idx == 0 or idx == 2:
                    objball.append(Vector(*ball))
                elif idx == 1 or idx == 3:
                    enemyball.append(Vector(*ball))
                elif idx == 4:
                    if flag1 and flag2:
                        objball.append(Vector(*ball))
                    else:
                        enemyball.append(Vector(*ball))
            # print(flag1,flag2)
    else:
        for idx, ball in enumerate(gameData.balls[1:]):
            # 목적구 2개가 다 끝났으면 True
            if ball == [-1.0, -1.0]:
                if idx == 1:
                    flag1 = True
                if idx == 3:
                    flag2 = True
                continue
            else:
                if idx == 1 or idx == 3:
                    objball.append(Vector(*ball))
                elif idx == 0 or idx == 2:
                    enemyball.append(Vector(*ball))
                elif idx == 4:
                    if flag1 and flag2:
                        objball.append(Vector(*ball))
                    else:
                        enemyball.append(Vector(*ball))

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



        # print(flag1,flag2)

# print(myball)
# print(objball)
# print(enemyball)

