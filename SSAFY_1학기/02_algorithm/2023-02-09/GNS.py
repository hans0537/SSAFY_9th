numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

T = int(input())

for tc in range(1, T + 1):
    _, n = input().split()
    n = int(n)

    text = input().split()

    numbers_cnt = [0] * 10

    # 카운트 배열
    for number in text:
        for i in range(10):
            if number == numbers[i]:
                numbers_cnt[i] += 1

    answer = ""
    for i in range(10):
        answer += (numbers[i] + " ") * numbers_cnt[i]
    print(f"#{tc}")
    print(answer)
