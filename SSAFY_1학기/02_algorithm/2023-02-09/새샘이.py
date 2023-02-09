prime = []
for i in range(2, 1000):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime.append(i)

T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    count = 0

    prime_len = len(prime)

    # 경우의 수를 일단 모두 구해보자
    for i in range(prime_len):
        # i 번째 소수를 고르고
        for j in range(i, prime_len):
            # j번째 소수를 고르고
            for k in range(j, prime_len):
                # k번재 소수를 고르고
                if prime[i] + prime[j] + prime[k] == n:
                    count += 1

    print(f"#{tc} {count}")
