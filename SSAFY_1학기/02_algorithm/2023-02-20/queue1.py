def isFull():
    return rear == size - 1

def enqueue(data):
    global rear
    if isFull():
        print("full")
        return
    rear += 1
    queue[rear] = data

def isEmpty():
    return front == rear

def dequeue():
    global front
    if isEmpty():
        print("emtpy")
        return
    front += 1
    return queue[front]

size = 10
queue = [0] * size
front = rear = -1

for i in range(10):
    enqueue(i)

for i in range(10):
    print(dequeue(), end=" ")
print()
# rear += 1
# queue[rear] = 1
# enqueue(2)
# enqueue(3)

print(dequeue())
print(dequeue())
print(dequeue())
if front != rear:
    print(dequeue())
if front != rear:
    print(dequeue())

q = []
q.append(10)
q.append(20)
q.append(30)
print(q.pop(0))
print(q.pop(0))
print(q.pop(0))

from collections import deque

q1 = deque()
q1.append(100)
q1.append(200)
q1.append(300)
print(q1.popleft())
print(q1.popleft())
print(q1.popleft())