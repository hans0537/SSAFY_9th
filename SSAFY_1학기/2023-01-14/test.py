import builtins

print("출력")
print = 10

# 빌트인 함수(내장함수)를 변수로 바꾼다음 복원하는 방법
print = builtins.print

print("출력2")