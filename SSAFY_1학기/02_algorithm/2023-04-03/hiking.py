T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < N and not v[nx][ny]

def dfs(cx, cy, cnt, cut):
    global ans

    # 상하좌우 탐색
    for d in range(4):
        nx = cx + dx[d]
        ny = cy + dy[d]

        # 일단 범위 내이고 가보지 못한곳이면 가본다
        if is_valid(nx, ny):
            # 일단 나보다 작으면 가본다
            if arr[cx][cy] > arr[nx][ny]:

            if cut and arr[cx][cy] <= arr[nx][ny]:
                tmp = arr[nx][ny]
                # 한칸만 줄인다
                arr[nx][ny] = arr[cx][cy] - 1
                v[nx][ny] = 1
                dfs(nx, ny, cnt + 1, cut - 1)
                v[nx][ny] = 0
                arr[nx][ny] = tmp
            else:
                v[nx][ny] = 1
                dfs(nx, ny, cnt + 1, cut)
                v[nx][ny] = 0
    else:
        ans = max(ans, cnt)
        return


for tc in range(1, T + 1):
    N, K = map(int, input().split())

    mx = 0
    arr = []
    for i in range(N):
        tmp = list(map(int, input().split()))
        mx = max(mx, max(tmp))
        arr.append(tmp)

    ans = 0
    v = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == mx:
                v[i][j] = 1
                dfs(i, j, 1, 1)
                v[i][j] = 0
    print('#{} {}'.format(tc, ans))