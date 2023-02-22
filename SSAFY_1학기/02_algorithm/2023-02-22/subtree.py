def pre(t):
    global cnt
    if t:
        cnt += 1
        pre(cleft[t])
        pre(cright[t])

T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    tree = list(map(int, input().split()))

    cleft = [0] * (E + 2)
    cright = [0] * (E + 2)
    for i in range(E):
        p = tree[i * 2]
        c = tree[i * 2 + 1]
        if cleft[p] == 0:
            cleft[p] = c
        else:
            cright[p] = c

    cnt = 0
    pre(N)
    print(f'#{tc} {cnt}')