# op = input()

# == : 같다
# != : 같지 않다

# if op != "+":
#     print("덧셈이 아니다")

# 숫자 두개 입력 할때 둘다 0이면 종료
# 반복을 종료한는 방법은 break

import math

while True:
    print("==================")
    print("계산기 프로그램!!!")
    print("1. 실행 \n2. 종료")
    sel = int(input("선택: "))
    if sel == 1:
        while True:
            print("=================")
            print("1. 사칙연산 \n2. 다른거...\n0. 뒤로")

            sel1 = int(input("선택: "))
            
            if sel1 == 1:
                print("=================")
                a = int(input("첫번째 숫자 입력: "))
                b = int(input("두번째 숫자 입력: "))
                c = input("사칙연산(+, - , /, *, %) 입력: ")
                
                if a == 0 and b == 0:
                    break

                if c == "+":
                    print(f"{a} + {b} = {a+b}")
                elif c == "-":
                    print(f"{a} - {b} = {a-b}")
                elif c == "/":
                    if(b == 0):
                        print("0으로 나눌수 없음")
                    else:
                        print(f"{a} / {b} = {a/b}")
                elif c == "*":
                    print(f"{a} X {b} = {a*b}")
                elif c == "%":
                    if(b == 0):
                        print("0으로 나눌수 없음")
                    else:
                        print(f"{a} % {b} = {a%b}")
            elif sel1 == 2:
                print("=================")
                print("1. 루트\n2. 제곱근\n3. 제곱\n4. log10\n5. log2\n0. 뒤로")
                sel2 = int(input("선택: "))
                

                if sel2 == 1:
                    a = int(input("숫자 입력: "))
                    print(f"{a}의 루트는: {math.sqrt(a)}")
                if sel2 == 2:
                    a = int(input("숫자 입력: "))
                    b = int(input("숫자 입력: "))
                    print(f"{a}의 {b}제곱근은: {a**(1/b)}")
                elif sel2 == 3:
                    a = int(input("숫자 입력: "))
                    b = int(input("제곱 숫자 입력: "))
                    print(f"{a}의 {b}제곱: {math.pow(a, b)}")
                elif sel2 == 4:
                    a = int(input("숫자 입력: "))
                    print(f"log10{a} = {math.log10(a)}")
                elif sel2 == 5:
                    a = int(input("숫자 입력: "))
                    print(f"log2{a} = {math.log2(a)}")
                elif sel2 == 0:
                    break
                else:
                    print("1,2,3,4,0 숫자만 입력하세요!")
            elif sel1 == 0:
                break
            else:
                print("1,2,0 만 선택하세요!")
    elif sel == 2:
        print("프로그램 종료")
        break
    else:
        print("1, 2번만 선택하세요")