T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())

    people = sorted(list(map(int, input().split())))
    cnt = 0

    for i in people:
        cnt += 1
        if (i // M) * K < cnt:
            print('#{} Impossible'.format(tc))
            break
    else:
        print('#{} Possible'.format(tc))
