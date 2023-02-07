T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()
    ans = [0] * 10
    j = 0
    for i in range(N - 1, N - 6, -1):
        ans[j] = numbers[i]
        j += 2

    j = 1
    for i in range(5):
        ans[j] = numbers[i]
        j += 2

    print(f'#{tc}', *ans)