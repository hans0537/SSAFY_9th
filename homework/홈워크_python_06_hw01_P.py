# 입력 예시
# # mass percent.py 실행 시
# 1.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: 1% 400g
# 2.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: 8% 300g
# Done

# 출력 예시
# 4.0% 700.0g

for _ in range(5):
    s = input('소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: ')

    if 'Done' in s:
        break

    s = s.split(' ')



tot_water = 0
tot_salt = 0
if len(s) == 1:
    print('정보를 입력하세요')
elif 'Done' in s and len(s) > s.index('Done') + 1:
    print('Done 이후에 입력을 하였습니다. 다시 입력하세요')
elif len(s) > 10:
    print('소금물 5개만 입력 가능합니다.')
elif 'Done' in s and len(s) % 2 == 0:
    print('소금물의 양과 농도를 맞춰서 입력하세요')
else:
    for i in range(0, len(s) - 1, 2):
        salt = int(s[i]) * int(s[i + 1]) / 100
        tot_water += int(s[i + 1])
        tot_salt += salt

    print(f'혼합물 퍼센트 농도 : {round(tot_salt / tot_water * 100, 2)}% | 혼합물 양 : {tot_water}g')