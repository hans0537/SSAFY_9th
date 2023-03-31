T = int(input())
def dfs(n, s, cal):
    global ans
    if cal > L:
        return

    if n == N:
        if cal <= L:
            ans = max(ans, s)
        return
    
    # 현재 합에서 나머지를 더해도 큰값보다 커질일이 없으면 바로 종료
    if ans > s + sum(tmp[n:]):
        return

    dfs(n + 1, s + info[n][0], cal + info[n][1])
    dfs(n + 1, s, cal)

for tc in range(1, T + 1):
    N, L = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    tmp = list(map(lambda x:x[0], info))
    dfs(0, 0, 0)
    print('#{} {}'.format(tc, ans))