numbers = [1,2,3,4,5]
# selected[i] == 1 => i번째 원소를 부분집합에 포함 O
# selected[i] == 0 => i번째 원소를 부분집합에 포함 X
selected = [0] * 5

n = len(numbers)
# 합이 x 보다 작은 부분집합만 구해야 한다면?
x = 10


# 재귀함수로 부분집합 구하기
# i 번째 원소를 부분집합에 포함 할지 안할지 결정
def subset(i, subsum):
    # 0. 다른 조건(최적화 조건) 이 있는 경우
    if subsum >= x:
        return

    # 1. 종료 조건
    if i == n:
        # n개의 원소에 대해 선택을 끝냈다. (고르든지 말든지)
        for j in range(n):
            if selected[j]:
                print(numbers[j], end=" ")
        print()
        print("========================")
        return

    # 2. 재귀 호출
    # i번째 원소를 선택하고(부분집합에 포함) 다음 i+1번쨰 원소를 선택하러 가거나
    selected[i] = 1
    subset(i + 1, subsum + numbers[i])
    # i번째 원소를 선택하지 않고(부분집합에 포함하지 않음) 다음 i+1번째 원소를 선택하러 가거나
    selected[i] = 0
    subset(i + 1, subsum)

subset(0)