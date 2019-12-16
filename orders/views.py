from datetime import date
from django.http import JsonResponse
from django.shortcuts import render
from .models import OrderDetails, Order
from catalog.models import Product


# Create your views here.
def add(request):
    sess_key = request.session.session_key
    user = request.user
    return_dict = dict()
    data = request.POST
    product_id = data.get('product_id')
    amount = int(data.get('amount'))
    price = float(data.get('price'))
    sum = float(price * amount / 100)

    order = Order.objects.filter(order_id=1)
    print(user)
    if len(order) == 0:
        if user.is_anonymous:
            Order.objects.create(order_id=1, order_date=date.today(), summa=0, customer=1,
                                 session_key=sess_key)  # order for admin
        else:
            Order.objects.create(order_id=1, order_date=date.today(), summa=0, customer=user, session_key=sess_key)
    else:
        if user.is_anonymous:
            if order[0].session_key != sess_key:
                order[0].delete()
                Order.objects.create(order_id=1, order_date=date.today(), summa=0, customer=1,
                                     session_key=sess_key)  # order for admin
        elif order[0].customer != user:
            order[0].delete()
            Order.objects.create(order_id=1, order_date=date.today(), summa=0, customer=user,
                                 session_key=sess_key)

    product = Product.objects.get(product_id=product_id)
    OrderDetails.objects.create(order=order[0], product=product, product_amount=amount, summa=sum)

    return JsonResponse(return_dict)
