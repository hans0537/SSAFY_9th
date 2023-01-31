class Stack:

    def __init__(self):
        self.arr = []

    def empty(self):
        return len(self.arr) == 0

    def top(self):
        if self.empty():
            return None
        return self.arr[-1]
    
    def pop(self):
        if self.empty():
            return None
        return self.arr.pop()

    def push(self, num):
        self.arr.append(num)

    def __repr__(self):
        return f'{self.arr}'

stack_arr = Stack()
stack_arr
print(stack_arr.empty())
stack_arr.push(1)
stack_arr.push(2)
stack_arr.push(3)
print(stack_arr)
print(stack_arr.top())
print(stack_arr.pop())
print(stack_arr)