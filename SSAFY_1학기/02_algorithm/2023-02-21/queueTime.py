import time
from collections import deque
n = 100000

# 1. front, rear를 사용한 선형 큐
q = [0] * n
front = rear = -1

# 2. deque
q2 = deque()

# 3. append, pop(0)
q3 = []

# 1번 방법으로 큐에 원소를 넣었다가 빼보기
start = time.time()
for i in range(n):
    rear += 1
    q[rear] = i

for i in range(n):
    front += 1
    v = q[front]
end = time.time()
print(f"1번 방법: {end-start}")

# 2번 방법으로 ...
start = time.time()
for i in range(n):
    q2.append(i)

for i in range(n):
    q2.popleft()

end = time.time()
print(f"2번 방법: {end-start}")

# 3번 방법으로 ...
start = time.time()
for i in range(n):
    q3.append(i)

for i in range(n):
    q3.pop(0)
end = time.time()
print(f"3번 방법: {end-start}")
