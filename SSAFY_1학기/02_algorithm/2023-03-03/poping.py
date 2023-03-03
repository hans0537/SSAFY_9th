from collections import deque
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]
def bfs(s, e):
    global cnt
    q = deque()
    q.append((s, e))
    visited[s][e] = 1
    cnt += 1

      while q:
        x, y = q.popleft()

        tmp = 0
        for d in range(8):
            mx = x + dx[d]
            my = y + dy[d]

            if 0 <= mx < N and 0 <= my < N and not visited[mx][my]:
                if arr[mx][my] == '*':
                    tmp += 1
                else:
                    visited[mx][my] = 1
                    q.append((mx, my))
        arr[x][y] = tmp


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    # 클릭 가능한 자리 저장 배열
    lst = deque()
    for i in range(N):
        for j in range(N):
            # if arr[i][j] == '*':
            #     visited[i][j] = -1
            if arr[i][j] == '.':
                lst.append((i, j))

    cnt = 0
    s, e = lst.popleft()
    bfs(s, e)