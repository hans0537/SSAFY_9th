'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

n = int(input())
tree = list(map(int, input().split()))

# 인덱스가 부모노드의 번호
cleft = [0] * (n + 1)
cright = [0] * (n + 1)

for i in range(n - 1):
    p = tree[i*2]
    c = tree[i*2 + 1]
    if cleft[p] == 0:
        cleft[p] = c
    else:
        cright[p] = c

# 1. 전위 순회 preorder VLR
def preorder(t):
    # t 노드가 존재한다면
    if t:
        # 데이터 처리
        print(t, end=' ')
        # 왼쪽 방문
        preorder(cleft[t])
        # 오른쪽 방문
        preorder(cright[t])
# 1. 중위 순회 inorder LVR
def inorder(t):
    # t 노드가 존재한다면
    if t:
        # 왼쪽 방문
        inorder(cleft[t])
        # 데이터 처리
        print(t, end=' ')
        # 오른쪽 방문
        inorder(cright[t])
# 1. 후위 순회 postorder LRV
def postorder(t):
    # t 노드가 존재한다면
    if t:
        # 왼쪽 방문
        postorder(cleft[t])
        # 오른쪽 방문
        postorder(cright[t])
        # 데이터 처리
        print(t, end=' ')

preorder(1)
print()
inorder(1)
print()
postorder(1)

