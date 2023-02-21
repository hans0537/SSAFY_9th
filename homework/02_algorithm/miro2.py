from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sx, sy):
    q = deque()
    q.append((sx, sy))
    visited = [[0] * 100 for _ in range(100)]
    # 지나간 길 처리
    visited[sx][sy] = 1

    while q:
        x, y = q.popleft()

        # 도착하면 종료
        if board[x][y] == '3':
            return 1

        # 4방향 탐색
        for d in range(4):
            mx = x + dx[d]
            my = y + dy[d]

            if 0 <= mx < 100 and 0 <= my < 100 and board[mx][my] != '1' and not visited[mx][my]:
                visited[mx][my] = 1
                q.append((mx, my))

    return 0

for tc in range(1, 11):
    input()
    board = []
    sx = sy = 0
    for i in range(100):
        tmp = list(input())
        for j in range(100):
            if tmp[j] == '2':
                sx = i
                sy = j
        board.append(tmp)

    print(f'#{tc} {bfs(sx, sy)}')