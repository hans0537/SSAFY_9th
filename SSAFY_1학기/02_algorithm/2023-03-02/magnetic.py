for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    arr = list(zip(*arr))

    ans = 0
    for i in range(N):
        check = 0
        for j in range(N):
            if arr[i][j] == 1:
                check = 1
            elif arr[i][j] == 2:
                if check == 1:
                    ans += 1
                    check = 0

    print('#{} {}'.format(tc, ans))