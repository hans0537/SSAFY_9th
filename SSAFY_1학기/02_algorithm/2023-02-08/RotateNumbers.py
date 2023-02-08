T = int(input())

def rotate90():
    for i in range(N):
        num = ''
        for j in range(N - 1, -1, -1):
            num += str(arr[j][i])
        answer[i][0] = num

def rotate180():
    k = 0
    for i in range(N - 1, -1, -1):
        num = ''
        for j in range(N - 1, -1, -1):
            num += str(arr[i][j])
        answer[k][1] = num
        k += 1

def rotate270():
    k = 0
    for i in range(N - 1, -1, -1):
        num = ''
        for j in range(N):
            num += str(arr[j][i])
        answer[k][2] = num
        k += 1


for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    answer = [[0] * 3 for _ in range(N)]

    rotate90()
    rotate180()
    rotate270()

    print(f'#{tc}')
    for i in range(N):
        for j in range(3):
            print(answer[i][j], end=' ')
        print()
