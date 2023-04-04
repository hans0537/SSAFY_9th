INF = 100000
def dijkstra(s, N):
    U = [0] * (N + 1)
    U[s] = 1
    D[s] = 0

    for e, w in adjL[s]:
        D[e] = w

    for _ in range(N):
        minV = INF
        t = 0
        for i in range(N + 1):
            if U[i] == 0 and minV > D[i]:
                minV = D[i]
                t = i

        U[t] = 1
        for e, w in adjL[t]:
            D[e] = min(D[e], D[t] + w)


T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    adjL = [[] for _ in range(N + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        adjL[s].append([e, w])

    D = [INF] * (N + 1)
    dijkstra(0, N)
    print('#{} {}'.format(tc, D[N]))
