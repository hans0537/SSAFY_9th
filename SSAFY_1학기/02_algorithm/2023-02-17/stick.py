T = int(input())
for tc in range(1, T + 1):
    s = input()

    ans = 0  # 정답 변수
    cnt = 0  # 잘려 나간 막대기 수
    for i in range(len(s)):
        if s[i] == '(':  # 막대기 시작 또는 레이저 시작
            cnt += 1
        elif s[i] == ')':
            # 바로 직전이 여는괄호면 레이저
            if s[i - 1] == '(':
                cnt -= 1  # 레이저 시작한거 빼고
                ans += cnt  # 왼쪽 잘려 나간 막대기 수
            else:
                ans += 1  # 닫힌 거 오른쪽 잘려나간거 하나 추가
                cnt -= 1  # 막대기 수 하나 줄이기

    print(f'#{tc} {ans}')