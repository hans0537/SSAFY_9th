def msort(s, e):
    if s == e:
        return

    m = (s + e) // 2
    msort(s, m)
    msort(m + 1, e)

    # merge 작업
    k = 0
    l, r = s, m + 1     # 왼쪽과 오른쪽에서 가장 자근 숫자의 위치
    while l <= m or r <= e:
        if l <= m and r <= e:
            if arr[l] <= arr[r]:
                tmp[k] = arr[l]
                l += 1
            else:
                tmp[k] = arr[r]
                r += 1
            k += 1
        elif l <= m:    # 왼쪽 부분이 남아 있으면
            while l <= m:
                tmp[k] = arr[l]
                k += 1
                l += 1
        elif r <= e:    # 오른쪽 부분이 남아 있으면
            while r <= e:
                tmp[k] = arr[r]
                k += 1
                r += 1

    i = 0
    while i < k:
        arr[s + i] = tmp[i]
        i += 1
    return

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    tmp = [0] * N
    msort(0, N - 1)
    print(arr)