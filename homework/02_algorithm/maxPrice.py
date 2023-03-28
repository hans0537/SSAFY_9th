T = int(input())

def dfs(cnt):
    global ans

    if cnt == M:
        ans = max(ans, int(''.join(nums)))
        return

    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]

            check = int(''.join(nums))
            if (cnt, check) not in visited:
                visited.append((cnt, check))
                dfs(cnt + 1)
            nums[i], nums[j] = nums[j], nums[i]


for tc in range(1, T + 1):
    N, M = input().split()
    M = int(M)
    nums = list(N)

    if M > len(nums):
        M = len(nums)
    ans = 0

    visited = []
    dfs(0)
    print('#{} {}'.format(tc, ans))