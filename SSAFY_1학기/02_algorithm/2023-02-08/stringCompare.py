T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    print(str1, str2)
    print(f'#{tc} 1') if str1 in str2 else print(f'#{tc} 0')