# prime number 소수 구하기

# 1 부터 1000까지의 수중에 소수를 출력하시오
# 1 보다 큰 수중에서 약수를 1과 자기 자신만 가지는 수를 소수
'''
에라토스테네스의 체
1. 2 부터 소스를 구하고자 하는 구간의 모든 수를 나열
2. 2는 소수이므로 2는 소수로 체크하고, 2를 제외한 자기 자신의 배수를 모두 소수가 아니라고 체크
3. 다음 수로 이동(체크가 안된 수로), 3 은 소수이므로 소수로 체크, 3을 제외한 자기 자신의 배수를 모두 소수가 아니라고 체크
4. 위의 과정을 계속 반복하면 원하는 구간의 소수가 남게 된다.
'''
prime = []
for i in range(2, 1000):
    # i를 기준으로 해서 i를 j로 나눴을때 나머지가 0이면 배수 ==> 체크
    # j의 범위는 2 <= j < i
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime.append(i)

n = 1000  # 2 부터 1000까지의 모든 수에 대하여 소수 판별
is_prime = [True for i in range(n + 1)]  # 처음엔 모든 수가 소수인 것으로 초기화

for i in range(2, int(n ** 0.5) + 1):  # 2부터 n의 제곱근까지만 확인해도 된다.
    if is_prime[i]:  # i가 소수인 경우
        # i를 제외한 모든 i의 배수를 지우면 된다. (False로 체크)
        j = 2
        while i * j <= n:
            is_prime[i * j] = False
            j += 1

print(prime)
print(is_prime[2:])
print(is_prime[23])