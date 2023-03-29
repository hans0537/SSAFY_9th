import random

students = [
    "이금규",
    "김승현",
    "안민",
    "김재만",
    "임준환",
    "홍경환",
    "이민규",
    "이정현",
    "서용준",
    "김세훈",
    "이지은",
    "이태성",
    "김진주",
    "조찬익",
    "김민국",
    "박지현",
    "신성주",
    "이정찬",
    "임철성",
    "김태형",
    "위효선",
    "양지혜",
]

print('==== 광주 3반 랜덤 점심밥 먹기 프로그램!!! ====')
for i in range(6):
    list = []
    if i < 4:
        for _ in range(4):
            s = random.choice(students)
            list.append(s)
            students.remove(s)
    else:
        for _ in range(3):
            s = random.choice(students)
            list.append(s)
            students.remove(s)
    print(f'{i+1}조 : {list}')
