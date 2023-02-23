def postCal(t):
    # 입력값이 2개이면 leafnode 이므로 값 리턴
    if len(tree[t]) == 2:
        return int(tree[t][1])
    else:
        # 후위 순회후 계산한 값 리턴
        left = postCal(int(tree[t][2]))
        right = postCal(int(tree[t][3]))

        if tree[t][1] == '+':
            return left + right
        elif tree[t][1] == '-':
            return left - right
        elif tree[t][1] == '*':
            return left * right
        elif tree[t][1] == '/':
            return left / right

for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N + 1)

    # 정점의 번호를 인덱스로 활용하여
    # 정점의 번호의 정보들을 담는다
    for i in range(N):
        tmp = input().split()
        tree[int(tmp[0])] = tmp

    print(f'#{tc} {int(postCal(1))}')