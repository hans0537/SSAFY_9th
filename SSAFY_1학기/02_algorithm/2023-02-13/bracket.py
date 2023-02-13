'''
4
( )( )((( )))
((( )((((( )( )((( )( ))((( ))))))
())
(()
'''

T = int(input())

for tc in range(1, T + 1):
    row = input()  # 검사할 문자열

    stack = []

    answer = 1  # 1 => 괄호가 제대로 되어있다, 0 => 제대로 되어있지 않다

    for c in row:
        # 열린 괄호가 나오면 스택에 push
        if c == "(":
            stack.append(c)
        # 닫힌 괄호가 나오면
        # 스택의 길이가 0 이 아닌지 검사 (언더플로우 방지)
        # 스택에서 pop 해서 나온 괄호와 짝이 일치하는지를 검사
        if c == ")":
            if len(stack) == 0:
                answer = 0
                break

            b = stack.pop()
            if not (b == "(" and c == ")"):
                answer = 0
                break

    # 반복이 다 끝나고 나서 남은 괄호가 스택에 있는지 검사
    if len(stack) > 0:
        answer = 0

    print(f"#{tc} {answer}")
