from datetime import date

#Driver's code
class Person:

    # 생성자
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #클래스 메서드
    @classmethod
    def get_age(cls, name, y):
        # 객체 생성후 리턴
        # cls를 사용하여 자신 클래스의 생성자 호출
        return cls(name, date.today().year - y) 

    def check_age(self):
        if self.age < 19:
            return False
        return True

person1 = Person('Mark', 20)
person2 = Person.get_age('Rohan', 1992)

print(person1.name, person1.age) 
print(person2.name, person2.age)
print(person1.check_age())
print(person2.check_age())
