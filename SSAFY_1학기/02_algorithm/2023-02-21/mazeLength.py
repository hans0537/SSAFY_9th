dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sx, sc):
    # 방문 배열 생성
    visited = [[0] * N for _ in range(N)]
    q = []
    q.append((sx, sc))

    while q:
        x, y = q.pop(0)

        if maze[x][y] == '3':
            return visited[x][y]

        for d in range(4):
            mx = x + dx[d]
            my = y + dy[d]

            if 0 <= mx < N and 0 <= my < N and maze[mx][my] != '1' and not visited[mx][my]:
                q.append((mx, my))
                visited[mx][my] = visited[x][y] + 1
    return 1


T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    sx = sy = 0
    maze = []
    for i in range(N):
        tmp = input()
        for j in range(N):
            if tmp[j] == '2':
                sx = i
                sy = j
        maze.append(tmp)

    print(f'#{tc} {bfs(sx, sy) - 1}')
