T = int(input())
for tc in range(1, T + 1):
    num = float(input())

    ans = ''
    cnt = 0
    while num != 0 and cnt < 13:
        num *= 2
        cnt += 1

        if int(num) == 1:
            ans += '1'
            num -= 1
        else:
            ans += '0'

    if cnt >= 13:
        print('#{} overflow'.format(tc))
    else:
        print('#{} {}'.format(tc, ans))