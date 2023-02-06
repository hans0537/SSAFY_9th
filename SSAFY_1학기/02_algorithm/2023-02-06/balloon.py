T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    maxV = 0
    for x in range(N):
        for y in range(M):
            tmp = arr[x][y]
            for d in range(4):
                mx = x + dx[d]
                my = y + dy[d]
                if 0 <= mx < N and 0 <= my < M:
                    tmp += arr[mx][my]
            if maxV < tmp:
                maxV = tmp
    print(f'#{tc} {maxV}')