T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    # 큐사용
    queue = []
    for i in range(N):
        s = input().split()
        for _ in range(int(s[1])):
            queue.append(s[0])

    print(f'#{tc}')
    while len(queue) != 0:
        for _ in range(10):
            if len(queue) == 0:
                break
            print(f'{queue.pop(0)}',end='')
        print()