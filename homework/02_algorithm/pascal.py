T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    pascal = [[0] * N for _ in range(N)]
    for i in range(N):
        # n 번째 줄에는 n개의 숫자가 들어간다
        for j in range(i + 1):
            # 처음과 끝에는 1을 넣어준다
            if j == 0 or j == i:
                pascal[i][j] = 1
            else:
                # 그다음 부분은 위에 줄의 왼쪽과 오른쪽을 더해준 값을 넣는다
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

    print(f'#{tc}')

    for i in pascal:
        for j in i:
            if j:
                print(j, end=' ')
        print()






