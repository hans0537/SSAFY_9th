# 후위표기식 결과 계산
def get_result(postfix):
    stack = []

    for c in postfix:
        # 피연산자를 만나면 스택에 넣기
        if '0' <= c <= '9':
            stack.append(int(c))

        # 연산자를 만나면 피연산자를 두개 꺼내서 계산
        else:
            # 오른쪽이 먼저
            right = stack.pop()
            # 외쪽이 나중에
            left = stack.pop()
            if c == '+':
                result = left + right
            elif c == '-':
                result = left - right
            elif c == '*':
                result = left * right
            elif c == '/':
                result = left / right

            # 스택에 계산 결과 넣기 (다음 연산을 위해서)
            stack.append(result)

    # 마지막에 남은 결과 하나 꺼내서 리턴
    return stack.pop()

print(get_result('234*5/+'))