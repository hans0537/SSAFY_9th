import sys

sys.stdin = open("algo2_sample_in.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    n = int(input())

    r, c = map(int, input().split())

    # 점수
    score = 0

    for i in range(n):
        # 두더지 정보
        a, b, k = map(int, input().split())

        # 두더지를 잡을수 있는지 확인 (거리 계산)
        # 잡을수 있으면 그냥 두더지 위치로 바로 이동
        if abs(a - r) + abs(b - c) <= k:
            score += 1
            r, c = a, b

        # 두더지를 잡을수 없으면 중간에 갈수있는 곳까지 이동
        # 1. 가로로 먼저 이동
        # 2. 세로로 이동
        else:
            move = k
            col_move = abs(b - c) if move > abs(b - c) else move
            if c > b:
                c -= col_move
            else:
                c += col_move
            move -= col_move
            if move > 0:
                if r > a:
                    r -= move
                else:
                    r += move

    print(f"#{tc} {score}")
