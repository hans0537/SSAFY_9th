def solution(n):
    l = len(n) * 4
    x = int(n, 16)

    ans = ''
    for i in range(l - 1, -1, -7):
        bin = ''
        for j in range(7):
            if i - j < 0:
                break
            print(i-j, 1 << i - j)
            # bin += '1' if x & (1 << i - j)

h1 = '0F97A3'
h2 = '01D06079861D79F99F'
solution(h1)
solution(h2)