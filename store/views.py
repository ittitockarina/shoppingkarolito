from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignInForm, SignUpForm, UpdateUserDataForm, UpdateUserPasswordForm
from .models import StoreProduct
from cart.cart import Cart
from .forms import StoreProductForm, StoreCategoryForm #agregado
from .models import StoreProduct, StoreCategory #agregado

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from .models import Customer
from yuno.customer import create_customer2
import uuid


def addFormErrorsToMessages(request, formErros):
    for errors in formErros.as_data().values():
        for error in errors:
            messages.error(request, error.message)

def about(request):
    return render(request, 'about.html')

def agregar(request):
    return render(request, 'agregar.html')

def home(request):
    store_products = StoreProduct.objects.all()
    return render(request, 'index.html', {
        'store_products': store_products,
    })

def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, 'You have been signed in')
            return redirect('home')
        addFormErrorsToMessages(request, form.errors)

    return render(request, 'sign-in.html', {
        'form': SignInForm(),
    })

def sign_out(request):
    logout(request)
    return redirect('sign_in')

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            merchant_customer_id = str(uuid.uuid4())  # generando un customer_id unico
            
            response = create_customer2(merchant_customer_id, first_name, last_name)

            response_data = response.json()

            if response.status_code == 201:  # Assuming 201 is the success status code
                customerId = response_data.get('id')
                user = form.save()
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    Customer.objects.create(user=user, customer_id=customerId, merchant_order_id=merchant_customer_id)
                    login(request, user)
                    messages.success(request, 'You have been signed up')
                    return redirect('home')
            else:
                messages.error(request, 'Error creating customer in external system')
                return redirect('sign_up')
        addFormErrorsToMessages(request, form.errors)
        return redirect('sign_up')

    return render(request, 'sign-up.html', {
        'form': SignUpForm(),
    })

def store_product(request, pk):
    try:
        cart = Cart(request)
        cart_quantities = cart.get_quantities()
        store_product = StoreProduct.objects.get(id=pk)
        return render(request, 'store-product.html', {
            'store_product': store_product,
            'quantity': cart_quantities.get(str(pk), 1),
        })
    except:
        return redirect('home')

def update_user_data(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        form = UpdateUserDataForm(request.POST or None, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User data has been updated!')
            return redirect('home')
        addFormErrorsToMessages(request, form.errors)
        return render(request, 'update-user-data.html', {
            'form': form,
        })

    return redirect('home')

def update_user_password(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)

        if request.method == 'POST':
            form = UpdateUserPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'User password has been updated!')
                return redirect('sign_in')
            addFormErrorsToMessages(request, form.errors)

        return render(request, 'update-user-password.html', {
            'form': UpdateUserPasswordForm(user),
        })

    return redirect('home')

def edit_product(request, pk):
    product = get_object_or_404(StoreProduct, pk=pk)
    if request.method == 'POST':
        form = StoreProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product has been updated successfully!')
            return redirect('home')  # Redirige a la página de inicio o a la vista de detalle del producto
        addFormErrorsToMessages(request, form.errors)
    else:
        form = StoreProductForm(instance=product)
    
    return render(request, 'admin/edit_product.html', {
        'form': form,
        'product': product,
    })
    
    
 ########################################3

@login_required
def manage_store(request):
    products = StoreProduct.objects.all()
    categories = StoreCategory.objects.all()

    product_form = StoreProductForm(request.POST or None, request.FILES or None)
    category_form = StoreCategoryForm(request.POST or None)

    if request.method == 'POST':
        if 'add_product' in request.POST and product_form.is_valid():
            product_form.save()
            messages.success(request, 'Producto agregado con éxito!')
            return redirect('manage_store')
        elif 'add_category' in request.POST and category_form.is_valid():
            category_form.save()
            messages.success(request, 'Categoría agregada con éxito!')
            return redirect('manage_store')

    return render(request, 'agregar.html', {
        'product_form': product_form,
        'category_form': category_form,
        'products': products,
        'categories': categories,
    })

@login_required
def edit_product(request, product_id):
    product = get_object_or_404(StoreProduct, id=product_id)
    if request.method == 'POST':
        form = StoreProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('manage_store')
    else:
        form = StoreProductForm(instance=product)
    return render(request, 'agregar.html', {'product_form': form, 'product': product})

@login_required
def edit_category(request, category_id):
    category = get_object_or_404(StoreCategory, id=category_id)
    if request.method == 'POST':
        form = StoreCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('manage_store')
    else:
        form = StoreCategoryForm(instance=category)
    return render(request, 'agregar.html', {'category_form': form, 'category': category})

@login_required
def delete_product(request, product_id):
    product = get_object_or_404(StoreProduct, id=product_id)
    product.delete()
    return redirect('manage_store')

@login_required
def delete_category(request, category_id):
    category = get_object_or_404(StoreCategory, id=category_id)
    category.delete()
    return redirect('manage_store')