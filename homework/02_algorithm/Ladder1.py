for tc in range(1, 11):
    input()
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 위에서 아래로 가는것보단 아래에서 위로 찾아 가는것이 더 효과적이다.
    # 좌,우 의 우선순위가 높으니 먼저 탐색하기 위해 상을 맨마지막에
    # 좌 우 상
    dx = [0, 0, -1]
    dy = [-1, 1, 0]


    # 끝에서 2인 좌표(x, y) 를 찾아 좌표 설정
    x = 99
    y = 0
    for i in range(100):
        if ladder[99][i] == 2:
            y = i
            break
    
    while True:
        # 맨 위에 다다르면 종료
        if x == 0:
            break
        
        # 좌 -> 우 -> 상 순으로 체크
        for i in range(3):
            mx = x + dx[i]
            my = y + dy[i]

            # 범위를 벗어나면 패스
            if mx < 0 or mx >= 100 or my < 0 or my >= 100:
                continue
            
            # 좌 -> 우 -> 상 순으로 체크하여 1이면 이동
            if ladder[mx][my]:
                # 좌 또는 우로 다시 되돌아가는 것을 방지 하기 위해 지나간길 처리
                ladder[mx][my] = 0
                # 현재위치 변경
                x = mx
                y = my
                break
    print(f'#{tc} {y}')