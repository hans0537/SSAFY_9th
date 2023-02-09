def palin(s, n):
    c = 0
    # 검색할 길이만큼 비교
    for i in range(8 - n + 1):
        if s[i : i + n] == s[i : i + n][::-1]:
            c += 1
    return c

for tc in range(1, 11):
    n = int(input())
    board = []
    cnt = 0
    # 가로 입력받을때 회문 체크후 배열에 삽입
    for _ in range(8):
        tmp = input()
        cnt += palin(tmp, n)
        board.append(tmp)

    # 세로 회문 체크
    for i in range(8):
        tmp = []
        for j in range(8):
            tmp.append(board[j][i])
        cnt += palin(tmp, n)

    print(f'#{tc} {cnt}')