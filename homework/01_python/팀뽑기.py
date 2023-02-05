import random

students = [
    "김민국",
    "김세훈",
    "김승현",
    "김재만",
    "김진주",
    "김태형",
    "서용준",
    "안민",
    "양지혜",
    "위효선",
    "이금규",
    "이민규",
    "이정찬",
    "이정현",
    "이태성",
    "임준환",
    "조찬익",
    "홍경환",
]

print('==== 광주 3반 팀 선정 프로그램!!! ====')
for i in range(6):
    list = []
    for _ in range(3):
        s = random.choice(students)
        list.append(s)
        students.remove(s)
    print(f'{i+1}조 : {list}')
