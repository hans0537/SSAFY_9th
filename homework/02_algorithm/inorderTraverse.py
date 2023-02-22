# 트리의 노드의 정보들을 담을 클래스 선언
class Node:
    def __init__(self, data):
        self.data = data
        self.left = 0   # 일단 생성시 0으로 leaf Node라고 선언
        self.right = 0  # 일단 생성시 0으로 leaf Node라고 선언

def inorder(v):
    # 객체의 정보가 있으면 중위 탐색
    if v:
        inorder(tree[int(v.left)])
        res.append(v.data)
        inorder(tree[int(v.right)])

for tc in range(1, 11):
    N = int(input())
    
    # 입력 받는 순서대로 클래스 객체 선언
    tree = [0] * (N + 1)
    for i in range(1, N + 1):
        tmp = input().split()
        if len(tmp) == 2:
            tree[int(tmp[0])] = Node(tmp[1])
        elif len(tmp) == 3:
            n = Node(tmp[1])
            n.left = tmp[2]
            tree[int(tmp[0])] = n
        elif len(tmp) == 4:
            n = Node(tmp[1])
            n.left = tmp[2]
            n.right = tmp[3]
            tree[int(tmp[0])] = n

    res = []
    inorder(tree[1])
    print(f'#{tc}', ''.join(res))