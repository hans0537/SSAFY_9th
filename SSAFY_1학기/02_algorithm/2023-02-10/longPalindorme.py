def palin(s):
    tmp = 0
    start = 0
    for i in range(2, 101):
        if s[0: i] == s[0: i][::-1]:
            start = i

    for n in range(start, 101):
        # 검색할 길이만큼 비교
        for i in range(100 - n + 1):
            if s[i : i + n] == s[i : i + n][::-1]:
                if tmp < n:
                    tmp = n
    return tmp

for tc in range(1,11):
    input()
    board = []
    maxL = 0
    # 가로 입력받을때 회문 체크후 배열에 삽입
    for _ in range(100):
        tmp = input()
        board.append(tmp)
        t = palin(tmp)
        if maxL < t:
            maxL = t

    # 세로 회문 체크 (zip 활용)
    board_z = list(zip(*board))
    for i in range(100):
        tmp = palin(board_z[i])
        if maxL < tmp:
            maxL = tmp
    print(f'#{tc} {maxL}')


