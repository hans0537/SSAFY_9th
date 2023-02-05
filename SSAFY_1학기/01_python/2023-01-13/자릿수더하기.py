n = int(input())

# 파이썬의 내장함수중에 sum 이라는 함수가 있다.
sum_n = 0
# 내장함수와 내가 만든 변수의 이름이 같으면
# 원래 내장함수를 사용할수 없게 되어버린다.

while n > 0:
    sum_n += n%10
    n = n // 10

print(sum_n)


