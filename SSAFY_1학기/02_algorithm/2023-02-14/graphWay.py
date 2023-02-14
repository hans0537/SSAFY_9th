T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    stack = []

    for _ in range(E):
        start, end = map(int, input().split())
        adj_list[start].append(end)

    s, e = map(int, input().split())
    print(f'#{tc}', end=' ')
    while True:
        if s == e:
            print(1)
            break

        for w in adj_list[s]:
            if visited[w] == 0:
                stack.append(w)
                s = w
                visited[w] = 1
                break
        else:
            if stack:
                s = stack.pop()
            else:
                print(0)
                break