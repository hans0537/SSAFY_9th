T = int(input())
def partition(l, r):
    p = lst[l]
    i, j = l, r
    while i <= j:
        while i <= j and lst[i] <= p:
            i += 1
        while i <= j and lst[j] >= p:
            j -= 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]

    lst[l], lst[j] = lst[j], lst[l]
    return j

def quickSort(l, r):
    if l < r:
        s = partition(l, r)
        quickSort(l, s - 1)
        quickSort(s + 1, r)

for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    quickSort(0, N - 1)
    print('#{} {}'.format(tc, lst[N // 2]))
