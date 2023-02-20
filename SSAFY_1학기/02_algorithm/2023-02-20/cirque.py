def enqueue(item):
    global rear
    rear = (rear + 1) % N
    queue[rear] = item

def dequeue():
    global front
    front = (front + 1) % N
    return queue[front]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    queue = [0] + list(map(int, input().split()))
    front = 0
    rear = N
    for i in range(M):
        tmp = dequeue()
        enqueue(tmp)

    print(f'#{tc} {dequeue()}')


