# 1 + 2
# 2 – 1
# 3 * 4
# 4 / 0

class Calculator:

    def __init__(self, num):
        self.num = num

    def add(self, o):
        return self.num + o.num
    
    def sub(self, o):
        return self.num - o.num
    
    def mul(self, o):
        return self.num * o.num
    
    def div(self, o):
        try:
            return self.num / o.num
        except:
            return '0으로 나눌수 없습니다.'

a = Calculator(1)
b = Calculator(2)

print(a.add(b))
print(b.sub(a))

c = Calculator(3)
d = Calculator(4)
e = Calculator(0)

print(c.mul(d))
print(d.div(e))