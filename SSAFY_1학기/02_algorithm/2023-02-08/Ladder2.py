import copy

for tc in range(1, 11):
    input()
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 좌 우 하
    dx = [0, 0, 1]
    dy = [-1, 1, 0]

    # 출발 리스트
    start_list = []

    for i in range(100):
        if ladder[0][i] == 1:
            start_list.append(i)

    minV = 1e9
    minIdx = 1e9
    for i in start_list:
        x = 0
        y = i

        tmp = 0
        tmpArr = copy.deepcopy(ladder)
        while True:
            if x == 99:
                break

            for j in range(3):
                mx = x + dx[j]
                my = y + dy[j]

                if mx < 0 or mx >= 100 or my < 0 or my >= 100:
                    continue

                if tmpArr[mx][my]:
                    tmpArr[mx][my] = 0
                    x = mx
                    y = my
                    tmp += 1
                    break
        if tmp < minV:
            minV = tmp
            minIdx = i

    print(f'#{tc} {minIdx}')
