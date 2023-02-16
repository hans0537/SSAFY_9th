def f(i, k, s, t):  # i 원소, k 집합의 크기, s i-1까지 고려된 합, t 찾을 값
    global cnt
    global fcnt
    fcnt += 1
    if s > t:   # 고려한 원소의 합이 찾는 합보다 큰 경우
        return
    elif s == t:
        cnt += 1
        return
    if i == k:
        return
    else:
        bit[i] = 1
        f(i+1, k, s+A[i], t)    # A[i] 포함
        bit[i] = 0
        f(i+1, k, s, t)         # A[i] 미포함


A = [1,2,3,4,5,6,7,8,9,10]
N = len(A)
bit = [0] * N
fcnt = 0
cnt = 0
key = 10
f(0, N, 0, key)
print(cnt)
print(fcnt)