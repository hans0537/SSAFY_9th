"""
3
3 17 1 39 8 41 2 32 99 2
22 8 5 123 7 2 63 7 3 46
6 63 2 3 58 76 21 33 8 1   
"""

T = int(input())
for tc in range(1, T + 1):

    # 숫자 한줄 입력받아서 리스트로 만들기
    num_list = list(map(int, input().split()))

    # 홀수의 총 합
    ans = 0

    for num in num_list:
        # 입력받은 수중에 홀수가 있는지 확인
        if num % 2 == 1:
            # 홀수가 맞다면 아래 코드가 실행될것.
            ans = ans + num

    # 반복이 끝나면 합을 출력
    print(f"#{tc} {ans}")
