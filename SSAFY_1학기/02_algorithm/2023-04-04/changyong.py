def find_set(x):
    while x != p[x]:
        x = p[x]
    return x

def union(x, y):
    p[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    p = [i for i in range(N + 1)]
    for _ in range(M):
        x, y = map(int, input().split())
        union(x, y)

    ans = set()
    for i in p[1:]:
        ans.add(find_set(i))

    print('#{} {}'.format(tc, len(ans)))
