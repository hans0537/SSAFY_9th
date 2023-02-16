# 우선순위 딕셔너리
dic = {'+' : 1, '*' : 2}
def cal(postfix):
    stack = []

    for c in postfix:
        # 숫자이면 스택에 저장
        if '0' <= c <= '9':
            stack.append(int(c))
        else:
            # 만약 스택이 2 이하이면 계산 불가 종료
            if len(stack) < 2:
                break
            op2 = stack.pop()
            op1 = stack.pop()
            if c == '+':
                stack.append(op1 + op2)
            elif c == '*':
                stack.append(op1 * op2)
    return stack.pop()

def get_postfix(infix):
    postfix = ''
    stack = []
    for c in infix:
        if '0' <= c <= '9':
            postfix += c
        else:
            while stack and dic.get(stack[-1]) >= dic.get(c):
                postfix += stack.pop()
            stack.append(c)

    while stack:
        postfix += stack.pop()

    return postfix

for tc in range(1, 11):
    n = int(input())
    infix = input()
    postfix = get_postfix(infix)
    print(f'#{tc} {cal(postfix)}')