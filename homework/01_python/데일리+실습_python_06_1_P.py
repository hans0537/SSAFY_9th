# A. 입력예시
# de_identify('970103-1234567')
# de_identify('8611232345678')

# B. 출력예시
# 970103*******
# 861123******* 

def de_identify(jumin):
    # 주민번호 생년월일은 6자리
    # 뒤자리는 7자리이므로 '*' * 7
    return jumin[:6] + '*' * 7

print(de_identify('970103-1234567'))
print(de_identify('8611232345678'))