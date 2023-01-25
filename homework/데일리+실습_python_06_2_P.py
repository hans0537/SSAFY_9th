def maxCost(grain_lst):
    
    # 높은 가격을 찾을 변수 설정
    max_cost = -1e9
    # 높은 가격을 가진 과일을 저장할 변수
    max_fruit = ''

    for fruit, cost in grain_lst:
        if cost > max_cost:
            max_cost = cost
            max_fruit = fruit

    return max_fruit

grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]
print(maxCost(grain_lst))
