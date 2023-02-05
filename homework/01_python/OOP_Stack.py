# Stack 자료구조 구현 클래스
class Stack:

    # 인스턴스 생성시 빈 배열 생성
    def __init__(self):
        self.arr = []

    # 배열의 길이가 0이면 True 아니면 False
    def empty(self):
        return len(self.arr) == 0

    # 인스턴스 메서드를 활용하여 empty면 none 반환
    # 가장 마지막 인덱스인 요소를 반환
    def top(self):
        if self.empty():
            return None
        return self.arr[-1]

    # 인스턴스 메서드를 활용하여 empty면 none 반환
    # 가장 마지막 인덱스인 요소를 반환후 삭제
    def pop(self):
        if self.empty():
            return None
        return self.arr.pop()

    # 배열의 append를 이용하여 마지막 인덱스에 요소 추가
    def push(self, num):
        self.arr.append(num)

    # 배열을 스트링으로 반환하여 배열의 요소를 출력
    def __repr__(self):
        return f'{self.arr}'

# 입력 예시
stack_arr = Stack()
print(stack_arr.empty())
stack_arr.push(1)
print(stack_arr)
stack_arr.push(2)
print(stack_arr)
stack_arr.push(3)
print(stack_arr)
print(stack_arr.top())
print(stack_arr.pop())
print(stack_arr)