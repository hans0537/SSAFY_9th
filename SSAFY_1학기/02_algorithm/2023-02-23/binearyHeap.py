def enq(n):
    global last
    last += 1
    tree[last] = n
    c = last
    p = c // 2
    while p > 0:
        if tree[p] > tree[c]:
            tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c // 2

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    tree = [0] * (N + 1)
    last = 0
    for i in nums:
        enq(i)

    tmp = N
    ans = 0
    while tree[tmp] > 0:
        tmp //= 2
        ans += tree[tmp]

    print(f'#{tc} {ans}')