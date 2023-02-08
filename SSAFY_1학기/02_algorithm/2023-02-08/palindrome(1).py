T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())

    # 문자열 배열로 써도 되고
    # 문자열 그대로 사용해도 된다.
    text = [list(input()) for _ in range(n)]

    # 정답이 될 단어
    answer = ""

    # (0,0) 부터 문장을 만든 후에 뒤집어서 결과가 같은지 확인
    for i in range(n):
        for j in range(n - m + 1):  # 인덱스 범위 조심
            # (i,j)에 있는 글자부터 단어 만들기 시작
            # 가로 ,세로 한번에
            word_row = ""
            word_col = ""
            # 우리가 원하는 단어의 길이는 ? m
            # m 만큼 문자를 떼와서 문자열 만들기
            for k in range(m):
                word_row += text[i][j + k]
                word_col += text[j + k][i]

            # 뒤집은 뒤에 비교
            if word_row == word_row[::-1]:
                answer = word_row[::-1]
            if word_col == word_col[::-1]:
                answer = word_col[::-1]

    print(f"#{tc} {answer}")
