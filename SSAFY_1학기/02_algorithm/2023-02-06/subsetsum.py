T = int(input())
for tc in range(1, T + 1):
    numbers = [n for n in range(1,13)]
    n = len(numbers)

    N, K = map(int, input().split())
    cnt = 0
    for i in range(1<<n):
        tmp = []
        for j in range(n):
            if i & (1<<j):
                tmp.append(numbers[j])
        if sum(tmp) == K and len(tmp) == N:
            cnt += 1
    print(f'#{tc} {cnt}')