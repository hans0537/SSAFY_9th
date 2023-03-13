import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = 'GWANGJU03_SHINSUNGJOO'

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

def initial_target():
    black_check = 0
    if order == 1:
        target_order = 1
        while True:
            if black_check == 2:
                target_order = 5
                break

            if balls[target_order][0] != -1.000000 or balls[target_order][1] != -1.000000:
                break
            target_order += 2
            black_check += 1
    else:
        target_order = 2
        while True:
            if black_check == 2:
                target_order = 5
                break

            if balls[target_order][0] != -1.000000 or balls[target_order][1] != -1.000000:
                break
            target_order += 2
            black_check += 1

    return target_order

def find_besthole(target_order):
    r = 0.573
    HOLES = [[r, r], [127 - r, r], [254 - r, r], [r, 127 - r], [127 - r, 127 - r], [254 - r, 127 - r]]

    # 목적구 x, y
    tx = balls[target_order][0]
    ty = balls[target_order][1]
    # 흰공 x, y
    wx = balls[0][0]
    wy = balls[0][1]

    for hx, hy in HOLES:
        # 1 사분면에 있을시 목표홀도 1사분면안에
        if wx < tx and wy < ty:
            if wx > hx or wy > hy:
                continue
            if tx < hx and hy > ty:
                return hx, hy
        # 2 사분면에 있을시 목표홀도 2사분면안에
        elif wx > tx and wy < ty:
            if wx < hx or wy > hy:
                continue
            if hx < tx and hy > ty:
                return hx, hy
        # 3 사분면에 있을시 목표홀도 3사분면안에
        elif wx > tx and wy > ty:
            if wx < hx or wy < hy:
                continue
            if hx < tx and hy < ty:
                return hx, hy
        # 4 사분면에 있을시 목표홀도 4사분면안에
        elif wx < tx and wy > ty:
            if wx > hx or wy < hy:
                continue
            if tx < hx and hy < ty:
                return hx, hy
    #
    return hx, hy

# 흰공이 도달해야 하는 좌표(즉 목적구를 때릴 곳)
def reach_p(hx, hy):
    # 목적구 x, y
    tx = balls[target_order][0]
    ty = balls[target_order][1]

    # # 목적구가 벽에 긍~~이 붙어 있을때
    # # 위에 붙어있을때
    # if TABLE_HEIGHT - ty < 5.73 / 2 + 0.5:
    #     if tx < hx and ty < hy:
    #         hx -= 5.73 / 2
    #         hy -= 5.73 / 2
    #     elif tx > hx and ty < hy:
    #         hx += 5.73 / 2
    #         hy -= 5.73 / 2
    # # 왼쪽 붙어있을때
    # elif tx < 5.73 / 2 + 0.5:
    #     if tx > hx and ty < hy:
    #         hx += 5.73 / 2
    #         hy -= 5.73 / 2
    #     elif tx > hx and ty > hy:
    #         hx += 5.73 / 2
    #         hy += 5.73 / 2
    # # 밑에 붙어있을때
    # elif ty < 5.73 / 2 + 0.5:
    #     if tx > hx and ty > hy:
    #         hx += 5.73 / 2
    #         hy += 5.73 / 2
    #     elif tx < hx and ty > hy:
    #         hx -= 5.73 / 2
    #         hy += 5.73 / 2
    # # 오른쪽에 붙어있을때
    # elif TABLE_WIDTH - tx < 5.73 / 2 + 0.5:
    #     if tx < hx and ty < hy:
    #         hx -= 5.73 / 2
    #         hy -= 5.73 / 2
    #     elif tx < hx and ty > hy:
    #         hx -= 5.73 / 2
    #         hy += 5.73 / 2
            
    # 흰공 x, y
    wx = balls[0][0]
    wy = balls[0][1]

    # 목표홀과 목적구사이의 거리
    dis = math.sqrt((hx - tx) ** 2 + (hy - ty) ** 2)

    radi = math.atan(abs(hx - tx) / abs(hy - ty))

    # 1,2,3,4 분면에 대해 좌표값 변경
    if wx < tx and wy < ty:
        return hx - (dis + 5.73)*math.sin(radi), hy - (dis + 5.73)*math.cos(radi)
    elif wx > tx and wy < ty:
        return (dis + 5.73)*math.sin(radi), hy - (dis + 5.73)*math.cos(radi)
    elif wx > tx and wy > ty:
        return (dis + 5.73)*math.sin(radi), (dis + 5.73)*math.cos(radi)
    elif wx < tx and wy > ty:
        return hx - (dis + 5.73)*math.sin(radi),(dis + 5.73)*math.cos(radi)

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

    #### 전략 ####
    '''
        stage1,2,3 은 기본 방향 대로 진행한 후
        그 이후 stage에 대해 
        만약 첫번째 공을 친 후에 다음 공을 칠시 목적구와 가장 적합한 목표 홀 을 찾아 
        목적구를 보낼 방향을 먼저 찾고
        그 방향에 대해 흰공이 가야할 좌표를 구한후
        그 좌표에 대해 각도를 구함   
    '''

    # 선공/후공에 따라 일단 가장 먼저 쳐야 할 공의 번호
    target_order = initial_target()
    
    # 다음 타겟 공을 칠 시 적합한 목표 홀에 대해 흰공이 도달해야 할 좌표 도출
    if target_order > 1:
        hx, hy = find_besthole(target_order)
        rx, ry = reach_p(hx, hy)

    # whiteBall_x, whiteBall_y: 흰 공의 X, Y좌표를 나타내기 위해 사용한 변수
    whiteBall_x = balls[0][0]
    whiteBall_y = balls[0][1]

    # targetBall_x, targetBall_y: 목적구의 X, Y좌표를 나타내기 위해 사용한 변수
    if target_order > 1:
        targetBall_x = rx
        targetBall_y = ry
    else:
        targetBall_x = balls[target_order][0] - (5.73 / 2) / 2
        targetBall_y = balls[target_order][1] - (5.73 / 2) / 2

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
        
    # distance: 두 점(좌표) 사이의 거리를 계산
    distance = math.sqrt(width**2 + height**2)

    # power: 거리 distance에 따른 힘의 세기를 계산
    if target_order == 1:
        power = distance * 50
    else:
        power = distance * 10

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