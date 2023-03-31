T = int(input())
dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]
def is_valid(x, y):
    return 0 <= x < N and 0 <= y < N

def dfs(ci, cj, d, s):
    global ans

    # 종료 조건
    # 현재 위치가 출발위치와 같아지고 오른쪽 아래 방향으로 시작했으니
    # 방향이 오른쪽 위이면
    if d == 3:
        if ci == si and cj == sj:
            ans = max(ans, s)
        return

    # 직진이냐
    if is_valid(ci + dx[d], cj + dy[d]) and not v[ci + dx[d]][cj + dy[d]]:
        v[ci + dx[d]][cj + dy[d]] = 1
        dfs(ci + dx[d], cj + dy[d], d, s + arr[ci][cj])
        v[ci + dx[d]][cj + dy[d]] = 0

    # 방향 전환이냐
    if is_valid(ci + dx[d + 1], cj + dy[d + 1]) and not v[ci + dx[d + 1]][cj + dy[d + 1]]:
        v[ci + dx[d + 1]][cj + dy[d + 1]] = 1
        dfs(ci + dx[d + 1], cj + dy[d + 1], d + 1, s + arr[ci][cj])
        v[ci + dx[d + 1]][cj + dy[d + 1]] = 0

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = -1

    # 방향은 오른쪽 아래부터 시계방향 고정 => 모양은 같기 때문에
    # 따라서 출발 가능 지역만 탐색
    v = [[0] * N for _ in range(N)]
    for i in range(N - 2):
        for j in range(1, N - 1):
            si = i
            sj = j
            v[i][j] = 1
            dfs(i, j, 0, 0)
            v[i][j] = 0

    print('#{} {}'.format(tc, ans))