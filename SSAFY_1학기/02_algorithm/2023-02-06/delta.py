import random

from pprint import pprint

n = 5

def is_valid(x, y):
    return 0 <= x < n and 0 <= y < n

arr = [[random.randrange(1, 11) for _ in range(n)] for _ in range(n)]

pprint(arr)

# 절대값의 총합
abs_sum = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 행 우선순회
for x in range(n):
    for y in range(n):
        # 현재 위치 (x, y)
        now = arr[x][y]
        print(f"arr[{x}][{y}] : {arr[x][y]}")
        # 4방향 탐색을 하면서 이웃한 원소의 차이의 절대값의 합
        # 주의할점 : 상하좌우로 움직일때 유효한 범위(인덱스) 인지 꼭 확인
        temp_abs = 0 # 현재 위치에서 절대값 차이의 합
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if is_valid(nx, ny):
                # 절대값 계산
                temp_abs += abs(arr[x][y] - arr[nx][ny])
        abs_sum += temp_abs
print(f'ans : {abs_sum}')