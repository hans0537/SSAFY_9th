T = int(input())
for tc in range(1, T + 1):
    binary = input()
    ternary = input()

    blist = []
    tlist = []

    for i in range(len(binary)):
        if binary[i] == '0':
            tmp = binary[:i] + '1' + binary[i + 1:]
        else:
            tmp = binary[:i] + '0' + binary[i + 1:]

        tmp = int(tmp, 2)
        blist.append(tmp)

    for i in range(len(ternary)):
        if ternary[i] == '0':
            tmp = ternary[:i] + '1' + ternary[i + 1:]
            tmp = int(tmp, 3)
            tlist.append(tmp)
            tmp = ternary[:i] + '2' + ternary[i + 1:]
            tmp = int(tmp, 3)
            tlist.append(tmp)
        elif ternary[i] == '1':
            tmp = ternary[:i] + '2' + ternary[i + 1:]
            tmp = int(tmp, 3)
            tlist.append(tmp)
            tmp = ternary[:i] + '0' + ternary[i + 1:]
            tmp = int(tmp, 3)
            tlist.append(tmp)
        else:
            tmp = ternary[:i] + '1' + ternary[i + 1:]
            tmp = int(tmp, 3)
            tlist.append(tmp)
            tmp = ternary[:i] + '0' + ternary[i + 1:]
            tmp = int(tmp, 3)
            tlist.append(tmp)

    for i in blist:
        for j in tlist:
            if i == j:
                print('#{} {}'.format(tc, i))
                break

