# Point 클래스
class Point:

    # 좌표값을 저장할 생성자
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    
    # 좌측상단좌표 와 우측상단좌표 (Point 인스턴스)들을
    # rectangle 인스턴스에 저장
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    # 넓이 메서드
    def get_area(self):
        # 각 좌표 인스턴스의 x와 y 좌표 접근
        return abs((self.p1.x - self.p2.x) * (self.p1.y - self.p2.y))

    # 둘레 메서드
    def get_perimeter(self):
        return (abs(self.p1.x - self.p2.x) + abs(self.p1.y - self.p2.y))*2

    # 정사각형 유무 메서드
    def is_square(self):
        if abs(self.p1.x - self.p2.x) == abs(self.p1.y - self.p2.y):
            return True
        return False


# 입력 예시
p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())

# 출력 예시
# 4
# 8
# True

# 9
# 12
# True