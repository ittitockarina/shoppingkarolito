from . import views

from django.urls import path

urlpatterns = [
	  path('', views.show_cart, name='show_cart'),
	  path('add-store-product/', views.add_store_product, name='add_store_product'),
    path('delete-store-product/', views.delete_store_product, name='delete_store_product'),
]
