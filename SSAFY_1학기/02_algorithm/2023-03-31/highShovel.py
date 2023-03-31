T = int(input())
def dfs(idx, s):
    global ans
    if ans <= s - B or s + sum(heights[idx:]) < B:
        return

    if idx == N:
        if s >= B:
            ans = min(ans, s-B)
        return

    dfs(idx + 1, s + heights[idx])
    dfs(idx + 1, s)


for tc in range(1, T + 1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    ans = 1e9
    dfs(0, 0)
    print('#{} {}'.format(tc, ans))