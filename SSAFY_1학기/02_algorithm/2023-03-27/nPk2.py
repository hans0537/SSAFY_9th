def perm(i, k):     # k 결정할 개수
    if i == k:
        print(*p)
    else:
        for j in range(k):   # 사용하지 않은 숫자를
            if not used[j]:
                p[i] = A[j]
                used[j] = 1
                perm(i + 1, k)
                used[j] = 0

A = [1, 4, 5]
p = [0] * 3
used = [0] * 3
perm(0, 3)