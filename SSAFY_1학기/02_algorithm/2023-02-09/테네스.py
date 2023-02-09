# 1. 에라토스테네스의 체 사용해서 소수 체크 배열 만들기
n = 10 ** 6

prime = [True for i in range(n + 1)]
prime[1] = False
prime[0] = False

for i in range(2, int(n ** 0.5) + 1):
    if prime[i]:
        j = 2
        while i * j <= n:
            prime[i * j] = False
            j += 1

# 2. 각 테스트 케이스마다 진행
T = int(input())

for tc in range(1, T + 1):
    d, a, b = map(int, input().split())

    count = 0
    for i in range(a, b + 1):
        if prime[i] and str(d) in str(i):
            # 2-1. a 이상 b 이하 숫자에 대해서 소수인지 검사
            # 2-2. 소수이면 문자열을 통해 d를 포함하는지 검사
            # 위 두가지 조건을 만족하면 count += 1
            count += 1

    print(f"#{tc} {count}")
