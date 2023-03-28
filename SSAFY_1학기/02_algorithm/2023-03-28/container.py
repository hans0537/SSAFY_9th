T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    wlist = sorted(list(map(int, input().split())), reverse=True)
    tlist = sorted(list(map(int, input().split())))
    used = [0] * N

    tot = 0
    for i in range(M):
        for j in range(N):
            if wlist[j] <= tlist[i] and not used[j]:
                used[j] = 1
                tot += wlist[j]
                break

    print('#{} {}'.format(tc, tot))

