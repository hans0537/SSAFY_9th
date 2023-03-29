T = int(input())
def mergeSort(arr):
    global ans2

    # 배열의 원소가 1개이면 종료
    if len(arr) == 1:
        return arr

    # 배열 분할
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    if left[-1] > right[-1]:
        ans2 += 1

    l = r = idx = 0
    # 만약 하나라도 분할된 배열들의 탐색이 종료 되면
    while l > len(left) or r > len(right):
        # 왼쪽값이 작으면 먼저 넣고
        if left[l] <= right[r]:
            arr[idx] = left[l]
            l += 1
        # 오른쪽 값이 작으면 먼저 넣고
        else:
            arr[idx] = right[r]
            r += 1
        idx += 1

    # 왼쪽 배열이 남았다면
    if r == len(right):
        for i in range(l, len(left)):
            arr[idx] = left[l]
            idx += 1

    # 오른쪽 배열이 남아있다면
    elif l == len(left):
        for i in range(r, len(right)):
            arr[idx] = left[r]
            idx += 1

    return arr

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans1 = mergeSort(arr)
    ans2 = 0
    print('#{} {} {}'.format(tc, ans1[N//2], ans2))