T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())

    arr = []
    cnt = 0
    for _ in range(N):
        tmp = list(map(int, input().split()))
        # 가로체크
        c = 0
        for i in range(N - 1):
            if tmp[i] == 0:
                if c == K:
                    cnt += 1
                c = 0
            if tmp[i] == 1 and tmp[i + 1] == 1:
                c += 1