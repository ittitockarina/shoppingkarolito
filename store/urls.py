from . import views

from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('sign-in/', views.sign_in, name='sign_in'),
    path('sign-out/', views.sign_out, name='sign_out'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('store-product/<int:pk>/', views.store_product, name='store_product'),
    path('update-user-data/', views.update_user_data, name='update_user_data'),
    path('update-user-password/', views.update_user_password, name='update_user_password'),
    path('edit-product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('manage-store/', views.manage_store, name='manage_store'),
    path('delete-product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('delete-category/<int:category_id>/', views.delete_category, name='delete_category'),
    path('edit-category/<int:category_id>/', views.edit_category, name='edit_category'),
]