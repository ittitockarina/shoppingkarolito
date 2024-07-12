from .models import StoreCategory, StoreProduct, StoreOrder, StoreOrderItem

from django.contrib import admin

admin.site.register(StoreCategory)
admin.site.register(StoreProduct)
admin.site.register(StoreOrder)
admin.site.register(StoreOrderItem)
