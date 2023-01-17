words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]

#혹시 모를 대문자를 -> 소문자로
words = [word.lower() for word in words]

#중복 체크 배열 (첫번째 단어는 프리패스이므로)
check = [words[0]]

for idx in range(1, len(words)):
    if words[idx] in check:
        print(f"{idx + 1}번째 사람 실패!! 중복된 단어 입니다!")
        break
    else:
        check.append(words[idx])
        if words[idx - 1][-1] != words[idx][0]:
            print(f"{idx + 1}번째 사람 실패!! 끝말잇기 실패!")
            break
else:
    print("모두 통과")