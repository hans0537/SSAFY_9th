from collections import deque

def bfs(start):
    visited = [0] * (V + 1)
    q = deque()
    q.append(start)

    while q:
        s = q.popleft()

        if s == end:
            return visited[s]

        for w in adjL[s]:
            if not visited[w]:
                q.append(w)
                visited[w] += visited[s] + 1

    return 0

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adjL = [[] for _ in range(V + 1)]

    for i in range(1, E + 1):
        x1, x2 = map(int, input().split())
        adjL[x1].append(x2)
        adjL[x2].append(x1)

    start, end = map(int, input().split())

    print(f'#{tc} {bfs(start)}')