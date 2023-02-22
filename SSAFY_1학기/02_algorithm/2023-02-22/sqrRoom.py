from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(s, e):
    q = deque()
    q.append((s, e))

    cnt = 1
    while q:
        x, y = q.popleft()

        for d in range(4):
            mx = x + dx[d]
            my = y + dy[d]

            if 0 <= mx < N and 0 <= my < N and room[mx][my] - room[x][y] == 1:
                cnt += 1
                q.append((mx, my))
                break
    return cnt

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]

    mx_cnt = 0
    dic = {}
    for i in range(N):
        for j in range(N):
            s = i
            e = j
            tmp = bfs(s, e)

            if mx_cnt <= tmp:
                mx_cnt = tmp
                if dic.get(mx_cnt):
                    dic[mx_cnt].append(room[i][j])
                else:
                    dic[mx_cnt] = [room[i][j]]

    print(f'#{tc} {min(dic.get(mx_cnt))} {mx_cnt}')