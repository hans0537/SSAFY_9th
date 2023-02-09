n = 10**6
is_prime = [True for i in range(n + 1)]
for i in range(2, int(n**0.5) + 1):
    if is_prime[i]:
        j = 2
        while i * j <=n:
            is_prime[i * j] = False
            j += 1

T = int(input())
for tc in range(1, T + 1):
    D, A, B = map(int, input().split())
    cnt = 0
    D = str(D)
    for i in range(A, B + 1):
        if i != 1 and is_prime[i] and (D in str(i)):
            cnt += 1

    print(f'#{tc} {cnt}')

