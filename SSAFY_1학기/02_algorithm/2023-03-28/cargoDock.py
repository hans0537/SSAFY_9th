import heapq

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cargo = []
    for _ in range(N):
        cargo.append(list(map(int, input().split())))

    cargo.sort(key=lambda x:x[1])
    ans = 0
    e = 0
    for i in range(N):
        if e <= cargo[i][0]:
            ans += 1
            e = cargo[i][1]

    print('#{} {}'.format(tc, ans))
