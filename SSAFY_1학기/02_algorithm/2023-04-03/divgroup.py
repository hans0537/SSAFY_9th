T = int(input())
def find_set(x):
    while x != p[x]:
        x = p[x]
    return x

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    # 집합 초기화
    p = list(range(N + 1))

    for i in range(M):
        p[find_set(arr[i*2+1])] = find_set(arr[i*2])

    ans = set()
    for i in range(1, N+1):
        ans.add(find_set(i))

    print('#{} {}'.format(tc, len(ans)))

