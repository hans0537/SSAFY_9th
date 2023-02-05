year = int(input('어떤 해를 입력하세요: '))

ans = '윤년 아닙니다'
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 100):
    ans = '윤년입니다'

print(ans)