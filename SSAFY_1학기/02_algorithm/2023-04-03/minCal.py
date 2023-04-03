from collections import deque

T = int(input())

def bfs(s):
    q = deque()
    q.append(s)
    v[s] = 1

    while q:
        cur = q.popleft()

        if cur == M:
            return v[cur]

        for d in (1, -1, 2, -10):
            if d == 2:
                n = cur * d
            else:
                n = cur + d

            if n <= 1000000 and not v[n]:
                q.append(n)
                v[n] = v[cur] + 1

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    v = [0] * 1000001
    print('#{} {}'.format(tc, bfs(N) - 1))

