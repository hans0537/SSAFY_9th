T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # 네방향 0으로 패딩해서 둘러쌈
    # 범위 초과를 굳이 안하려는 동작
    board = [[0] * (N + 2) for _ in range(N + 2)]

    # 초기 돌 놓기
    board[N // 2 + 1][N // 2 + 1] = board[N // 2][N // 2] = 2
    board[N // 2 + 1][N // 2] = board[N // 2][N // 2 + 1] = 1

    # 흑돌 백돌 입력 받아서 처리
    for i in range(M):
        si, sj, p = map(int, input().split())
        board[si][sj] = p
        # 8방향 탐색
        for di, dj in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
            # 해당 방향으로 뻗어나가면서 처리
            tlst = []
            for mul in range(1, N):
                ni, nj = si + di * mul, sj + dj * mul
                if board[ni][nj] == 0:  # 빈칸 이거나 범위 밖
                    break
                elif board[ni][nj] != p:  # 다른 돌인 경우 뒤집기 후보에 추가
                    tlst.append((ni, nj))
                else:
                    while tlst:  # 같은 돌을 만나면 흰돌들 뒤집기
                        ti, tj = tlst.pop()
                        board[ti][tj] = p
                    break
    bcnt = wcnt = 0
    for lst in board:
        bcnt += lst.count(1)
        wcnt += lst.count(2)
    print(f'#{tc} {bcnt} {wcnt}')
