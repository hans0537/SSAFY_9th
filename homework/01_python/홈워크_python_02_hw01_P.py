orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
o_list = orders.split(',')

print('====광주 3반 CaFE====')
print(f'주문대기 수: {len(o_list)}')

print(f'중복 제거(내림차순) 메뉴 리스트: ')
o_list = sorted(set(o_list), reverse=True)
print(o_list)