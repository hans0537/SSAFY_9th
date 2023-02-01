# 입력 예시
# # mass percent.py 실행 시
# 1.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: 1% 400g
# 2.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: 8% 300g
# Done

# 출력 예시
# 4.0% 700.0g

import re

tot_water = 0
tot_salt = 0
for _ in range(5):
    s = input('소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: ')

    if 'Done' in s:
        break
    
    # %와 g이 들어갈수도 있으니 숫자만 추출하여 per, salt변수에 각각 대입
    per, water = map(int, re.findall(r'\d+', s))
    
    tot_water += water
    tot_salt += per * water / 100

print(f'{round(tot_salt / tot_water * 100, 2)}% {tot_water}g')
