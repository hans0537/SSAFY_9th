def maxCost(grain_lst):
    
    # 높은 가격을 찾을 변수 설정
    # 일단 초기값 저장
    max_cost = grain_lst[0][1]
    # 높은 가격을 가진 과일을 저장할 변수
    # 일단 초기값 저장
    max_fruit = grain_lst[0][0]
    
    for fruit, cost in grain_lst:
        if cost > max_cost:
            max_cost = cost
            max_fruit = fruit

    return max_fruit

grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]
print(maxCost(grain_lst))
