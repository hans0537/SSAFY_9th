def dfs(idx, cnt):
    global ans
    if idx == N:
        return

    if cnt == N // 2:
        x = y = 0
        for i in range(N):
            if visited[i]:
                x += lst[i][0]
                y += lst[i][1]
            else:
                x -= lst[i][0]
                y -= lst[i][1]
        s = x ** 2 + y ** 2
        ans = min(s, ans)
        return

    visited[idx] = 1
    dfs(idx + 1, cnt + 1)
    visited[idx] = 0
    dfs(idx + 1, cnt)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [tuple(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    ans = 1e20
    dfs(0, 0)
    print('#{} {}'.format(tc, ans))