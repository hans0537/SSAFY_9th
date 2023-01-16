s = int(input('숫자를 입력해주세요: '))
sum = 0
while s > 0:
    sum += s % 10
    s = s // 10
print(sum)

