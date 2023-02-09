T = int(input())
for tc in range(1, T + 1):
    sudo = []
    check = True
    # 입력을 받을때 가로줄을 동시에 체크한다.
    # 통과 못하면 check를 false로 하고 출력후 종료
    for _ in range(9):
        tmp = list(map(int, input().split()))
        if len(set(tmp)) != 9:
            check = False
            break
        sudo.append(tmp)

    # 가로가 검증이 되었으면
    if check:
        # 세로 검증
        for i in range(9):
            tmp = []
            for j in range(9):
                tmp.append(sudo[j][i])
            if len(set(tmp)) != 9:
                check = False
                break
        x = 0
        y = 0
        # 박스 검증
        while check:
            if y == 9:
                break
            tmp = []

            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    tmp.append(sudo[i][j])

            if len(set(tmp)) != 9:
                check = False

            if x == 6:
                x = 0
                y += 3
            else:
                x += 3

    if check:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
