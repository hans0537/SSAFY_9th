T = int(input())
for tc in range(1, T + 1):
    N, Q = map(int, input().split())

    # 1번부터 N번까지의 상자
    box = [0] * (N + 1)
    for i in range(1, Q + 1):
        L, R = map(int, input().split())
        box[L:R + 1] = [i] * (R - L + 1)

    print(f'#{tc}', *box[1:])