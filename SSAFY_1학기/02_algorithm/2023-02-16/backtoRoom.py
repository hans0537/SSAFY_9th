T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 복도 배열
    corridor = [0] * 200
    for i in range(N):
        s, e = map(int, input().split())
        if s > e:
            s, e = e, s

        if s % 2:
            s //= 2
        else:
            s = s//2 - 1

        if e % 2:
            e = e // 2 + 1
        else:
            e //= 2

        for j in range(s, e):
            corridor[j] += 1
    print(f'#{tc} {max(corridor)}')