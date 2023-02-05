class Person:
    def __init__(self):
        self._age = 0

    # def get_age(self):      # getter
    #     print('getter 호출 !')
    #     return self._age
    
    # def set_age(self, age): # setter
    #     print('setter 호출 !')
    #     self._age = age

    # age = property(get_age, set_age)

    @property
    def age(self):      # getter
        print('getter 호출 !')
        return self._age
    
    @age.setter
    def age(self, age): # setter
        print('setter 호출 !')
        self._age = age
    


p1 = Person()
# p1._age = 25   -> protected 라 안됨
# print(p1._age) -> 이것도 안됨

# 좋은 코드지만 불편함
# p1.set_age(25)
# print(p1.get_age())

# age 변수에 property를 활용하여 getter, setter 호출
# 다만 property 정의도 불편함
p1.age = 25
print(p1.age)