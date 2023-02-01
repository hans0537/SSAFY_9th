import random

class ClassHelper:

    def __init__(self, arr):
        self.arr = arr

    def pick(self, idx):
        return random.sample(self.arr, idx)

    def match_pair(self):
        r_list = []
        random.shuffle(self.arr)
        if len(self.arr) % 2:
            r_list.append([self.arr.pop(0), self.arr.pop(0), self.arr.pop(0)])
            
        for i in range(len(self.arr) // 2):
            r_list.append([self.arr.pop(0), self.arr.pop(0)])
        
        return r_list


ch = ClassHelper(['김해피', '이해킹', '조민지', '박영수', '정민수'])

print(ch.pick(1))
print(ch.pick(1))
print(ch.pick(2))
print(ch.pick(3))
print(ch.pick(4))

print(ch.match_pair())
