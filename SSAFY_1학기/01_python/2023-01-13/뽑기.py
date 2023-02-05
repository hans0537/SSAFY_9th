import random

students = [
    "김민국",
    "김세훈",
    "김승현",
    "김재만",
    "김진주",
    "김태형",
    "박지현",
    "서용준",
    "신성주",
    "안민",
    "양지혜",
    "위효선",
    "이금규",
    "이민규",
    "이정찬",
    "이정현",
    "이지은",
    "이태성",
    "임준환",
    "임철성",
    "조찬익",
    "홍경환",
]

면제권 = []

if len(students) == len(면제권):
    print("다했어요")
else:
    vip = random.choice(students)
    while vip in 면제권:
        vip = random.choice(students)
    print(f"======!!{vip} 님 당첨!!======")
