T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    num_list = list(map(int, input().split()))

    ans = 0
    max_v = num_list[-1]
    for i in range(N - 2, -1, -1):
        if num_list[i] >= max_v:
            max_v = num_list[i]
        else:
            ans += max_v - num_list[i]
    print(f'#{tc} {ans}')