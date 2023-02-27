decode = {
    '0001101': '0',
    '0011001': '1',
    '0010011': '2',
    '0111101': '3',
    '0100011': '4',
    '0110001': '5',
    '0101111': '6',
    '0111011': '7',
    '0110111': '8',
    '0001011': '9'
}

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    code = [list(input()) for _ in range(N)]

    code_num = ''

    for row in code:

        # 0 인것들은 무시
        if row.count('1') == 0:
            continue

        idx = 0
        # 뒤에서부터 확인해서 처음 1 인 idx값 가져오기
        for i in range(M - 1, -1, -1):
            if row[i] == '1':
                idx = i
                break

        while idx > 0:
            if ''.join(row[idx - 6:idx + 1]) in decode:
                code_num += decode.get(''.join(row[idx - 6:idx + 1]))
                idx -= 7
            else:
                break
        break

    cnt1 = cnt2 = 0
    # 거꾸로 저장했기 때문에 반대로 저장
    for i in range(len(code_num)):
        if i % 2:
            cnt1 += int(code_num[i])
        else:
            cnt2 += int(code_num[i])

    print('#{} {}'.format(tc, 0 if (cnt1*3 + cnt2) % 10 else (cnt1 + cnt2)))
