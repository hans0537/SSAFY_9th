size = 10 + 1
cq = [0] * size
front = rear = 0


def isFull():
    return (rear + 1) % size == front


def enqueue(item):
    global rear
    if isFull():
        print("full")
        return
    rear = (rear + 1) % size
    cq[rear] = item


def isEmpty():
    return front == rear


def dequeue():
    global front
    if isEmpty():
        print("empty")
        return
    front = (front + 1) % size
    return cq[front]


for i in range(10):
    enqueue(i)

print(cq)
print(isEmpty())
print(isFull())

for i in range(10):
    print(dequeue(), end=" ")
print()
print(isEmpty())
print(isFull())

enqueue(99)
print(cq)
