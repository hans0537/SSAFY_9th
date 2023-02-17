# 좌상 상 우상 우 우하 하 좌하 좌
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    land = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        for j in range(M):
            # 모서리에는 주변이 3개이므로 아애 탐색에서 제외
            if (i == 0 and j == 0) or (i == 0 and j == M - 1) or (i == N - 1 and j == 0) or (i == N - 1 and j == M - 1):
                continue

            # 8방향 탐색
            cnt = 0
            for d in range(8):
                mx = i + dx[d]
                my = j + dy[d]
                if 0 <= mx < N and 0 <= my < M and land[mx][my] < land[i][j]:
                    cnt += 1

            if cnt >= 4:
                ans += 1

    print(f'#{tc} {ans}')