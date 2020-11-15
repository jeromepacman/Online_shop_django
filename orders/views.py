from django.shortcuts import render, redirect
from django.contrib import messages

from cart.cart import Cart
from . forms import OrderCreateForm
from . models import OrderItem


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'],
                                         quantity=item['quantity'])

            cart.clear()
            messages.success(request, "Votre commande est maintenant validée !")
            return redirect("/")
    else:
        form = OrderCreateForm()
    return render(request, 'create_order.html', {'cart': cart, 'form': form})
