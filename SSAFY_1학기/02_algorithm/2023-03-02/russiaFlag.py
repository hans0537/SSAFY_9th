T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    ans = 1e9
    tmp = []
    for w in range(N - 2):
        for b in range(w + 1, N - 1):
            tmp.append((w, b))

    for w, b in tmp:
        t = 0
        for i in range(w + 1):
            t += M - arr[i].count('W')

        for j in range(w + 1, b + 1):
            t += M - arr[j].count('B')

        for k in range(b+1,N):
            t += M - arr[k].count('R')

        ans = min(ans, t)


    print('#{} {}'.format(tc, ans))