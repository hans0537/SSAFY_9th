from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(s, e):
    global ans
    q = deque()
    visited = [[0] * N for _ in range(N)]
    q.append((s, e))
    visited[s][e] = 1

    while q:
        x, y = q.popleft()

        if visited[x][y] >= N - N//2:
            break

        for d in range(4):
            mx = x + dx[d]
            my = y + dy[d]

            if 0 <= mx < N and 0 <= my < N and not visited[mx][my]:
                ans += arr[mx][my]
                visited[mx][my] = visited[x][y] + 1
                q.append((mx, my))

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    arr = [list(map(int, list(input()))) for _ in range(N)]

    s = e = N // 2
    ans = arr[s][e]
    bfs(s, e)

    print('#{} {}'.format(tc, ans))