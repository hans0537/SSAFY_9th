# 입력 예시
s = '@#~I NeVEr DrEamEd AbouT SuCCeSs, i woRkEd foR iT.!>!'

#  먼저 소문자로 변환
s = s.lower()

# 첫번째 알파벳 인덱스
fidx = 0
# 마지막 문장의 . 인덱스
lidx = 0

for idx, i in enumerate(s):
    if fidx == 0 and i.isalpha():
        fidx = idx
    
    if i == '.':
        lidx = idx

# 앞뒤 특수문자 제거
s = s[fidx:lidx + 1]
# 첫번째 알파벳을 대문자로
s = s[0].upper() + s[1:]

print(s)

# 출력 예시
# 'I never dreamed about success, i worked for it.'
