from django.shortcuts import render

# Create your views here.
def price(request, thing, cnt):
    product_price = {"라면":980,"홈런볼":1500,"칙촉":2300, "식빵":1800}
    amount = 0
    msg = ''
    context = {}

    if thing in product_price:
        amount += product_price.get(thing) * cnt
        msg += f'{thing} {cnt}개의 가격은 {amount}원 입니다.'
    else:
        msg += f'{thing}은/는 없어용'

    context['msg'] = msg

    return render(request, 'prices/price.html', context)