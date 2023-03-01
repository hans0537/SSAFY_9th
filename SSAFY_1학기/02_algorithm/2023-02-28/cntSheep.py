T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    i = 0
    num = []
    while True:
        if len(set(num)) == 10:
            print(f'#{tc} {N * i}')
            break

        i += 1

        tmp = N * i
        while tmp > 0:
            num.append(tmp % 10)
            tmp //= 10

