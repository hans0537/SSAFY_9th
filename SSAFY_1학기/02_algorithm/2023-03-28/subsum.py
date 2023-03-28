T = int(input())
def dfs(i, s):
    global ans
    if i == N:
        if s == K:
            ans += 1
        return

    dfs(i + 1, s + lst[i])
    dfs(i + 1, s)

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    ans = 0
    dfs(0, 0)
    print('#{} {}'.format(tc, ans))