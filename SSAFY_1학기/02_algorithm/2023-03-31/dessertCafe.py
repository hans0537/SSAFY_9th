T = int(input())
dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]
def is_valid(x, y):
    return 0 <= x < N and 0 <= y < N

def dfs(v, ci, cj, d):
    global ans

    # 종료 조건
    # 현재 위치가 출발위치와 같아지고 오른쪽 아래 방향으로 시작했으니
    # 방향이 오른쪽 위이면

    if d == 3 and ci == si and cj == sj:
        ans = max(ans, len(v))
        return

    for i in range(2):
        # 직진이냐 방향전환이냐
        d += i

        if d > 3:
            break

        ni = ci + dx[d]
        nj = cj + dy[d]

        if is_valid(ni, nj) and arr[ni][nj] not in v:
            v.append(arr[ni][nj])
            dfs(v, ni, nj, d)
            v.pop()


for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = -1

    # 방향은 오른쪽 아래부터 시계방향 고정 => 모양은 같기 때문에
    # 따라서 출발 가능 지역만 탐색
    for i in range(N - 2):
        for j in range(1, N - 1):
            si = i
            sj = j
            dfs([], i, j, 0)

    print('#{} {}'.format(tc, ans))