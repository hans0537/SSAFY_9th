from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    global ans
    while water:
        x, y = water.popleft()

        for d in range(4):
            mx = x + dx[d]
            my = y + dy[d]

            if 0 <= mx < N and 0 <= my < M and visited[mx][my] == -1:
                water.append((mx, my))
                visited[mx][my] = visited[x][y] + 1
                ans += visited[mx][my]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    ans = 0
    visited = [[-1] * M for _ in range(N)]
    # 물인 곳인 좌표들을 큐에 저장하여 모든 좌표를 동시에 bfs를 돌리기 위
    water = deque()

    for i in range(N):
        tmp = list(input())
        for j in range(M):
            if tmp[j] == 'W':
                water.append((i, j))
                visited[i][j] = 0   # 물인곳은 거리가 0

    bfs()
    print('#{} {}'.format(tc, ans))
