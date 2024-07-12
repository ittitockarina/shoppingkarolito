from .cart import Cart
from store.models import StoreProduct

from django.shortcuts import get_object_or_404, redirect, render

def show_cart(request):
    cart = Cart(request)
    cart_store_products = cart.get_store_products()
    cart_quantities = cart.get_quantities()
    total = cart.total()
    return render(request, 'cart.html', {
        'cart_store_products': cart_store_products,
        'cart_quantities': cart_quantities,
        'total': total,
    })

def add_store_product(request):
    if request.method == 'POST':
        cart = Cart(request)
        quantity = int(request.POST['quantity'])
        store_product_id = int(request.POST['store_product_id'])
        store_product = get_object_or_404(StoreProduct, id=store_product_id)
        cart.add(store_product, quantity)
        return redirect('show_cart')

def delete_store_product(request):
    if request.method == 'POST':
        cart = Cart(request)
        store_product_id = int(request.POST['store_product_id'])
        cart.delete(store_product_id)
        return redirect('show_cart')

