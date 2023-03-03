from collections import deque
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]
def bfs(x, y):


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    # 클릭 가능한 자리 저장 배열
    lst = deque()
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '*':
                visited[i][j] = -1
            elif arr[i][j] == '.':
                lst.append((i, j))

    cnt = 0
    s, e = lst.popleft(0)
    bfs(s, e)