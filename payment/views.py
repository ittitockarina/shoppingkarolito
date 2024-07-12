import requests
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import PaymentCardForm, ShippingInformationForm
from store.models import StoreOrder, StoreOrderItem, StoreProduct
from cart.cart import Cart
import uuid

def addFormErrorsToMessages(request, form_errors):
    for errors in form_errors.as_data().values():
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

def create_customer(cart_shipping_information, user):
    url = "https://api-sandbox.y.uno/v1/customers"
    payload = {
        "document": {
            "document_number": "1093333333",
            "document_type": "CC"
        },
        "phone": {
            "country_code": "57",
            "number": "3132450765"
        },
        "billing_address": {
            "country": "PE",
            "address_line_1": cart_shipping_information.get('address'),
            "address_line_2": "Apartamento 502, Torre I",
            "city": "Bogotá",
            "state": "Cundinamarca",
            "zip_code": "111111",
            "neighborhood": "Comuna 2"
        },
        "shipping_address": {
            "country": "EC",
            "address_line_1": cart_shipping_information.get('address'),
            "address_line_2": "Apartamento 502, Torre I",
            "city": "Bogotá",
            "state": "Cundinamarca",
            "zip_code": "111111",
            "neighborhood": "Comuna 2"
        },
        "merchant_customer_id": str(user.id),
        "merchant_customer_created_at": user.date_joined.isoformat(),
        "first_name": user.first_name,
        "last_name": user.last_name,
        "gender": "M",
        "date_of_birth": "1990-02-28",
        "email": user.email,
        "nationality": "CO",
        "country": "CO",
        "metadata": [
            {"key": "ID", "value": "123456"},
            {"value": "123456", "key": "ID"}
        ]
    }
    headers = {
        "accept": "application/json",
        "charset": "utf-8",
        "content-type": "application/json",
        "public-api-key": "sandbox_gAAAAABmULQZqNYRmMEyeutiZ7MLxBKbCHzWcUKdq8F53eVHXX_D6vsZvpItVyUxVYXQODe3wRIJqJVEdUS-WnXEOmHxO9saxwwIjdbBhJC0SWKzP7hkT5sz4w5suhM9BRDkZg-d6uqQWuigUklLZxTsFPyFdzeD5jaZ4kKrfIASNkJ4i3CNupR6m5-9p7T4WzW_24wxrgLwCBymZIFK7_N7Be92icuGiUwyvxpej1zGKyRc81fhQiY-sY9ncu2E0CgcVM3O6-ni",
        "private-secret-key": "gAAAAABmULQZJCFTJnM-rHEY11P-Mz3aihCmwcwoMRYGeO1JBT7hwZAuo4D5CT_RuuM6obEUJXW1leGVRWiu9BokV4WBRUqQSF78es0CFwhQVVXaS_ezW0h7Pl1P7J4CR7oKGtvp9mZ-1RNXgxyZC2MG0GKdIEeXq7rruJokpaLwCeSYU7hwzrPwxJJ7Z4Ftupy3dS7i8RkNAwqwoTFfzHIVX6fqJKw6wtcrhxlrFK01JaZ71Twp_McjTLCQ-zldKPy63-fW7dWj"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json().get('id')

def create_checkout_session(customer_id, total):
    url = "https://api-sandbox.y.uno/v1/checkout/sessions"
    payload = {
        "country": "AR",
        "amount": {
            "currency": "ARS",
            "value": total
        },
        "installments": {"plan_id": "7b70350a-0d08-4f2f-be84-6423273aec7c"},
        "customer_id": customer_id,
        "merchant_order_id": str(uuid.uuid4()),
        "payment_description": "Payment Description",
        "callback_url": "www.y.uno",
        "account_id": "d06a2605-85d3-4a3f-a86b-b5750feb1b09",
        "metadata": [{"key": "ID", "value": "123456"}]
    }
    headers = {
        "accept": "application/json",
        "charset": "utf-8",
        "content-type": "application/json",
        "public-api-key": "sandbox_gAAAAABmULQZqNYRmMEyeutiZ7MLxBKbCHzWcUKdq8F53eVHXX_D6vsZvpItVyUxVYXQODe3wRIJqJVEdUS-WnXEOmHxO9saxwwIjdbBhJC0SWKzP7hkT5sz4w5suhM9BRDkZg-d6uqQWuigUklLZxTsFPyFdzeD5jaZ4kKrfIASNkJ4i3CNupR6m5-9p7T4WzW_24wxrgLwCBymZIFK7_N7Be92icuGiUwyvxpej1zGKyRc81fhQiY-sY9ncu2E0CgcVM3O6-ni",
        "private-secret-key": "gAAAAABmULQZJCFTJnM-rHEY11P-Mz3aihCmwcwoMRYGeO1JBT7hwZAuo4D5CT_RuuM6obEUJXW1leGVRWiu9BokV4WBRUqQSF78es0CFwhQVVXaS_ezW0h7Pl1P7J4CR7oKGtvp9mZ-1RNXgxyZC2MG0GKdIEeXq7rruJokpaLwCeSYU7hwzrPwxJJ7Z4Ftupy3dS7i8RkNAwqwoTFfzHIVX6fqJKw6wtcrhxlrFK01JaZ71Twp_McjTLCQ-zldKPy63-fW7dWj"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json().get('id')

def create_payment(checkout_session, customer_id, total, cart_shipping_information, user):
    url = "https://api-sandbox.y.uno/v1/payments"
    payload = {
        "country": "CO",
        "amount": {
            "currency": "ARS",
            "value": total
        },
        "customer_payer": {
            "document": {"document_number": "351.040.753-97"},
            "billing_address": {
                "address_line_1": cart_shipping_information.get('address'),
                "city": "Bogota",
                "country": "BR",
                "state": "Cundinamarca",
                "zip_code": "111111",
                "neighborhood": "Barrio 11"
            },
            "shipping_address": {
                "address_line_1": cart_shipping_information.get('address'),
                "city": "Bogota",
                "country": "CO"
            },
            "id": customer_id,
            "merchant_customer_id": str(user.id),
            "first_name": user.first_name,
            "last_name": user.last_name,
            "gender": "M",
            "date_of_birth": "1990-02-28",
            "email": user.email,
            "nationality": "CO",
            "ip_address": "192.168.123.167",
            "device_fingerprint": "hi88287gbd8d7d782ge"
        },
        "checkout": {"session": checkout_session},
        "workflow": "DIRECT",
        "payment_method": {
            "detail": {"card": {"verify": False}},
            "type": "EFECTY"
        },
        "account_id": "d06a2605-85d3-4a3f-a86b-b5750feb1b09",
        "description": "Test Payment",
        "merchant_order_id": "AA01",
        "merchant_reference": "Test_AAB",
        "callback_url": "www.y.uno",
        "metadata": [{"key": "ID", "value": "SD00"}]
    }
    headers = {
        "accept": "application/json",
        "charset": "utf-8",
        "content-type": "application/json",
        "public-api-key": "sandbox_gAAAAABmULQZqNYRmMEyeutiZ7MLxBKbCHzWcUKdq8F53eVHXX_D6vsZvpItVyUxVYXQODe3wRIJqJVEdUS-WnXEOmHxO9saxwwIjdbBhJC0SWKzP7hkT5sz4w5suhM9BRDkZg-d6uqQWuigUklLZxTsFPyFdzeD5jaZ4kKrfIASNkJ4i3CNupR6m5-9p7T4WzW_24wxrgLwCBymZIFK7_N7Be92icuGiUwyvxpej1zGKyRc81fhQiY-sY9ncu2E0CgcVM3O6-ni",
        "private-secret-key": "gAAAAABmULQZJCFTJnM-rHEY11P-Mz3aihCmwcwoMRYGeO1JBT7hwZAuo4D5CT_RuuM6obEUJXW1leGVRWiu9BokV4WBRUqQSF78es0CFwhQVVXaS_ezW0h7Pl1P7J4CR7oKGtvp9mZ-1RNXgxyZC2MG0GKdIEeXq7rruJokpaLwCeSYU7hwzrPwxJJ7Z4Ftupy3dS7i8RkNAwqwoTFfzHIVX6fqJKw6wtcrhxlrFK01JaZ71Twp_McjTLCQ-zldKPy63-fW7dWj",
        "X-Idempotency-Key": str(uuid.uuid4())
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

def pay_now(request):
    if request.user.is_authenticated:
        cart = Cart(request)
        cart_payment_card = cart.get_payment_card()
        cart_shipping_information = cart.get_shipping_information()
        cart_store_products = cart.get_store_products()
        cart_quantities = cart.get_quantities()
        total = cart.total()

        customer_id = create_customer(cart_shipping_information, request.user)
        checkout_session_id = create_checkout_session(customer_id, total)
        payment_response = create_payment(checkout_session_id, customer_id, total, cart_shipping_information, request.user)

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

            cart.delete(cart_store_product.id)

        send_mail(
            f'Store - Billing information #{store_order.id}',
            f'''
            Username: {request.user.username}
            Email Address: {request.user.email}
            First Name: {request.user.first_name}
            Last Name: {request.user.last_name}
            Address: {cart_shipping_information.get("address")}
            Phone Number: {cart_shipping_information.get("phone_number")}
            Total: ${total}

            Card CVC: {cart_payment_card.get("cvc")}
            Card Date: {cart_payment_card.get("date")}
            Card Number: {cart_payment_card.get("number")}
            ''',
            'ittitoc@ulasalle.edu.pe',
            ['ittitoc@ulasalle.edu.pe'],
            fail_silently=False,
        )

        messages.success(request, f'An email has been sent to {request.user.email}')
        return redirect('home')

    return redirect('sign_in')
