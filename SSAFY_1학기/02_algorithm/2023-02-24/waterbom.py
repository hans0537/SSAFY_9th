from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(si, sj):
    q = deque()
    visited = [[] * M for _ in range(N)]
    q.append((si, sj))
    visited[si][sj] = 1
    tmp = 1e9
    while q:
        x, y = q.popleft()

        if arr[x][y] == 'W':
            break

        for d in range(4):
            mx = x + dx[d]
            my = y + dy[d]

            if 0 <= mx < N and 0 <= my < M and not visited[mx][my]:
                q.append((mx, my))
                visited[mx][my] = visited[x][y] + 1

        tmp = min(tmp, visited[x][y])

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    ans = 0
    for si in range(N):
        for sj in range(M):
            if arr[si][sj] == 'L':
                bfs(si, sj)
