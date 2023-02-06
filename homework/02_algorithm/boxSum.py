# 가로 체크
def maxRow(box):
    maxV = 0
    for i in range(100):
        tmp = 0
        for j in range(100):
            tmp += box[i][j]
        if tmp > maxV:
            maxV = tmp
    return maxV

# 세로체크
def maxCol(box):
    maxV = 0
    for i in range(100):
        tmp = 0
        for j in range(100):
            tmp += box[j][i]
        if tmp > maxV:
            maxV = tmp
    return maxV

# 대각선 체크
def maxDiag(box):
    sum1 = 0
    # 오른쪽 아래 대각선
    for i in range(100):
        sum1 += box[i][i]

    sum2 = 0
    # 왼쪽 아래 대각선
    for i in range(99, -1, -1):
        sum2 += box[99 - i][i]

    if sum1 < sum2:
        return sum2
    elif sum1 > sum2:
        return sum1
    else:
        return sum1

for tc in range(1, 11):
    input()
    box = [list(map(int, input().split())) for _ in range(100)]
    max1 = maxRow(box)
    max2 = maxCol(box)
    max3 = maxDiag(box)
    print(f'#{tc} {max([max1, max2, max3])}')


