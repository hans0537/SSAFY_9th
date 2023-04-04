def find_set(x):
    while x != p[x]:
        x = p[x]
    return x

def union(x, y):
    p[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    graph = []
    p = [i for i in range(V + 1)]
    for _ in range(E):
        graph.append(list(map(int, input().split())))

    graph.sort(key=lambda x:x[2])

    s = cnt = 0
    for n1, n2, w in graph:
        if find_set(n1) != find_set(n2):
            cnt += 1
            s += w
            union(n1, n2)
            if cnt == V:
                break

    print('#{} {}'.format(tc, s))