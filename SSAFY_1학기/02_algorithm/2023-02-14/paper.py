T = int(input())

def p(n):
    n //= 10
    f = [0] * (n + 1)
    f[0] = 1
    f[1] = 1
    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2] * 2

    return f[n]

# def p(n):
#     # 0이면 10 과 20으로 갈라진것
#     if n == 0:
#         return 1
#     # 음수이면 갈라짐 실패
#     if n < 0:
#         return 0
#     # 20은 가로 10이 두개 이므로 2를 곱해준 리턴
#     return p(n - 10) + p(n - 20) * 2

for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc} {p(N)}')