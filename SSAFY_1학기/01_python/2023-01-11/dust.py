# dust1 = 미세먼지농도
dust1 = 150


# 결과가 bool (True or False) 인 식을 써준다.
# 조건을 하나 만족하게 되면 나머지는 실행하지 않는다.
if dust1 > 150:
    print("매우나쁨")
elif 80 < dust1 <= 150:
    print("나쁨")
elif 30 < dust1 and dust1 <= 80:
    print("보통")
else:
    print("좋음")
