T = int(input())
def bSearch(n, left, right, check):
    global ans
    mid = (left + right) // 2

    if A[mid] == n:
        ans += 1
        return
    elif A[mid] < n and check != 1:
        bSearch(n, mid + 1, right, 1)
    elif A[mid] > n and check != -1:
        bSearch(n, left, mid - 1, -1)


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    ans = 0
    for i in B:
        bSearch(i, 0, N - 1, 0)

    print('#{} {}'.format(tc, ans))