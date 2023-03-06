dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for x in range(N):
        for y in range(M):
            tmp = arr[x][y]

            for i in range(1, tmp + 1):
                for d in range(4):
                    mx = x + dx[d] * i
                    my = y + dy[d] * i

                    if 0 <= mx < N and 0 <= my < M:
                        tmp += arr[mx][my]

            ans = max(tmp, ans)

    print('#{} {}'.format(tc, ans))