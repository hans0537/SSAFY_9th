T = int(input())
def cal(alst):
    blst = [x for x in range(N) if x not in alst]

    asum = bsum = 0

    for i in alst:
        for j in alst:
            asum += info[i][j]
    for i in blst:
        for j in blst:
            bsum += info[i][j]

    return abs(asum - bsum)


def dfs(n, acnt, alst, tmp):
    global ans

    if n == N:
        if acnt == N // 2:
            tmp = cal(alst)
            ans = min(ans, tmp)
        return

    dfs(n + 1, acnt + 1, alst+[n], tmp + 1)
    dfs(n + 1, acnt, alst, tmp + 1)

for tc in range(1, T + 1):
    N = int(input())
    info = [list(map(int, input().split())) for _ in range(N)]
    ans = 1e9
    dfs(0, 0, [], 0)
    print('#{} {}'.format(tc, ans))
