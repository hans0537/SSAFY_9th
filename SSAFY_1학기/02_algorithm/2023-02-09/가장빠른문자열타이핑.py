T = int(input())

for tc in range(1, T + 1):
    a, b = input().split()

    typing = 0

    # 문자열 인덱스 0부터 탐색하면서 타이핑 횟수 세기
    idx = 0
    # 패턴 비교할수 있을만큼 비교 (텍스트길이 - 패턴길이)
    while idx < len(a) - len(b) + 1:
        # 패턴 길이 만큼 잘라서 비교
        # 같으면 개수 1 증가
        # 인덱스를 패턴의 길이만큼 뒤로 이동
        sub = ""
        for i in range(len(b)):
            sub += a[idx + i]

        # 잘랐는데 패턴과 일치
        if sub == b:
            typing += 1
            idx += len(b)
        # 패턴과 불일치
        else:
            typing += 1
            idx += 1

    # 남은 글자 처리 (텍스트에서 마지막부분, 패턴 길이보다 짧은 부분)
    while idx < len(a):
        typing += 1
        idx += 1

    print(f"#{tc} {typing}")
