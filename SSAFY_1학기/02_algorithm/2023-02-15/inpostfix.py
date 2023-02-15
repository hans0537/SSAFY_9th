# 스택 밖에 있을시 우선 순위 (토큰의 우선순위)
icp = {'+': 1, '-': 1, '/': 2, '*': 2, '(': 3}
# 스택 안에 있을시 우선 순위
isp = {'+': 1, '-': 1, '/': 2, '*': 2, '(': 0}

# infix => 중위표기식
# n => 식의 길이
def get_postfix(infix, n):
    postfix = ''  # 결과로 출력할 후위 표기식
    stack = []

    # infix 안에 있는 문자들을 하나씩 떼와서 처리
    for i in range(n):
        # 피연산자인 경우
        if '0' <= infix[i] <= '9':
            postfix += infix[i]

        # 연산자인 경우
        else:
            # 닫는 괄호가 나오는 경우
            if infix[i] == ')':
                # 여는 괄호가 나올때까지 pop 해서 결과에 출력
                while stack:
                    char = stack.pop()
                    if char == '(':
                        break
                    postfix += char
            # 다른 연산자가 나오는 경우
            else:
                # 현재 토큰(연산자)의 우선순위보다
                # stack[top]의 우선순위가 같거나 높으면 계속 pop
                while stack and isp[stack[-1]] >= icp[infix[i]]:
                    postfix += stack.pop()
                # 그게 아니면 push
                stack.append(infix[i])

    # 남아 있는 연산자를 출력
    while stack:
        postfix += stack.pop()

    return postfix

string = '2+3*4/5'
print(get_postfix(string, 7))