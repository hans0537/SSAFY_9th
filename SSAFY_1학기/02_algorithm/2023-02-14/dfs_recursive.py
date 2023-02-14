def dfs(now):
    print(now)
    # now : 현재 정점 번호
    # 현재 정점에서 방문할수 있는 정점을 찾아서 방문
    for to in range(1, V + 1):
        if adj[now][to] and not visited[to]:
            visited[to] = 1
            dfs(to) # 재귀호출, like stack push


V, E = map(int, input().split())
adj = [[0] * (V + 1) for _ in range(V + 1)]
# 인접 리스트
adj_list = [[] for _ in range(V + 1)]
for i in range(E):
    start, to = map(int, input().split())
    adj[start][to] = 1
    # 무향 그래프 (방향이 없는 그래프)만 아래 추가
    adj[to][start] = 1
    # 인접 리스트 사용
    adj_list[start].append(to)
    adj_list[to].append(start)

visited = [0] * (V + 1)
visited[1] = 1
dfs(1)
