class Node:
    def __init__(self, data):
        self.data = data
        self.left = 0
        self.right = 0

def inorderCal(t):
    if t:
        inorderCal(tree[int(t.left)])
        left = int(t.data)

        inorderCal(tree[int(t.right)])
        right = int(t.data)


for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N + 1)

    for i in range(N):
        tmp = input().split()
        if len(tmp) == 2:
            tree[int(tmp[0])] = Node(int(tmp[1]))
        else:
            t = Node(tmp[1])
            t.left = tmp[2]
            t.right = tmp[3]
            tree[int(tmp[0])] = t

    print(f'#{tc} {inorderCal(1)}')