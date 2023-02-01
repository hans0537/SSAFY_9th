orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'

orders = orders.split(',')
orders_dic = {}
for i in orders:
    if '아이스' in i:
        if i in orders_dic.keys():
            orders_dic[i] += 1
        else:
            orders_dic[i] = 1
    
for key in orders_dic:
    print(f'{key} : {orders_dic[key]}잔')