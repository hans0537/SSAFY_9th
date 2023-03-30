T = int(input())

for tc in range(1, T + 1):
    lst = list(map(int, input().split()))
    N = lst[0]
    dp = [1e9] * (N * 2)
    dp[1] = 0

    # 1번 정류장부터 ~ N번 정류장까지
    for i in range(1, N):
        # 해당 정류장에서 갈 수 있는 거리를 탐색후
        for j in range(1, lst[i] + 1):
            # 현재 위치에서 한번 간거랑 기존에 저장되어 있는 값이랑 비교후 최소값 저장
            dp[i + j] = min(dp[i + j], dp[i] + 1)

    print('#{} {}'.format(tc, dp[N] - 1))