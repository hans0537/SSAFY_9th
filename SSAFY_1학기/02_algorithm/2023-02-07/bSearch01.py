T = int(input())

def bSearch(n):
    res = 1
    start = 1
    end = P
    while start <= end:
        mid = int((start+end)/2)

        if mid == n:
            return res
        elif mid > n:
            end = mid
        else:
            start = mid
        res += 1
    return res

for tc in range(1, T + 1):
    P, A, B = map(int, input().split())

    pa = bSearch(A)
    pb = bSearch(B)

    if pa < pb:
        print(f"#{tc} A")
    elif pa > pb:
        print(f"#{tc} B")
    else:
        print(f"#{tc} 0")
