T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())

    nums = list(map(int, input().split()))

    minV = 1e9
    maxV = -1e9
    for i in range(n - m + 1):
        tmp = sum(nums[i:i+m])
        if tmp > maxV:
            maxV = tmp

        if tmp < minV:
            minV = tmp

    print(f"#{tc} {maxV - minV}")
