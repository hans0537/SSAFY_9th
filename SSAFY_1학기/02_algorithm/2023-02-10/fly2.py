T = int(input())

def colrow(board):
    maxV = 0
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for x in range(N):
        for y in range(N):
            tmp = board[x][y]
            for k in range(M - 1):
                for d in range(4):
                    mx = x + dx[d] * (k + 1)
                    my = y + dy[d] * (k + 1)

                    if 0 <= mx < N and 0 <= my < N:
                        tmp += board[mx][my]
            if maxV < tmp:
                maxV = tmp
    return maxV
def xshape(board):
    maxV = 0
    # 좌상, 좌하, 우상, 우하
    dx = [-1, 1, -1, 1]
    dy = [-1, -1, 1, 1]
    for x in range(N):
        for y in range(N):
            tmp = board[x][y]
            for k in range(M - 1):
                for d in range(4):
                    mx = x + dx[d] * (k + 1)
                    my = y + dy[d] * (k + 1)

                    if 0 <= mx < N and 0 <= my < N:
                        tmp += board[mx][my]
            if maxV < tmp:
                maxV = tmp
    return maxV

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    ans = max(colrow(board), xshape(board))
    print(f'#{tc} {ans}')