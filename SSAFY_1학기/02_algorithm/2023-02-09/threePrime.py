prime = []
for i in range(2, 1000):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime.append(i)
m = len(prime)

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    cnt = 0
    for i in range(m):
        if prime[i] > n:
            break

        for j in range(i, m):
            if prime[j] > n:
                break

            for k in range(j, m):
                if prime[k] > n:
                    break

                if prime[i] + prime[j] + prime[k] == n:
                    cnt += 1
    print(f'#{tc} {cnt}')

