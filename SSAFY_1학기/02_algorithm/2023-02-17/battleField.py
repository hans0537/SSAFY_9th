dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move(d):
    global tx, ty, td
    td = d
    mx = tx + dx[d]
    my = ty + dy[d]

    if 0 <= mx < H and 0 <= my < W and board[mx][my] == '.':
        board[tx][ty] = '.'
        if d == 0:
            board[mx][my] = '^'
        elif d == 1:
            board[mx][my] = 'v'
        elif d == 2:
            board[mx][my] = '<'
        elif d == 3:
            board[mx][my] = '>'
        tx = mx
        ty = my
    else:
        if d == 0:
            board[tx][ty] = '^'
        elif d == 1:
            board[tx][ty] = 'v'
        elif d == 2:
            board[tx][ty] = '<'
        elif d == 3:
            board[tx][ty] = '>'

def shoot(tx, ty, d):
    x = tx
    y = ty
    i = 0
    while True:
        mx = x + dx[d] * i
        my = y + dy[d] * i

        if 0 <= mx < H and 0 <= my < W and board[mx][my] != '#':
            if board[mx][my] == '*':
                board[mx][my] = '.'
                break
            i += 1
        else:
            break

T = int(input())
for tc in range(1, T + 1):
    H, W = map(int, input().split())
    board = []
    # 탱크의 좌표와 방향 정보
    tx = ty = td = 0
    for i in range(H):
        tmp = []
        line = input()
        for j in range(W):
            tmp.append(line[j])
            if line[j] == '<':
                tx = i
                ty = j
                td = 2
            elif line[j] == '>':
                tx = i
                ty = j
                td = 3
            elif line[j] == '^':
                tx = i
                ty = j
                td = 0
            elif line[j] == 'v':
                tx = i
                ty = j
                td = 1
        board.append(tmp)
    N = int(input())
    player = input()
    for i in player:
        if i == 'U':
            move(0)
        elif i == 'D':
            move(1)
        elif i == 'L':
            move(2)
        elif i == 'R':
            move(3)
        elif i == 'S':
            shoot(tx, ty, td)

    print(f'#{tc}', end=' ')
    for i in range(H):
        print(''.join(board[i]))