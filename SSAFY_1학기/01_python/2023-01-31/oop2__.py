class Person:
    def __init__(self, name, age, money, num):
        # public
        self.name = name
        self.age = age
        
        # protect
        self._money = money

        # private
        self.__num = num

    def get_money(self):
        print(self._money)
    
    def get_num(self, password):
        if password == "1234":
            print(self.__num)
        else:
            print("비밀번호를 잘못 입력했습니다.")

p1 = Person("홍길동", 30, "1억", "1234-1234")

print(p1.age)

# print(p1._money)
p1.get_money()

# print(p1.__num) 오류
p1.get_num("1111")
p1.get_num("1234")

# 밖에서 private 에 접근 가능 (그러나 비추!!!)
# print(p1._Person__num)