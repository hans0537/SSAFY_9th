T = int(input())
for tc in range(1, T + 1):
    A, B = input().split()
    a = len(A)
    b = len(B)
    cnt = 0
    i = 0
    while i < a:
        if A[i] == B[0] and A[i:i+b] == B:
            cnt += 1
            i += b
        else:
            cnt += 1
            i += 1
    print(f'#{tc} {cnt}')