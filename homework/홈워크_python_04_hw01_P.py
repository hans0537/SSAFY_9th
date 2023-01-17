words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]

#혹시 모를 대문자를 -> 소문자로
words = [word.lower() for word in words]

#중복 체크 딕셔너리
check = {}

for idx in range(len(words) - 1):
    if words[idx] in check:
        
    if words[idx][-1] != words[idx + 1][0]:
        print(f"{idx + 1}번째 사람 실패!! 끝말이 이어지지 않음ㅋ")


    

#몇번째, 그사람이 말한 단어를 뽑기 위해 enumerate
for idx, word in enumerate(words):
    if word[-1] == 


def game()