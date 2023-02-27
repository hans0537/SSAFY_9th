decode = {
    0 : 13,
    1 : 25,
    2 : 19,
    3 : 61,
    4 : 35,
    5 : 49,
    6 : 47,
    7 : 59,
    8 : 55,
    9 : 11
}

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    code = [list(map(int, list(input()))) for _ in range(N)]

    code_num = ''
    check = False
    for row in code:
        if check:
            break

        if row.count(1) == 0:
            continue

        i = 0
        while i + 7 < M:
            tmp = row[i : i + 7]
            for j in tmp:
                for d in range(10):
                    if decode[d] & (2**j) != 0:
                        code_num += str(d)
                        i += 7
                        check = True
                        break

    print(code_num)


    # print(code)