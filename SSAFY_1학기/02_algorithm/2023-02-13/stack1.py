# 1. 배열의 메서드 사용하기

stack = []


def push(item):
    stack.append(item)


def pop():
    if len(stack) == 0:
        return
    else:
        return stack.pop()


def peek():
    return stack[-1]


for i in range(10):
    push(i)

print(stack)
print(peek())

for i in range(10):
    print(pop(), end=" ")
print()

# 2. 직접 구현하기

# 스택 초기화
top = -1
size = 10
stack = [0] * 10


def my_push(item):
    # push를 하고 나면 꼭대기를 가르키는 top 이 변하기 때문에 global 선언
    global top

    if top == size:
        print("오버플로우!!")
    else:
        top += 1
        stack[top] = item


def my_pop():
    global top
    if top == -1:
        print("언더플로우!!")
        return
    else:
        top -= 1
        return stack[top + 1]


for i in range(10):
    my_push(i)

print(stack)

for i in range(10):
    print(my_pop(), end=" ")
print()
