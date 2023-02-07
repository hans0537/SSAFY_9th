def sequentialSearch(a, n, key):
    i = 0
    while i < n and a[i] != key:
        i += 1
        if i < n:
            return i
        else:
            return -1

a = [3, 4, 1, 10, 5, 19, 123]
print(sequentialSearch(a, len(a), 123))