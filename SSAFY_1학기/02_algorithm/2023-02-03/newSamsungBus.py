T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    cnt = [0] * 1001
    for _ in range(N):
        a, b, c = map(int, input().split())

        if a == 1:
            for i in range(b, c + 1):
                cnt[i] += 1
        elif a == 2:
            if b % 2:
                for i in range(b, c + 1):
                    if i % 2:
                        cnt[i] += 1
            else:
                for i in range(b, c + 1):
                    if i % 2 == 0:
                        cnt[i] += 1
        elif a == 3:
            if b % 2:
                for i in range(b, c + 1):
                    if i % 3 == 0 and i % 10 != 0:
                        cnt[i] += 1
            else:
                for i in range(b, c + 1):
                    if i % 4 == 0:
                        cnt[i] += 1

    print(f'#{tc} {max(cnt)}')