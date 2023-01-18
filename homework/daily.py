test_status = {
    '김싸피': 'solving',
   	'이코딩': 'solving',
   	'최이썬': 'cheating',
   	'오디비': 'sleeping',
   	'임온실': 'cheating',
   	'조실습': 'solving',
   	'박장고': 'sleeping',
   	'염자바': 'cheating'
}

cheat = []

for i in test_status.keys():
    if test_status[i] == 'cheating':
        cheat.append(i)
    elif test_status[i] == 'sleeping':
        test_status[i] = 'solving'

cheat = sorted(cheat)
for i in cheat:
    del test_status[i]
print(cheat)
print(test_status)