from . import views

from django.urls import path

urlpatterns = [
		path('billing-information/', views.billing_information, name='billing_information'),
		path('checkout/', views.checkout, name='checkout'),
		path('card/', views.payment_card, name='payment_card'),
		path('pay-now/', views.pay_now, name='pay_now'),
		path('shipping-information/', views.add_shipping_information, name='add_shipping_information'),
]
