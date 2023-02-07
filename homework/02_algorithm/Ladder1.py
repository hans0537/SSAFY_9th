for tc in range(1, 11):
    input()
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 위에서 아래로 가는것보단 아래에서 위로 찾아 가는것이 더 효과적이다.
    # 좌 우 상
    dx = [0, 0, -1]
    dy = [-1, 1, 0]

    x = 99
    y = 0
    # 끝에서 2인 좌표를 찾아 좌표 설정
    for i in range(100):
        if ladder[99][i] == 2:
            y = i
            break

    while True:
        if x == 0:
            break
        
        for i in range(3):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or mx >= 100 or my < 0 or my >= 100:
                continue
            
            if ladder[mx][my]:
                ladder[mx][my] = 0
                x = mx
                y = my
                break
    print(f'#{tc} {y}')