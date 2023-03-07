dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
from collections import deque
import copy

def down(temp):
    d_arr = [[0] * W for _ in range(H)]
    for w in range(W):
        # 끌어올 위치
        pointer = H - 1
        for h in range(H - 1, -1, -1):
            if temp[h][w]:
                d_arr[pointer][w] = temp[h][w]
                pointer -= 1
    return d_arr

def bomb(temp, x, y, p):
    q = deque()
    q.append((x, y, p))

    while q:
        cx, cy, p = q.popleft()
        temp[cx][cy] = 0

        for d in range(4):
            for k in range(1, p):
                mx = cx + dx[d] * k
                my = cy + dy[d] * k

                if 0 <= mx < H and 0 <= my < W:
                    if temp[mx][my] != 0:
                        if temp[mx][my] > 1:
                            q.append((mx, my, temp[mx][my]))
                        temp[mx][my] = 0

def c_block(temp):
    global minV
    tmp = 0
    for i in range(H):
        for j in range(W):
            if temp[i][j]:
                tmp += 1
    minV = min(minV, tmp)

# 구슬 떨어트리는 경우의 수
def dfs(arr, N):
    global minV

    if N == 0:
        # 현재 배열 상태를 넘겨서 세준다.
        c_block(arr)
        return

    # 떨어트릴 위치를 찾기
    # 가로를 본다
    for j in range(W):
        # 매번 복사해서 넘겨주어야 함
        temp = copy.deepcopy(arr)
        x, y = 0, j
        # x, y 에 블록이 있는곳을 찾는다
        while x < H and not temp[x][y]:
            x += 1

        # 만약 맨땅에 떨어트렸을때의 경우의 수
        if x == H:
            c_block(temp)
            continue

        bomb(temp, x, y, temp[x][y])
        temp = down(temp)
        dfs(temp, N - 1)

T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    minV = 1e9

    # 처음 구슬을 떨어트릴 위치 시작
    dfs(arr, N)
    print('#{} {}'.format(tc, minV))
