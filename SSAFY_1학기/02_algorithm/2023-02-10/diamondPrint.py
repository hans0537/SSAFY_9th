T = int(input())
def diamond(shape):
    for i in range(n):
        print(shape, end='')
        if i == n - 1:
            print(shape[0])

for tc in range(1, T + 1):
    s = input()
    n = len(s)

    diamond('..#.')
    diamond('.#.#')
    for i in range(n):
        print(f'#.{s[i]}.', end='')
        if i == n - 1:
            print('#')
    diamond('.#.#')
    diamond('..#.')
