def inorderCal(t):

    if t > N:
        return 0

    left = inorderCal(t*2)
    right = inorderCal()
    if tree[t] == '+':
        return int(left) + int(inorderCal(t*2 + 1))
    elif tree[t] == '-':
        return int(left) - int(inorderCal(t*2 + 1))
    elif tree[t] == '*':
        return int(left) * int(inorderCal(t*2 + 1))
    elif tree[t] == '/':
        return int(left) / int(inorderCal(t*2 + 1))

for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N + 1)

    for i in range(N):
        tmp = input().split()
        tree[int(tmp[0])] = tmp[1]

    print(f'#{tc} {inorderCal(1)}')