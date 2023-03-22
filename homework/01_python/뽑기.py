import random

students = [
    "이금규",
    "이민규",
    "이정찬",
    "이정현",

    "김세훈",
    "김승현",
    "조찬익",
    "홍경환",
    "김재만",
    "김진주",
    "이지은",
    "이태성",
    "임준환",
    "임철성",
    "김민국",
    "김태형",
    "박지현",
    "서용준",
    "신성주",
    "양지혜",
    "위효선",
    "안민",

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
