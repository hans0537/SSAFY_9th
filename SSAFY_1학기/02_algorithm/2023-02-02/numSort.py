T = int(input())

def c_sort(nums, k):
    c_list = [0] * (k + 1)
    res = [0] * len(nums)

    for i in range(len(nums)):
        c_list[nums[i]] += 1

    for i in range(1, len(c_list)):
        c_list[i] += c_list[i - 1]

    for i in range(len(res) - 1, -1, -1):
        c_list[nums[i]] -= 1
        res[c_list[nums[i]]] = nums[i]

    return res

for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    print(f"#{tc}", end = " ")
    print(*c_sort(nums,max(nums)))
