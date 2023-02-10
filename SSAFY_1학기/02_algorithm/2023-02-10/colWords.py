T = int(input())
for tc in range(1, T + 1):
    words = []
    for _ in range(5):
        words.append(input())

    # 가장 긴 단어의 길이
    ml = max(map(len,words))
    ans = ''
    for i in range(ml):
        for j in range(5):
            # 없는 부분은 공백으로 처리
            if i >= len(words[j]):
                ans += ''
            else:
                ans += words[j][i]
    print(ans)