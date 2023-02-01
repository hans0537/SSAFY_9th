# 강아지의 정보를 담을 클래스 생성
class Doggy:
    # 현재 강아지수
    num_of_dogs = 0
    # 태어난 강아지들의 수
    birth_of_dogs = 0

    # 생성자
    # 인스턴스 생성시 강아지의 이름, 종을 저장후
    # 태어난, 현재 강아지 수 (클래스 변수) 증가
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1

    # 강아지가 죽을때(인스턴스 소멸) 현재 강아지수 감소(클래스 변수)
    def __del__(self):
        Doggy.num_of_dogs -= 1
    
    # 강아지가 짖는 메서드
    def bark(self):
        return f'{self.name} : 왈왈'

    # 현재 status를 출력해주는 클래스 메서드 활용
    @classmethod
    def get_status(cls):
        return f'태어난 수: {cls.birth_of_dogs}마리\n현재 수: {cls.num_of_dogs}마리'

d1 = Doggy('초코', '푸들')
print(d1.bark())
d2 = Doggy('흰둥이', '말티즈')
d3 = Doggy('제키', '허스키')

print(Doggy.get_status())
del d2

print()
print(Doggy.get_status())