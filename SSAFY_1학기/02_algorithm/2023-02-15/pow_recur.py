def recur(n, p):
    if p == 0:
        return 1
    return n * recur(n,p-1)

for tc in range(1, 11):
    input()
    n, p = map(int, input().split())
    print(f'#{tc} {recur(n,p)}')