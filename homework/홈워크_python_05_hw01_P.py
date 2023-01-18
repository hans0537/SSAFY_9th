# 입력 예시
# 2015
# 8
# 31

# 출력 예시 
#경고 월요일입니다.
#{'년': 2015, '월': 8, '일': 31, '요일': '월요일'}

import calendar

# 요일을 가져올 배열 생성
w_list = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']

while True:
    print('==============타임 머신==============')
    print('1. 시간여행하기\n2. 종료')
    
    sel = int(input('선택: '))

    if sel == 1:
        while True:
            # 또 시간 여행을 할 수 있으니 이 부분에서 dic 생성
            dic = {}
            print('================================================================')
            year = int(input('연도 입력: '))
            
            if calendar.isleap(year):
                print(f"{year}년은 윤년입니다. 다시 입력하세요")
                continue
            
            print('================================================================')
            print(calendar.calendar(year))
            print('================================================================')
            
            while True:
                month = int(input('월 입력: '))
                day = int(input('일 입력: '))
                
                try:
                    wday = w_list[calendar.weekday(year,month,day)]
                    if wday == '월요일':
                        print('경고!! 월요일입니다.')
                    dic['년'] = year
                    dic['월'] = month
                    dic['일'] = day
                    dic['요일'] = wday
                    print(dic)
                    break
                except:
                    print('날짜가 안맞게 입력 되었습니다.')
                    print('================================================================')
            break
    elif sel == 2:
        print('타임머신 종료!!')
        break
    else:
        print('1번과 2번중 선택하세요')

