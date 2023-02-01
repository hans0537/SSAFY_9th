# TOOLS 로 부터 가져오기
# calc 폴더 내에 __init__.py 파일이 있으면 외부에서 불러서 사용가능
from calc import tools

print(tools.add(1, 2))
print(tools.sub(2, 1))

# 함수를 바로 사용하려면 아래와 같이 임포트
# from calc.tools import add, sub

# print(add(1, 2))
# print(sub(1, 2))

