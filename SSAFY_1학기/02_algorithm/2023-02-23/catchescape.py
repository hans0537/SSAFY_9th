from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def passCheck(d, next):
    if d == 0 and (next == 3 or next == 4 or next == 7):
        return False
    elif d == 1 and (next == 3 or next == 5 or next == 6):
        return False
    elif d == 2 and (next == 2 or next == 6 or next == 7):
        return False
    elif d == 3 and (next == 2 or next == 4 or next == 5):
        return False
    return True

def direction(d):
    if d == 1:
        return [0, 1, 2, 3]
    elif d == 2:
        return [0, 1]
    elif d == 3:
        return [2, 3]
    elif d == 4:
        return [0, 3]
    elif d == 5:
        return [1, 3]
    elif d == 6:
        return [1, 2]
    elif d == 7:
        return [0, 2]

def bfs(r, c):
    global ans
    q = deque()
    visited = [[0] * M for _ in range(N)]
    q.append((r, c))
    visited[r][c] = 1
    time = 1

    while q:
        x, y = q.popleft()

        for d in direction(board[x][y]):
            mx = x + dx[d]
            my = y + dy[d]

            if 0 <= mx < N and 0 <= my < M and not visited[mx][my] and board[mx][my] != 0 and passCheck(d, board[mx][my]):
                q.append((mx, my))
                visited[mx][my] = visited[x][y] + 1
                if visited[mx][my] <= L:
                    ans += 1

T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(N)]

    ans = 1
    bfs(R, C)
    print(f'#{tc} {ans}')
