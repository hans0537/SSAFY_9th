def dump(cnt, box):
    if cnt == 0:
        return
    while cnt > 0:

    box = sorted(box)
    for i in range(1, 100):
        if box[0] < box[i]:
            cnt -= box[i] - box[0]
            box[99] -= box[i] - box[0]
            box[0] += box[i] - box[0]
            break
    return dump(cnt, box)




for tc in range(1, 11):
    cnt = int(input())
    box = list(map(int, input().split()))

    dump(cnt, box)
