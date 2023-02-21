'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def bfs(v, N):
    visited = [0] * (N + 1)     # visited 생성
    q = [v]     # 큐 생성, 시작점 인큐
    visited[v] = 1      # 시작점 방문 처리
    while q:
        t = q.pop(0)
        print(t, end=' ')
        for v in adjL[t]:   # t에 인접이고 방문한 적 없는 v
            if not visited[v]:
                q.append(v)     # v 인큐
                visited[v] = visited[t] + 1  # v 인큐 표시
    print(visited)



V, E = map(int,input().split())
arr = list(map(int, input().split()))
adjL = [[] for _ in range(V + 1)]
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2 + 1]
    adjL[n1].append(n2)
    adjL[n2].append(n1)

print(adjL)
bfs(1, V)   # 시작정점 1, 마지막 정점 V