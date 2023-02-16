def f(i, k, key):
    if i == k:  # 하나의 부분집합 완성
        tot = 0
        for j in range(k):
            if bit[j]:
                tot += A[j]     # 부분 집합의 합
                # print(A[j], end=' ')
        if tot == key:
            return 1
        return 0
        # if tot == key:    # 부분집합의 합이 key와 같은 집합 출력
        #     for j in range(k):
        #         if bit[j]:
        #             print(A[j], end=' ')
        #     print()
        # print('합:', tot)
        # print(bit)
    else:
        bit[i] = 1
        f(i + 1, k, key)
        bit[i] = 0
        f(i + 1, k, key)


A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * 10
f(0, 10, 10)
