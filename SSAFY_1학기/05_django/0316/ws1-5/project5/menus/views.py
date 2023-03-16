from django.shortcuts import render

# Create your views here.
foods = ["피자", "치킨", "국밥", "초밥", "민초흑당로제마라탕"]
drinks = ["cider", "coke", "miranda", "fanta", "eye of finetree"]

def food(request):
    content = {
        'food' : foods
    }
    return render(request, 'menus/food.html', content)

def drink(request):
    content = {
        'drink' : drinks
    }
    return render(request, 'menus/drink.html', content)

def receipt(request):
    order = request.GET.get("order").lower()
    print(order)
    print(foods)
    check = -1
    print(order in foods)
    if order in foods or order in drinks:
        check = 1

    content = {
        'check' : check,
        'order' : order
    }    

    return render(request, 'menus/receipt.html', content)