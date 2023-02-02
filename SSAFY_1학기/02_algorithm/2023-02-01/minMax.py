T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    maxV = -1e9
    minV = 1e9

    for i in list(map(int, input().split())):
        if i > maxV:
            maxV = i

        if i < minV:
            minV = i

    print(f"#{tc} {maxV - minV}")