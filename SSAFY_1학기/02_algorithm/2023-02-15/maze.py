dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, n):
    global ans

    visited[x][y] = 1
    if maze[x][y] == 3:
        ans = 1
        return

    for d in range(4):
        mx = x + dx[d]
        my = y + dy[d]

        if 0 <= mx < n and 0 <= my < n and maze[mx][my] != 1 and not visited[mx][my]:
            dfs(mx, my, n)

T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    maze = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    ans = 0

    for i in range(N):
        tmp = input()
        for j in range(N):
            if int(tmp[j]) == 2:
                x = i
                y = j
            if int(tmp[j]) == 1:
                visited[i][j] == 1
            maze[i][j] = int(tmp[j])

    dfs(x, y, N)
    print(f'#{tc} {ans}')


