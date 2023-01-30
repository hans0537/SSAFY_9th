class Person:
    count = 0 # 클래스 변수

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1
        print('생성될 때 자동으로 불려요')
    
    def __str__(self):
        return self.name + " : " + self.age

    def __gt__(self, other):
        return self.age > other.age

    @classmethod
    def number_of_population(cls):
        print(f"인구수는 {cls.count} 입니다")

aiden = Person('aiden', 23)
issac = Person('issac', 19)
print(aiden > issac)

Person.number_of_population()
aiden.number_of_population()
issac.number_of_population()