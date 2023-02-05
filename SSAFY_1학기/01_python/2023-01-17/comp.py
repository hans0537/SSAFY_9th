my_list = [num ** 2 for num in range(1, 11) if num % 2 == 0]

print(my_list)

my_dict = {num: num ** 2 for num in range(1, 11) if num % 2 == 0}

print(my_dict)

n = 4

# match n:
#     case 1:
#         print("n is 1")
#     case 2:
#         print("n is 2")
#     case _:
#         print("not matched", n)
