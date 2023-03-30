T = int(input())


def btrack(idx, s):
    global ans

    if ans <= s:
        return

    # idx는 한 행을 의미, 따라서 N개 선택이 끝나면 종료
    if idx == N:
        ans = min(ans, s)
        return

    # i 는 공장을 선택하는 경우
    for i in range(N):
        if not v[i]:
            v[i] = 1
            btrack(idx + 1, s + arr[idx][i])
            v[i] = 0


for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 1e9

    v = [0] * N
    btrack(0, 0)

    print('#{} {}'.format(tc, ans))
