# 퀴즈
# 행 5 * 열 6, 값을 임의로 할당(random)
# 2 차원 배열의 모든 원소를 순회하면서 짝수인 원소의 개수를 세는 프로그램

import random
from pprint import pprint

def is_valid(x, y):
    return 0 <= x < 6 and 0 <= y < 5

arr = [[random.randrange(1, 11) for _ in range(6)] for _ in range(5)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0
for x in range(5):
    for y in range(6):
        if arr[x][y] % 2 == 0:
            cnt += 1
