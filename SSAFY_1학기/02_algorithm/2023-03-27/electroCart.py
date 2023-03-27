T = int(input())
def dfs(i, lst):
    global ans

    if i > N:
        lst = lst + [1]
        tmp = 0
        for j in range(len(lst) - 1):
            tmp += arr[lst[j] - 1][lst[j + 1] - 1]
        ans = min(ans, tmp)

    for n in range(2, N + 1):
        if not v[n]:
            v[n] = 1
            dfs(i + 1, lst + [n])
            v[n] = 0

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 1e9
    v = [0] * (N + 1)
    # 2부터 순열 시작
    dfs(2, [1])
    print('#{} {}'.format(tc, ans))
