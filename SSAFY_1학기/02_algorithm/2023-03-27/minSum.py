from collections import deque

# def bfs():
#     q = deque()
#     # 왼쪽위 시작점부터
#     q.append((0, 0))
#     visited[0][0] = arr[0][0]
#
#     while q:
#         x, y = q.popleft()
#
#         for d in ((0, 1), (1, 0)):
#             mx = x + d[0]
#             my = y + d[1]
#
#             if 0 <= mx < N and 0 <= my < N:
#                 if visited[mx][my]:
#                     visited[mx][my] = min(visited[mx][my], visited[x][y] + arr[mx][my])
#                 else:
#                     visited[mx][my] = visited[x][y] + arr[mx][my]
#                 q.append((mx, my))

# def bfs(x, y, csum):
#     global ans
#
#     if (x, y) == (N - 1, N - 1):
#         ans = (ans, csum)
#         return
#
#     for d in ((0, 1), (1, 0)):
#         mx = x + d[0]
#         my = y + d[1]
#
#         if 0 <= mx < N and 0 <= my < N:
#             bfs(mx, my, csum + arr[mx][my])

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # visited = [[0] * N for _ in range(N)]
    # bfs()

    # 중간 위치 (i, j) 까지의 합을 다시 계산하지 않도록 저장
    dp = [[0] * N for _ in range(N)]

    # 이동방향이 왼쪽 => 오른쪽 or 위 => 아래
    for i in range(N):
        for j in range(N):
            # i, j 위치에서 위에서도 올 수 있고, 왼쪽에서도 올 수 있다
            if i - 1 >= 0 and j - 1 >= 0:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + arr[i][j]
            # 위에서만 올 수 있다
            elif i - 1 >= 0 and j - 1 < 0:
                dp[i][j] = dp[i - 1][j] + arr[i][j]
            # 왼쪽에서만 올 수 있다
            elif i - 1 < 0 and j - 1 >= 0:
                dp[i][j] = dp[i][j - 1] + arr[i][j]
            elif i - 1 < 0 and j - 1 < 0:
                dp[i][j] = arr[i][j]

    print('#{} {}'.format(tc, dp[N - 1][N - 1]))

    # print('#{} {}'.format(tc, visited[N - 1][N - 1]))
