num = 0

try:
    # print(10/0)
    my_list = []
    my_list[2]
except ZeroDivisionError:
    print("0으로 나눌수는 없습니다")
except Exception:
    print("예외 발생")


print(num)