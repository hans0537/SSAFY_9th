for tc in range(1, 11):
    input()
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 위에서 아래로 가는것보단 아래에서 위로 찾아 가는것이 더 효과적이다.
    # 위 좌 우
    dx = [-1, 0, 0]
    dy = [0, -1, 1]
## 좌 우 상 
    x = 99
    y = 0
    # 끝에서 2인 좌표를 찾아 좌표 설정
    for i in range(100):
        if ladder[99][i] == 2:
            y = i

    while True:
        if x == 0:
            break

        if y - 1 >= 0 and ladder[x][y - 1]:
            while True:
                mx = x + dx[1]
                my = y + dy[1]
                if my >= 0 and ladder[mx][my] == 0:
                    break
                x = mx
                y = my
        elif y + 1 < 100 and ladder[x][y + 1]:
            while True:
                mx = x + dx[2]
                my = y + dy[2]
                if my < 100 and ladder[mx][my] == 0:
                    break
                x = mx
                y = my

        # 올라가기
        x += dx[0]
        y += dy[0]

    print(f'#{tc} {y}')