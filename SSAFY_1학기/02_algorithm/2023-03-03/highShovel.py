T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))

    diff = []
    for i in range(1 << N):
        tmp = 0
        # 부분집합중 합의 크기가 B보다 크면
        for j in range(N):
            if i & (1 << j):
                tmp += lst[j]
        if tmp >= B:
            diff.append(tmp - B)

    print('#{} {}'.format(tc, min(diff)))
