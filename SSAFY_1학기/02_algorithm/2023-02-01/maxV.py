'''
3
5
55 7 78 12 42
6
12 3 40 2 4 8
7
31 2 90 54 88 4 3
'''

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    maxV = arr[0]
    for i in arr:
        if maxV < i:
            maxV = i

    print(f"#{tc} {maxV}")
