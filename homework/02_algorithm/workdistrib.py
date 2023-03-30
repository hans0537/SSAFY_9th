T = int(input())
def dfs(row, s):
    global ans
    if s <= ans:
        return

    if row == N:
        ans = max(ans, s)
        return

    for idx in range(N):
        if not v[idx] and arr[row][idx] != 0:
            v[idx] = 1
            dfs(row + 1, s * (arr[row][idx] / 100))
            v[idx] = 0

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [0] * N
    ans = 0
    dfs(0, 1)
    print('#{} {:.6f}'.format(tc, round(ans*100, 6)))

