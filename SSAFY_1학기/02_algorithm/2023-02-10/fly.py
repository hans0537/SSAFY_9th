T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0
    # 보드 크기와 파리채 크기를 뺀다
    # 즉 파리채가 보드를 훑을수 있는 인덱스 범위
    t = N - M + 1
    for i in range(t):
        for j in range(t):
            tmp = []
            for lst in board[i:i+M]:
                tmp += lst[j:j+M]
            tmp = sum(tmp)
            if maxV < tmp:
                maxV = tmp
    print(f'#{tc} {maxV}')