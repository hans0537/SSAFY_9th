def threesqrt(num):
    dp = [0] * (num + 1)
    for i in range(num + 1):
        dp[i] = i ** 3

    return dp


T = int(input())
for tc in range(1, T + 1):
    num = int(input())
    lst = threesqrt(int(num ** (1/3)) + 1)
    if num in lst:
        print(f'#{tc} {lst.index(num)}')
    else:
        print(f'#{tc} -1')