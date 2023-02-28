pat = {
    (2, 1, 1): 0,
    (2, 2, 1): 1,
    (1, 2, 2): 2,
    (4, 1, 1): 3,
    (1, 3, 2): 4,
    (2, 3, 1): 5,
    (1, 1, 4): 6,
    (3, 1, 2): 7,
    (2, 1, 3): 8,
    (1, 1, 2): 9
}


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # 중복된 값 제거후 정렬
    code = sorted(list(set([input()[:M] for _ in range(N)])))
    # 정렬된 값에서 0번째는 0으로만 되어있으므로 제거
    code.pop(0)

    # 확인한 코드인지 판별할 배열
    check = []

    N = len(code)
    ans = 0
    for i in range(N):
        l = len(code[i]) * 4
        x = int(code[i], 16)

        bit = ""
        for j in range(l - 1, -1, -1):
            # i번째 비트가 1인지 아닌지
            bit += '1' if x & (1 << j) else '0'

        # 오른쪽에서 1전까지 0 제거
        bit = bit.rstrip('0')

        # 뒤로 탐색하면서 1 과 0들의 개수를 세어 비율을 구한다
        c1 = c2 = c3 = c4 = 0
        code_num = []
        for j in range(len(bit) - 1, -1, -1):
            if bit[j] == '1' and c3 == 0:
                c4 += 1
            elif bit[j] == '0' and c2 == 0:
                c3 += 1
            elif bit[j] == '1' and c1 == 0:
                c2 += 1
            elif bit[j] == '0':  # 맨 앞으 0의 비율은 생략해도 됨
                if bit[j - 1] == '1':  # 만약 직전 값이 1 이면
                    g = gcd(gcd(c2, c3), c4)  # 최대공약수를 구해 굵은 암호코드 처리
                    code_num.append(pat.get((c2 // g, c3 // g, c4 // g)))
                    c2 = c3 = c4 = 0    # 정보를 담고 0으로 초기화

                    if len(code_num) == 8:  # 8자리 코드가 완성이 되면
                        cnt1 = cnt2 = 0
                        # 거꾸로 저장했기 때문에 반대로 저장
                        for i in range(8):
                            if i % 2:
                                cnt1 += code_num[i]
                            else:
                                cnt2 += code_num[i]

                        if (cnt1 * 3 + cnt2) % 10 == 0:
                            if code_num not in check:
                                ans += (cnt1 + cnt2)
                                check.append(code_num)

                        code_num = [] # 초기화

    print('#{} {}'.format(tc, ans))
