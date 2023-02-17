T = int(input())
for tc in range(1, T + 1):
    mem = input()
    bit = ['0'] * len(mem)
    cnt = 0
    for i in range(len(mem)):
        if mem[i] != bit[i]:
            bit[i:] = mem[i] * len(bit[i:])
            cnt += 1

    print(f'#{tc} {cnt}')