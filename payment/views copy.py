from .forms import PaymentCardForm, ShippingInformationForm
from store.models import StoreOrder, StoreOrderItem, StoreProduct
from cart.cart import Cart

from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render

def addFormErrorsToMessages(request, formErros):
    for errors in formErros.as_data().values():
        for error in errors:
            messages.error(request, error.message)

def billing_information(request):
    if request.user.is_authenticated:
        cart = Cart(request)
        cart_shipping_information = cart.get_shipping_information()
        if not cart_shipping_information:
            return redirect('add_shipping_information')
        cart_payment_card = cart.get_payment_card()
        if not cart_payment_card:
            return redirect('payment_card')
        cart_store_products = cart.get_store_products()
        cart_quantities = cart.get_quantities()
        total = cart.total()
        return render(request, 'billing-information.html', {
            'cart_payment_card': cart_payment_card,
            'cart_shipping_information': cart_shipping_information,
            'cart_store_products': cart_store_products,
            'cart_quantities': cart_quantities,
            'total': total,
        })

    return redirect('sign_in')

def payment_card(request):
    if request.user.is_authenticated:
        cart = Cart(request)
        cart_payment_card = cart.get_payment_card()
        if request.method == 'POST':
            form = PaymentCardForm(request.POST or None)
            if form.is_valid():
                cart.set_payment_card(form.cleaned_data.get('cvc'), form.cleaned_data.get('date'), form.cleaned_data.get('number'))
                return redirect('billing_information')
            addFormErrorsToMessages(request, form.errors)

        return render(request, 'payment-card.html', {
            'form': PaymentCardForm(cart_payment_card or None),
        })

    return redirect('sign_in')

def add_shipping_information(request):
    if request.user.is_authenticated:
        cart = Cart(request)
        cart_shipping_information = cart.get_shipping_information()
        if request.method == 'POST':
            form = ShippingInformationForm(request.POST or None)
            if form.is_valid():
                cart.set_shipping_information(form.cleaned_data.get('address'), form.cleaned_data.get('phone_number'))
                return redirect('payment_card')
            addFormErrorsToMessages(request, form.errors)

        return render(request, 'shipping-information.html', {
            'form': ShippingInformationForm(cart_shipping_information or None),
        })

    return redirect('sign_in')

def checkout(request):
    if request.user.is_authenticated:
        cart = Cart(request)
        cart_store_products = cart.get_store_products()
        cart_quantities = cart.get_quantities()
        total = cart.total()
        return render(request, 'checkout.html', {
            'cart_store_products': cart_store_products,
            'cart_quantities': cart_quantities,
            'total': total,
        })

    return redirect('sign_in')

def pay_now(request):
    if request.user.is_authenticated:
        cart = Cart(request)
        cart_payment_card = cart.get_payment_card()
        cart_shipping_information = cart.get_shipping_information()
        cart_store_products = cart.get_store_products()
        cart_quantities = cart.get_quantities()
        total = cart.total()

        cart_store_products_lines = []

        store_order = StoreOrder.objects.create(
            address=cart_shipping_information.get('address'),
            amount_paid=total,
            customer=request.user,
            phone_number=cart_shipping_information.get('phone_number'),
        )

        for cart_store_product in cart_store_products:
            quantity = cart_quantities.get(str(cart_store_product.id))

            StoreOrderItem.objects.create(
                order=store_order,
                product=cart_store_product,
                quantity=quantity,
            )

            store_product = StoreProduct.objects.get(pk=cart_store_product.id)
            store_product.quantity -= quantity
            store_product.save()

            cart_store_products_lines.append(f'{cart_store_product.name}: ({quantity}) * ${cart_store_product.price}')
            cart.delete(cart_store_product.id)

        send_mail(
            f'Store - Billing information #{store_order.id}',
            '\n'.join([
                f'Username: {request.user.username}',
                f'Email Address: {request.user.email}',
                f'First Name: {request.user.first_name}',
                f'Last Name: {request.user.last_name}',
                f'Address: {cart_shipping_information.get("address")}',
                f'Phone Number: {cart_shipping_information.get("phone_number")}',
                f'Total: ${total}',
                '',
                f'Card CVC: {cart_payment_card.get("cvc")}',
                f'Card Date: {cart_payment_card.get("date")}',
                f'Card Number: {cart_payment_card.get("number")}',
                '',
            ] + cart_store_products_lines),
            'ittitoc@ulasalle.edu.pe',
            ['ittitoc@ulasalle.edu.pe'],
            fail_silently=False,
        )

        messages.success(request, f'An email has been sent to {request.user.email}')

        return redirect('home')

    return redirect('sign_in')
