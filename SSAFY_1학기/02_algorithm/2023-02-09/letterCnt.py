from collections import Counter
T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()

    str1 = set(str1)
    str2 = Counter(str2)
    max = -1e9
    for i in str1:
        if max < str2.get(i):
            max = str2.get(i)

    print(f'#{tc} {max}')