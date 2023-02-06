T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    box = [[0 for _ in range(10)] for n in range(10)]
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        if color == 1:
            for j in range(c1, c2 + 1):
                for k in range(r1, r2 + 1):
                    if box[j][k] == 2:
                        box[j][k] += 1
                    else:
                        box[j][k] = 1
        else:
            for j in range(c1, c2 + 1):
                for k in range(r1, r2 + 1):
                    if box[j][k] == 1:
                        box[j][k] += 2
                    else:
                        box[j][k] = 2
    cnt = 0
    for i in range(10):
        for j in range(10):
           if box[i][j] == 3:
               cnt += 1

    print(f'#{tc} {cnt}')