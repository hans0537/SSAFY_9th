from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(s, e):
    global ans
    q = deque()
    q.append((s, e))
    visited = [[0] * N for _ in range(N)]
    visited[s][e] = 1

    home_cnt = 0
    # 만약 시작 위치에 집이 있으면
    # 집이 1개 k = 1 인 경우 처리
    if city[s][e] == 1:
        home_cnt += 1
        if home_cnt * M - 1 >= 0:
            ans = max(ans, home_cnt)

    while q:
        x, y = q.popleft()

        for d in range(4):
            mx = x + dx[d]
            my = y + dy[d]

            if 0 <= mx < N and 0 <= my < N and not visited[mx][my]:
                # 방문 했을때 영역안에 집이 있으면 집 개수 늘린후
                if city[mx][my] == 1:
                    home_cnt += 1
                q.append((mx, my))
                visited[mx][my] = visited[x][y] + 1
                k = visited[mx][my]

        # k 영역 방향 탐색하면서 운영비용 검색하면서
        # 손해가 아닐시 정답 변수 최신화
        if home_cnt * M - (k*k + (k-1)*(k-1)) >= 0:
            ans = max(ans, home_cnt)

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    # 모든 위치에서 서비스 영역 넓히기 BFS 실행
    for s in range(N):
        for e in range(N):
            bfs(s, e)

    print(f'#{tc} {ans}')