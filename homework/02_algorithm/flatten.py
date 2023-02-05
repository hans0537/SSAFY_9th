def dump(cnt, box):

    while cnt > 0:
        maxV = -1e9
        maxIdx = 0
        minV = 1e9
        minIdx = 0
        for i in range(len(box)):
            if box[i] > maxV:
                maxV = box[i]
                maxIdx = i

            if box[i] < minV:
                minV = box[i]
                minIdx = i

        box[maxIdx] -= 1
        box[minIdx] += 1
        cnt -= 1

    return max(box) - min(box)

for tc in range(1, 11):
    cnt = int(input())
    box = list(map(int, input().split()))

    print(dump(cnt, box))

