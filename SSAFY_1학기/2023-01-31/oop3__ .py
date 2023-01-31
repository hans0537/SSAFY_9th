class Calculator:
    # getter setter 는 public에는 사용 안한다.
    def __init__(self, a, b):
        self._a = a
        self._b = b

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, new_b):
        if new_b == 0:
            print("0 으로는 바꿀 수 없습니다")
            return
        self._b = new_b

    def divide(self):
        return self._a / self._b

c = Calculator(10, 5)

print(c.divide())

c.b = 0
print(c.divide())
