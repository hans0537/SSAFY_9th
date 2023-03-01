T = int(input())
for tc in range(1, T + 1):
    people = [0] + list(map(int, list(input())))

    cnt = 0
    ans = 0
    for i in range(1, len(people)):
        if i - 1 <= cnt:
            cnt += people[i]
        else:
            ans += i - 1 - cnt
            cnt = i - 1 + people[i]

    print('#{} {}'.format(tc, ans))