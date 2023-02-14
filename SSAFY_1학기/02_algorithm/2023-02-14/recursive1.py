def f(i, k):
    if i == k:      # 목표에 도달하면
        print(B)
        return
    else:
        B[i] = A[i]
        f(i + 1, k)

A = [10, 20, 30]
B = [0] * 3
f(0, 3)

# 생각보다 재귀의 깊이가 깊지 않다
# A = [i for i in range(1000)]
# B = [0] * 1000
# f(0, 1000)