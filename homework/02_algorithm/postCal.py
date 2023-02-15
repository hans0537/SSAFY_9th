# 후위 표기식 변환
def get_postfix(infix):
    post = ''
    stack = []
    for i in infix:
        if '0' <= i <= '99':
            post += i
        else:
            # 스택에 + 가 있으면 빼고 다시 넣기
            if len(stack) != 0 and stack[-1] == i:
                post += stack.pop()
            stack.append(i)
    return post

# 후위 표기식 계산
def cal(post):
    stack = []
    for i in post:
        if '0' <= i <= '9':
            stack.append(int(i))
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(op1 + op2)
    # 스택에 남아 있는 값들을 더해준다
    return sum(stack)

for tc in range(1, 11):
    input()
    print(f'#{tc} {cal(get_postfix(input()))}')