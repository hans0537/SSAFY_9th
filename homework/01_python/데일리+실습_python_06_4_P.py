entry_record = ['이싸피', '박장고', '조실습', '이싸피', '조실습', '오디비', '임온실', '조실습', '조실습', '이싸피', '안도둑', '임온실', '최이썬', '오디비', '안도둑', '염자바', '박장고', '조실습',
                '최이썬', '조실습', '염자바', '박장고', '임온실', '임온실', '이싸피', '임온실', '오디비', '조실습', '염자바', '임온실', '박장고', '최이썬', '안도둑', '염자바', '임온실', '박장고', '이싸피', '안도둑',
                '임온실', '오디비', '최이썬', '안도둑', '이싸피', '오디비', '안도둑', '이싸피', '박장고', '박장고', '안도둑', '안도둑', '안도둑', '염자바', '최이썬', '오디비', '오디비', '최이썬', '이싸피', '임온실', '안도둑']

exit_record = ['최이썬', '조실습', '이싸피', '안도둑', '임온실', '안도둑', '이싸피', '오디비', '염자바', '박장고', '최이썬', '이싸피', '염자바', '염자바', '박장고', '임온실', '이싸피',
               '박장고', '안도둑', '염자바', '이싸피', '조실습', '조실습', '임온실', '박장고', '이싸피', '조실습', '박장고', '오디비', '안도둑', '조실습', '임온실', '안도둑', '안도둑', '임온실', '조실습', '최이썬', '안도둑', '임온실',
               '염자바', '이싸피', '임온실', '안도둑', '오디비', '안도둑', '오디비', '임온실', '염자바', '임온실', '박장고', '조실습', '이싸피', '최이썬', '최이썬', '오디비', '오디비', '염자바', '오디비', '안도둑', '박장고']

# 딕셔너리 사용
entry_dic = {} 
exit_dic = {}

for i in entry_record:
    if i in entry_dic:
        entry_dic[i] += 1
    else:
        entry_dic[i] = 1

for i in exit_record:
    if i in exit_dic:
        exit_dic[i] += 1
    else:
        exit_dic[i] = 1

top3 = list(sorted(entry_dic.items(), key=lambda x : x[1], reverse=True))
print(top3)
print('입장 기록 많은 Top3')
for i in range(3):
    print(f'{top3[i][0]} {top3[i][1]}회')

print()

print('출입 기록이 수상한 사람')
suspicious = []
for name in entry_dic:
    cnt = entry_dic.get(name) - exit_dic.get(name)
    if cnt != 0:
        suspicious.append((name, cnt, ))

for name in suspicious:
    if name[1] > 0:
        print(f'{name[0]}은 입장 기록이 {name[1]}회 더 많아 수상합니다.')
    elif name[1] < 0:
        print(f'{name[0]}은 퇴장 기록이 {-name[1]}회 더 많아 수상합니다.')

print()
# 카운터 사용
from collections import Counter

entry_dic = Counter(entry_record)
exit_dic = Counter(exit_record)

# Counter 모듈에는 가장 흔한 데이터를 가져올수 있는 메소드가 most_common(cnt)
# 매개변수로는 상위 몇개를 뽑아올지 정할수 있다. 없으면 전체 
print('입장 기록 많은 Top3')
for name, cnt in entry_dic.most_common(3):
    print(f'{name} {cnt}회')

print()

# # Counter 객체는 서로 빼고 더할수 있다.
# # 단 뺄샘의 결과로 0이나 음수가 나온 경우에는 최종 카운터 객체에서 제외가 된다.
# # 따라서 반대로 다시 빼준다
print('출입 기록이 수상한 사람')
# suspicious = entry_dic - exit_dic
# for name in suspicious:
#     print(f'{name}은 입장 기록이 {suspicious.get(name)}회 더 많아 수상합니다.')

# suspicious = exit_dic - entry_dic
# for name in suspicious:
#     print(f'{name}은 퇴장 기록이 {suspicious.get(name)}회 더 많아 수상합니다.')

# subtract 사용 
entry_dic.subtract(exit_dic)
for name in entry_dic:
    if entry_dic.get(name) > 0:
        print(f'{name}은 입장 기록이 {entry_dic.get(name)}회 더 많아 수상합니다.')
    elif entry_dic.get(name) < 0:
        print(f'{name}은 퇴장 기록이 {-entry_dic.get(name)}회 더 많아 수상합니다.')
