def presum(t):
    if t <= 0 or t > N:
        return 0

    if tree[t]:
        return tree[t]

    return presum(t*2) + presum(t*2 + 1)

T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())

    tree = [0] * (N + 1)
    for i in range(M):
        leaf, data = map(int, input().split())
        tree[leaf] = data

    print(f'#{tc} {presum(L)}')
