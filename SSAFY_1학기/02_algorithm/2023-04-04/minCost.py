from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    q = deque()
    q.append((x, y))
    # 출발 위치는 0의 연료
    v[x][y] = 0

    while q:
        x, y = q.popleft()

        # 인접한 4방향 탐색
        for d in range(4):
            mx = x + dx[d]
            my = y + dy[d]

            if 0 <= mx < N and 0 <= my < N:
                # 일단 다음칸 넘어가는 연료를 저장후
                tmp = v[x][y] + 1
                # 다음 갈 곳이 높으면 차이 만큼 더해준다
                if arr[mx][my] > arr[x][y]:
                    tmp += arr[mx][my] - arr[x][y]

                # 다음칸에 갈 연료를 최소값을 갱신후 이동
                if tmp < v[mx][my]:
                    v[mx][my] = tmp
                    q.append((mx, my))


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    v = [[10000000] * N for _ in range(N)]
    bfs(0, 0)
    print('#{} {}'.format(tc, v[N-1][N-1]))