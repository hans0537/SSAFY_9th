dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 현재 이동방향에서 1~5번 블록을 만날때 방향 전환해줄 배열
block = [[], [1, 3, 0, 2], [3, 0, 1, 2], [2, 0, 3, 1], [1, 2, 3, 0], [1, 0, 3, 2]]

def wallD(d):
    if d == 0:
        return 1
    elif d == 1:
        return 0
    elif d == 2:
        return 3
    elif d == 3:
        return 2

def wormHoll(x, y, w):
    for rx, ry in wormholl.get(w):
        if rx != x or ry != y:
            return rx, ry

def bfs(si, sj):
    global ans
    # 시작 위치 저장
    start = (si, sj)

    # 현재위치에서 4가지 방향에 대한 경우 탐색
    for d in range(4):
        mx, my = si, sj
        cnt = 0

        while True:
            mx = mx + dx[d]
            my = my + dy[d]

            # 시작지점으로 다시 오면
            if mx == start[0] and my == start[1]:
                break

            # 벽에 부딪힐시 방향 반대 전환
            if mx < 0 or mx >= N or my < 0 or my >= N:
                d = wallD(d)
                cnt += 1
            # 블랙홀 일시 종료
            elif board[mx][my] == -1:
                break
            # 장애물이 있다면
            elif board[mx][my] != 0:
                tmp = board[mx][my]
                if 1 <= tmp <= 5:  # 블록일때
                    cnt += 1
                    d = block[tmp][d]
                elif 6 <= tmp <= 10:  # 웜홀일때
                    wx, wy = wormHoll(mx, my, tmp)
                    mx = wx
                    my = wy

        ans = max(ans, cnt)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    # 웜홀 짝 맞춘 딕셔너리 생성
    wormholl = {6: [], 7: [], 8: [], 9: [], 10: []}
    ans = 0
    for i in range(N):
        for j in range(N):
            if 6 <= board[i][j] <= 10:
                wormholl[board[i][j]].append((i, j))

    for si in range(N):
        for sj in range(N):
            if board[si][sj] == 0:
                bfs(si, sj)

    print(f'#{tc} {ans}')
