from collections import deque
def findMax(visited):
    mx = max(visited)
    mx_idx = 0
    for i in range(101):
        if visited[i] == mx:
            if mx_idx < i:
                mx_idx = i

    return mx_idx

def bfs(start):
    visited = [0] * 101
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        s = q.popleft()

        for w in adjL[s]:
            if not visited[w]:
                q.append(w)
                visited[w] = visited[s] + 1

    return findMax(visited)


for tc in range(1, 11):
    N, start = map(int, input().split())
    adjL = [[] for _ in range(101)]
    arr = list(map(int, input().split()))
    for i in range(N // 2):
        adjL[arr[i*2]].append(arr[i*2 + 1])

    print(f'#{tc} {bfs(start)}')