s = input('숫자를 입력해주세요: ')

# 방법 1
s = int(s)
sum = 0
while s > 0:
    sum += s % 10
    s = s // 10
print(sum)

"""
# 방법2
s = list(map(int, s))
print(s)
print(sum(s))
"""


