T = int(input())

for tc in range(1, T + 1):
    n, hex_num = input().split()

    n = int(n)

    print(f"#{tc}", end=" ")

    for i in range(n):
        num = int(hex_num[i], 16)  # 10 진수로 바꾸고
        # 16진수 => 2진수 * 4
        # 3번, 2번, 1번, 0번 비트 검사해서 1 포함하면 1 아니면 0
        for j in range(3, -1, -1):
            if num & (2 ** j) == 0:
                # num & (2**j) == 1 : num의 j번째 비트에 1이 있는지 검사
                print("0", end="")
            else:
                print("1", end="")
    print()
